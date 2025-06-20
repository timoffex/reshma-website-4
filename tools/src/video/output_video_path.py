from __future__ import annotations

import pathlib
from typing import final, override

from src import media


ROOT_FOLDER = pathlib.Path("static/videos/")
_URL_BASE = "/videos"


@final
class OutputVideoPath(media.OutputMediaPath):
    """Path to a generated video."""

    @override
    @classmethod
    def root_folder(cls) -> pathlib.Path:
        return ROOT_FOLDER

    @override
    @classmethod
    def _url_base(cls) -> str:
        return _URL_BASE

    @override
    @classmethod
    def known_extensions(cls) -> list[str]:
        return ["webm", "mp4"]
