from __future__ import annotations

import dataclasses
import pathlib

from .output_image_path import OutputImagePath


_TS_PATH = pathlib.Path("src/lib/generated-images.ts")


@dataclasses.dataclass(frozen=True)
class GeneratedImagesEntry:
    """An entry in the generates-images.ts file."""

    source_name: str
    aspect_ratio: float
    output_paths: list[OutputImagePath]


class GeneratedImagesInfo:
    """An object to construct the generated-images.ts file."""

    def __init__(self) -> None:
        self._entries: list[GeneratedImagesEntry] = []

    def add(self, entry: GeneratedImagesEntry) -> None:
        """Add an entry to the file."""
        self._entries.append(entry)

    def write(self, *, tool_name: str) -> None:
        """Generate the file.

        Args:
            tool_name: The tool name to mention in a comment at the top.
        """
        with _TS_PATH.open("w") as images_ts:
            images_ts.write(f"// AUTO-GENERATED BY {tool_name}\n\n")

            self._entries.sort(key=lambda entry: entry.source_name)
            for entry in self._entries:
                webp_sources = _ts_sources_list(entry.output_paths, "webp")
                jpeg_sources = _ts_sources_list(entry.output_paths, "jpeg")

                images_ts.write(
                    f"export const {_kebab_to_camel(entry.source_name)} = {{\n"
                    f"    aspectRatio: {entry.aspect_ratio},\n"
                    f"    webpSources: {webp_sources},\n"
                    f"    jpegSources: {jpeg_sources},\n"
                    f"}};\n"
                )


def _ts_sources_list(
    outputs: list[OutputImagePath],
    extension: str,
) -> str:
    sources = ",".join(
        [
            f"{{ src: '{output.url}', width: {output.width} }}"
            for output in outputs
            if output.extension == extension
        ]
    )

    return f"[{sources}]"


def _kebab_to_camel(kebab: str) -> str:
    """Convert a kebab-case string to a camelCase string."""
    return "".join([part.capitalize() for part in kebab.split("-")])
