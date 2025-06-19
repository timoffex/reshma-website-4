from __future__ import annotations

import dataclasses
import functools
import pathlib
import re


ROOT_FOLDER = pathlib.Path("images/")
_SOURCE_IMAGE_NAME_RE = re.compile(r"([a-z\-]+)\.(png|webp)")
"""Regex for the basename of a source image.

Groups:

1. The stem (name without extension).
2. The extension.
"""


def from_path(path: pathlib.Path) -> SourceImagePath:
    """Parses a file path into a source image path.

    Args:
        path: Path to a source image file, relative to the project root.

    Raises:
        ValueError: If the path is not a valid source image file.
    """
    if path.parent != ROOT_FOLDER:
        raise ValueError(str(path))

    match = _SOURCE_IMAGE_NAME_RE.fullmatch(path.name)
    if not match:
        raise ValueError(str(path))

    name, extension = match.groups()
    return SourceImagePath(
        path=path,
        name=name,
        extension=extension,
    )


@dataclasses.dataclass(frozen=True)
@functools.total_ordering
class SourceImagePath:
    """Path to a source image."""

    path: pathlib.Path
    name: str
    extension: str

    def __hash__(self):
        return hash(self.path)

    def __lt__(self, other):
        if not isinstance(other, SourceImagePath):
            return NotImplemented
        return self.path < other.path
