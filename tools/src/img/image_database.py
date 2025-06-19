from __future__ import annotations

import dataclasses
import pathlib

from . import output_image_path
from . import source_image_path


def find_all() -> ImageFiles:
    """Returns paths to all existing files relevant to image generation."""

    sources: list[source_image_path.SourceImagePath] = []
    outputs: list[output_image_path.OutputImagePath] = []

    bad_sources: list[pathlib.Path] = []
    bad_outputs: list[pathlib.Path] = []

    for path in source_image_path.ROOT_FOLDER.iterdir():
        try:
            src = source_image_path.from_path(path)
        except ValueError:
            bad_sources.append(path)
        else:
            sources.append(src)

    for path in output_image_path.ROOT_FOLDER.iterdir():
        try:
            out = output_image_path.from_path(path)
        except ValueError:
            bad_outputs.append(path)
        else:
            outputs.append(out)

    return ImageFiles(
        source_paths=sorted(sources),
        bad_source_paths=sorted(bad_sources),
        output_paths=sorted(outputs),
        bad_output_paths=sorted(bad_outputs),
    )


@dataclasses.dataclass(frozen=True)
class ImageFiles:
    source_paths: list[source_image_path.SourceImagePath]
    """Paths to existing source image files, sorted."""

    bad_source_paths: list[pathlib.Path]
    """Invalid files in the source folder, sorted."""

    output_paths: list[output_image_path.OutputImagePath]
    """Paths to existing output image files, sorted."""

    bad_output_paths: list[pathlib.Path]
    """Invalid files in the output folder, sorted"""

    @property
    def sources_by_name(self) -> dict[str, source_image_path.SourceImagePath]:
        """A dictionary mapping source names to existing source paths."""
        return {src.name: src for src in self.source_paths}

    @property
    def orphaned_outputs(self) -> list[output_image_path.OutputImagePath]:
        """Output files with no corresponding source path."""
        return [
            out
            for out in self.output_paths
            if out.name not in self.sources_by_name
        ]

    def find_output(
        self,
        *,
        name: str,
        width: int,
        extension: str,
    ) -> output_image_path.OutputImagePath | None:
        """Find an output file by name, width and extension."""
        for output in self.output_paths:
            if (
                output.name == name
                and output.width == width
                and output.extension == extension
            ):
                return output

        return None
