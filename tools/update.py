import pathlib

import fire

from src import img, video


def update(
    images: bool = False,
    videos: bool = False,
) -> None:
    """Update generated files.

    Args:
        images: Whether to update images.
        videos: Whether to update videos.
    """
    tool_name = pathlib.Path(__file__).name

    if images:
        img.Updater(tool_name=tool_name).run()
    if videos:
        video.Updater(tool_name=tool_name).run()


if __name__ == "__main__":
    fire.Fire(update)
