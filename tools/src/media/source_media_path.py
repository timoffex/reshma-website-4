import abc
import dataclasses
import functools
import pathlib
import re
from typing import Self


@dataclasses.dataclass(frozen=True)
@functools.total_ordering
class SourceMediaPath(abc.ABC):
    """Path to a source image or video.

    All source media files use kebab-case naming and are placed in some
    root folder.
    """

    path: pathlib.Path
    name: str
    extension: str

    def __hash__(self):
        return hash(self.path)

    def __lt__(self, other):
        if not isinstance(other, SourceMediaPath):
            return NotImplemented
        return self.path < other.path

    @classmethod
    def from_path(cls, path: pathlib.Path) -> Self:
        """Parses a file path into a source image or video path.

        Args:
            path: Path to a source file relative to the project root.

        Raises:
            ValueError: If the path is not a valid source media file.
        """
        if path.parent != cls.root_folder():
            raise ValueError(str(path))

        name_pattern = r"[a-z\-]+"
        ext_pattern = "|".join(cls.known_extensions())
        match = re.fullmatch(rf"({name_pattern})\.({ext_pattern})", path.name)
        if not match:
            raise ValueError(str(path))

        name, extension = match.groups()
        return cls(path=path, name=name, extension=extension)

    @classmethod
    @abc.abstractmethod
    def root_folder(cls) -> pathlib.Path:
        """The folder containing this type of media."""

    @classmethod
    @abc.abstractmethod
    def known_extensions(cls) -> list[str]:
        """The allowed source file extensions."""
