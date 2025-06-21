"""Utilities for using ffmpeg."""

from __future__ import annotations

import pathlib
import re
import subprocess


class FfmpegError(Exception):
    """An ffmpeg command didn't work."""


def ffmpeg_convert(
    *,
    source: pathlib.Path,
    target: pathlib.Path,
    target_width: int,
    target_height: int,
    extension: str,
) -> None:
    """Rescale and convert a video.

    Args:
        source: The source video to convert.
        target: The output path. Its extension must be extension.
        target_width: The output's desired width in pixels.
        target_height: The output's desired height in pixels.
        extension: The desired output format.
    """
    if target.suffix != f".{extension}":
        raise ValueError(f"Target {target} does not end with {extension}.")

    input_options = ["-i", str(source)]
    scale_options = ["-vf", f"scale={target_width}x{target_height}"]

    if extension == "mp4":
        format_options = ["-movflags", "faststart"]
    else:
        format_options = []

    try:
        subprocess.run(
            [
                "ffmpeg",
                *input_options,
                *scale_options,
                *format_options,
                str(target),
            ],
            capture_output=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise FfmpegError(
            f"Command {e.cmd} exited with {e.returncode}:\n{e.stderr.decode()}"
        ) from None


def ffmpeg_get_size(source: pathlib.Path) -> tuple[int, int]:
    """Get the width and height of a video.

    Args:
        source: A video file.

    Returns:
        The (width, height) of the video.
    """
    command = ["ffprobe"]
    command += ["-v", "error"]  # Don't print anything extra except on error.
    command += ["-select_streams", "v:0"]  # Read the first video stream.
    command += ["-show_entries", "stream=width,height"]  # Print stream's size.

    # Output options:
    # - Use 'x' as the field separator (the fields above are width and height).
    # - Don't print section names.
    command += ["-of", "csv=s=x:p=0"]

    command.append(str(source))

    try:
        result = subprocess.run(command, capture_output=True, check=True)
        output = result.stdout.decode()
    except subprocess.CalledProcessError as e:
        raise FfmpegError(
            f"Command {e.cmd} exited with {e.returncode}:\n{e.stderr.decode()}"
        ) from None

    match = re.fullmatch(r"(\d+)x(\d+)", output.strip())
    if not match:
        raise ValueError(output)

    width, height = match.groups()
    return int(width), int(height)
