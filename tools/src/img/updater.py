from __future__ import annotations

import io
import itertools
import sys

from PIL import Image
import rich
import rich.console
from rich.markup import escape

from src import media

from .generated_images_file import GeneratedImagesEntry, GeneratedImagesInfo
from .source_image_path import SourceImagePath
from .output_image_path import OutputImagePath

_SCALES = [1.0, 0.8, 0.5, 0.2]


class Updater:
    """Program for generating converted and rescaled images."""

    def __init__(self, *, tool_name: str) -> None:
        self._tool_name = tool_name
        self._console = rich.console.Console(stderr=True)
        self._initial_files = media.find_all(SourceImagePath, OutputImagePath)

        self._output_info = GeneratedImagesInfo()
        self._stale = set(self._initial_files.output_paths)
        self._unchanged: set[OutputImagePath] = set()

    def run(self) -> None:
        """Update generated images."""
        self._error_on_bad_files()
        self._generate_images()
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
            "Image file names must consist of lowercase letters, digits and"
            " numbers. The allowed extensions for source images are png"
            " and webp. Please remove invalid files and try again."
        )
        sys.exit(1)

    def _generate_images(self) -> None:
        """Generate scaled and converted versions of all source images."""
        for source in self._initial_files.source_paths:
            with Image.open(source.path) as source_img:
                outputs_for_source = []

                if getattr(source_img, "is_animated", False):
                    self._console.print(
                        "[red]Animations not supported, skipping:[/red]"
                        f" [cyan]{escape(str(source.path))}[/cyan]"
                    )
                    continue

                if not source_img.has_transparency_data:
                    extensions = ["jpeg", "webp"]
                elif (
                    (extrema := source_img.getchannel("A").getextrema())
                    and extrema[0] == extrema[1]
                ):
                    source_img = source_img.convert(mode="RGB")
                    extensions = ["jpeg", "webp"]
                else:
                    extensions = ["webp"]

                for ext, scale in itertools.product(extensions, _SCALES):
                    output = self._save_scaled_image(
                        source,
                        source_img,
                        scale=scale,
                        extension=ext,
                    )
                    self._stale.discard(output)

                    outputs_for_source.append(output)

                self._output_info.add(
                    GeneratedImagesEntry(
                        source_name=source.name,
                        aspect_ratio=source_img.width / source_img.height,
                        output_paths=outputs_for_source,
                    )
                )

    def _save_scaled_image(
        self,
        source: SourceImagePath,
        image: Image.Image,
        *,
        scale: float,
        extension: str,
    ) -> OutputImagePath:
        """Save a rescaled version of the given image.

        Does nothing if the rescaled version is up-to-date.

        Args:
            source: The source image path.
            image: The opened Image object.
            scale: The scaling factor to use.
            extension: The output format.

        Returns:
            The path to the generated image.
        """
        output_width = int(scale * image.width)
        output_height = int(scale * image.height)

        # Skip if the image is up to date.
        if (old_output := self._initial_files.find_output(
            name=source.name,
            width=output_width,
            extension=extension,
        )) and old_output.path.stat().st_mtime > source.path.stat().st_mtime:
            self._unchanged.add(old_output)
            return old_output

        # Rescale the image.
        scaled_image = image.resize((output_width, output_height))

        # Get the image's bytes.
        output_image_bytes = io.BytesIO()
        scaled_image.save(output_image_bytes, format=extension)

        output = OutputImagePath.from_content(
            content=output_image_bytes.getbuffer(),
            name=source.name,
            width=output_width,
            extension=extension,
        )

        self._console.print(
            f"Generating [cyan]{escape(str(output.path))}[/cyan]"
        )

        # Save the image to file.
        with output.path.open("wb") as f:
            f.write(output_image_bytes.getbuffer())

        return output

    def _remove_stale(self) -> None:
        """Remove stale files after having generated images."""
        if not self._stale:
            self._console.print("All images were up to date.")
            return

        for output in self._stale:
            output.path.unlink()

        self._console.print(f"Removed {len(self._stale)} stale files.")
