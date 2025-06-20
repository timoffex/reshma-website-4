from __future__ import annotations

import abc
import dataclasses
import functools
import pathlib
import re
from typing import Self


@dataclasses.dataclass(frozen=True)
@functools.total_ordering
class OutputMediaPath(abc.ABC):
    """Path to a generated image or video."""

    path: pathlib.Path

    name: str
    width: int
    sha: str
    extension: str

    @property
    def url(self) -> str:
        """The URL for accessing this file in TypeScript."""
        return f"{self._url_base()}/{self.path.name}"

    @classmethod
    def create(
        cls,
        name: str,
        width: int,
        sha: str,
        extension: str,
    ) -> Self:
        """Create an output media path.

        Args:
            name: The name of the source file (without the extension).
            width: The output width in pixels.
            sha: The 10-digit hash of the output file's contents.
            extension: The file extension.
        """

        filename = f"{name}-{width}.{sha}.{extension}"

        return cls(
            path=cls.root_folder() / filename,
            name=name,
            width=width,
            sha=sha,
            extension=extension,
        )

    @classmethod
    def from_path(cls, path: pathlib.Path) -> Self:
        """Parses a path to an output image.

        Args:
            path: Path to an output image file, relative to the project root.

        Raises:
            ValueError: If the path is not in the right format.

        Returns:
            The parsed path, if it's valid.
        """
        if path.parent != cls.root_folder():
            raise ValueError(str(path))

        name_pat = r"[a-z\-]+"
        width_pat = r"\d+"
        hash_pat = r"[a-z0-9]{10}"
        ext_pat = "|".join(cls.known_extensions())
        match = re.fullmatch(
            rf"({name_pat})-({width_pat})\.({hash_pat})\.({ext_pat})",
            path.name,
        )
        if not match:
            raise ValueError(str(path))

        name, width, hash, extension = match.groups()
        return cls(
            path=path,
            name=name,
            width=int(width),
            sha=hash,
            extension=extension,
        )

    @classmethod
    @abc.abstractmethod
    def root_folder(cls) -> pathlib.Path:
        """The folder containing this type of generated file."""

    @classmethod
    @abc.abstractmethod
    def known_extensions(cls) -> list[str]:
        """The allowed output file extensions."""

    @classmethod
    @abc.abstractmethod
    def _url_base(cls) -> str:
        """The URL prefix to access the root folder, like '/images'."""

    def __hash__(self):
        return hash(self.path)

    def __lt__(self, other):
        if not isinstance(other, OutputMediaPath):
            return NotImplemented
        return self.path < other.path
