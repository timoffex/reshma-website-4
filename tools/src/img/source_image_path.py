from __future__ import annotations

import pathlib
from typing import final, override

from src import media


ROOT_FOLDER = pathlib.Path("images/")


@final
class SourceImagePath(media.SourceMediaPath):
    """Path to a source image."""

    @override
    @classmethod
    def root_folder(cls) -> pathlib.Path:
        return ROOT_FOLDER

    @override
    @classmethod
    def known_extensions(cls) -> list[str]:
        return ["webp", "png"]
