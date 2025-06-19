import pathlib

import fire

from src import img


def update_images() -> None:
    """Update generated images from the images/ folder."""
    updater = img.Updater(tool_name=pathlib.Path(__file__).name)
    updater.run()


if __name__ == "__main__":
    fire.Fire(update_images)
