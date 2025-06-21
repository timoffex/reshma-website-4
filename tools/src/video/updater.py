from __future__ import annotations

import itertools
import pathlib
import sys
import tempfile

import rich
import rich.console
from rich.markup import escape

from src import media

from .generated_videos_file import GeneratedVideosEntry, GeneratedVideosInfo
from .ffmpeg import ffmpeg_convert, ffmpeg_get_size
from .source_video_path import SourceVideoPath
from .output_video_path import OutputVideoPath

_EXTENSIONS = ["webm", "mp4"]
_SCALES = [1.0, 0.8, 0.5, 0.2]


class Updater:
    """Program for generating converted and rescaled videos."""

    def __init__(self, *, tool_name: str) -> None:
        self._tool_name = tool_name
        self._console = rich.console.Console(stderr=True)
        self._initial_files = media.find_all(SourceVideoPath, OutputVideoPath)

        self._output_info = GeneratedVideosInfo()
        self._stale = set(self._initial_files.output_paths)
        self._unchanged: set[OutputVideoPath] = set()

    def run(self) -> None:
        """Update generated videos."""
        self._error_on_bad_files()
        self._generate_videos()
        self._output_info.write(tool_name=self._tool_name)
        self._remove_stale()

    def _error_on_bad_files(self) -> None:
        """Print an error if any bad paths were found."""
        if (
            not self._initial_files.bad_source_paths
            and not self._initial_files.bad_output_paths
        ):
            return

        self._console.print("[red]Invalid files found![/red]")
        for path in (
            *self._initial_files.bad_source_paths,
            *self._initial_files.bad_output_paths,
        ):
            self._console.print(f"  [cyan]{escape(str(path))}[/cyan]")

        self._console.print(
            "Video file names must consist of lowercase letters, digits and"
            " numbers. The allowed extensions for source videos are"
            f" {OutputVideoPath.known_extensions()}. Please remove invalid"
            " files and try again."
        )
        sys.exit(1)

    def _generate_videos(self) -> None:
        """Generate scaled and converted versions of all source videos."""
        for source in self._initial_files.source_paths:
            outputs_for_source = []

            source_width, source_height = ffmpeg_get_size(source.path)

            for ext, scale in itertools.product(_EXTENSIONS, _SCALES):
                output = self._save_scaled_video(
                    source,
                    source_width=source_width,
                    source_height=source_height,
                    scale=scale,
                    extension=ext,
                )
                self._stale.discard(output)

                outputs_for_source.append(output)

            self._output_info.add(
                GeneratedVideosEntry(
                    source_name=source.name,
                    aspect_ratio=source_width / source_height,
                    output_paths=outputs_for_source,
                )
            )

    def _save_scaled_video(
        self,
        source: SourceVideoPath,
        *,
        source_width: int,
        source_height: int,
        scale: float,
        extension: str,
    ) -> OutputVideoPath:
        """Save a rescaled version of the given video.

        Does nothing if the rescaled version is up-to-date.

        Args:
            source: The source video path.
            source_width: Source video's width.
            source_height: Source video's height.
            scale: The scaling factor to use.
            extension: The output format.

        Returns:
            The path to the generated video.
        """
        output_width = int(scale * source_width)
        output_height = int(scale * source_height)

        # h.264 requires dimensions to be even.
        output_width += output_width % 2
        output_height += output_height % 2

        # Skip if the video is up to date.
        if old_output := self._initial_files.get_up_to_date(
            source,
            width=output_width,
            extension=extension,
        ):
            self._unchanged.add(old_output)
            return old_output

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_file = pathlib.Path(tmp_dir, f"{source.name}.{extension}")

            ffmpeg_convert(
                source=source.path,
                target=tmp_file,
                target_width=output_width,
                target_height=output_height,
                extension=extension,
            )

            output = OutputVideoPath.from_content(
                content=tmp_file,
                name=source.name,
                width=output_width,
                extension=extension,
            )

            output.path.unlink(missing_ok=True)
            tmp_file.rename(output.path)
            self._console.print(f"Generated [cyan]{escape(str(output.path))}[/cyan]")

            return output

    def _remove_stale(self) -> None:
        """Remove stale files after having generated videos."""
        if not self._stale:
            self._console.print("All videos were up to date.")
            return

        for output in self._stale:
            output.path.unlink()

        self._console.print(f"Removed {len(self._stale)} stale files.")
