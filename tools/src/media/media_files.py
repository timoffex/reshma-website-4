from __future__ import annotations

import dataclasses
import pathlib
from typing import Generic, TypeVar

from . import output_media_path
from . import source_media_path


_Source = TypeVar("_Source", bound=source_media_path.SourceMediaPath)
_Output = TypeVar("_Output", bound=output_media_path.OutputMediaPath)


def find_all(
    source_type: type[_Source],
    output_type: type[_Output],
) -> MediaFiles[_Source, _Output]:
    """Returns paths to all source and generated media of a type."""

    sources: list[_Source] = []
    outputs: list[_Output] = []

    bad_sources: list[pathlib.Path] = []
    bad_outputs: list[pathlib.Path] = []

    source_type.root_folder().mkdir(parents=True, exist_ok=True)
    output_type.root_folder().mkdir(parents=True, exist_ok=True)

    for path in source_type.root_folder().iterdir():
        try:
            src = source_type.from_path(path)
        except ValueError:
            bad_sources.append(path)
        else:
            sources.append(src)

    for path in output_type.root_folder().iterdir():
        try:
            out = output_type.from_path(path)
        except ValueError:
            bad_outputs.append(path)
        else:
            outputs.append(out)

    return MediaFiles(
        source_paths=sorted(sources),
        bad_source_paths=sorted(bad_sources),
        output_paths=sorted(outputs),
        bad_output_paths=sorted(bad_outputs),
    )


@dataclasses.dataclass(frozen=True)
class MediaFiles(Generic[_Source, _Output]):
    source_paths: list[_Source]
    """Paths to existing source media files, sorted."""

    bad_source_paths: list[pathlib.Path]
    """Invalid files in the source folder, sorted."""

    output_paths: list[_Output]
    """Paths to existing output media files, sorted."""

    bad_output_paths: list[pathlib.Path]
    """Invalid files in the output folder, sorted"""

    @property
    def sources_by_name(self) -> dict[str, _Source]:
        """A dictionary mapping source names to existing source paths."""
        return {src.name: src for src in self.source_paths}

    @property
    def orphaned_outputs(self) -> list[_Output]:
        """Output files with no corresponding source path."""
        return [
            out for out in self.output_paths if out.name not in self.sources_by_name
        ]

    def get_up_to_date(
        self,
        source: _Source,
        *,
        width: int,
        extension: str,
    ) -> _Output | None:
        """Returns an up-to-date output for the parameters.

        Args:
            source: The source file.
            width: The output width to search for.
            extension: The output extension to search for.
        """
        output = self.find_output(
            name=source.name,
            width=width,
            extension=extension,
        )
        if not output:
            return None

        source_mtime = source.path.stat().st_mtime
        output_mtime = output.path.stat().st_mtime
        return output if output_mtime > source_mtime else None

    def find_output(
        self,
        *,
        name: str,
        width: int,
        extension: str,
    ) -> _Output | None:
        """Find an output file by name, width and extension."""
        for output in self.output_paths:
            if (
                output.name == name
                and output.width == width
                and output.extension == extension
            ):
                return output

        return None
