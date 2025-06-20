from __future__ import annotations

import pathlib
from typing import final, override

from src import media


ROOT_FOLDER = pathlib.Path("videos/")

@final
class SourceVideoPath(media.SourceMediaPath):
    """Path to a source video."""

    @override
    @classmethod
    def root_folder(cls) -> pathlib.Path:
        return ROOT_FOLDER

    @override
    @classmethod
    def known_extensions(cls) -> list[str]:
        return ["webm", "mp4"]
