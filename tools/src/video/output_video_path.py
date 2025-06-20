from __future__ import annotations

import pathlib
from typing import final, override

from src.media import output_media_path


ROOT_FOLDER = pathlib.Path("static/videos/")
_URL_BASE = "/videos"


@final
class OutputVideoPath(output_media_path.OutputMediaPath):
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
