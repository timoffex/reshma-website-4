import pathlib

import fire
from rich.console import Console
from rich.markup import escape
import subprocess


console = Console(stderr=True)


def lint_mp4(*files: str, fix: bool = False) -> None:
    """Detect if given MP4 files do not start with a moov atom.

    The 'moov' atom contains metadata that's necessary to start playing
    the video. Some programs put this at the end, causing browsers to have
    to load the entire file before they can play it.
    """
    for file in files:
        _lint_mp4(pathlib.Path(file), fix=fix)


def _lint_mp4(path: pathlib.Path, *, fix: bool) -> None:
    path_escaped = escape(str(path))

    if path.suffix != ".mp4":
        console.print(
            f"[red]ERROR[/red]Not an MP4: [cyan]{path_escaped}[/cyan]",
        )
        return

    with path.open("rb") as f:
        first_50_bytes = f.read(50)
        is_faststart = b"moov" in first_50_bytes

    console.print(f"[cyan]{path_escaped}[/cyan]: ", end="")
    if not is_faststart:
        console.print("[red]moov not near start[/red]")
        if fix:
            console.print("[yellow]Fixing...[/yellow]")
            _fix(path)
    else:
        console.print("[green]all good![/green]")


def _fix(path: pathlib.Path) -> None:
    output_name = f"{path.stem}_fast.mp4"
    output_path = path.parent / output_name

    ffmpeg_args = ["-i", str(path)]
    ffmpeg_args.extend(["-c", "copy"])
    ffmpeg_args.extend(["-movflags", "faststart"])
    ffmpeg_args.append(str(output_path))
    subprocess.check_call(["ffmpeg", *ffmpeg_args])

    path.unlink()
    output_path.rename(path)


if __name__ == "__main__":
    fire.Fire(lint_mp4)
