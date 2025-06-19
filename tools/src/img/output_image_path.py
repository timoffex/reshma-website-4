from __future__ import annotations

import dataclasses
import pathlib
import re


ROOT_FOLDER = pathlib.Path("static/images/")

_URL_BASE = "/images"

_WIDTH = r"\d+"
_HASH = r"[a-z0-9]{10}"
_OUTPUT_IMAGE_NAME_RE = re.compile(
    rf"([a-z\-]+)-({_WIDTH})\.({_HASH})\.(webp|jpeg)",
)
"""Regex for the basename of a generated image.

Groups:

1. The stem of the source image (name without extension).
2. The width.
3. The hash.
4. The extension.
"""


def from_path(path: pathlib.Path) -> OutputImagePath:
    """Parses a path to an output image.

    Args:
        path: Path to an output image file, relative to the project root.

    Raises:
        ValueError: If the path is not in the right format.

    Returns:
        The parsed path, if it's valid.
    """
    if path.parent != ROOT_FOLDER:
        raise ValueError(str(path))

    match = _OUTPUT_IMAGE_NAME_RE.fullmatch(path.name)
    if not match:
        raise ValueError(str(path))

    name, width, hash, extension = match.groups()
    return OutputImagePath(
        path=path,
        name=name,
        width=int(width),
        sha=hash,
        extension=extension,
    )




@dataclasses.dataclass(frozen=True)
class OutputImagePath:
    """Path to a generated image."""

    path: pathlib.Path

    name: str
    width: int
    sha: str
    extension: str

    @property
    def url(self) -> str:
        """The URL for accessing this image in TypeScript."""
        return f"{_URL_BASE}/{self.path.name}"

    @staticmethod
    def create(
        name: str,
        width: int,
        sha: str,
        extension: str,
    ) -> OutputImagePath:
        """Create an output image path.

        Args:
            name: The name of the source image (without the extension).
            width: The output width in pixels.
            sha: The 10-digit hash of the output image.
            extension: The file extension.
        """

        filename = f"{name}-{width}.{sha}.{extension}"

        return OutputImagePath(
            path=ROOT_FOLDER / filename,
            name=name,
            width=width,
            sha=sha,
            extension=extension,
        )

    def __hash__(self):
        return hash(self.path)

    def __lt__(self, other):
        if not isinstance(other, OutputImagePath):
            return NotImplemented
        return self.path < other.path
