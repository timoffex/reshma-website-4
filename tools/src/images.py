import functools
import hashlib
import pathlib
import re
import subprocess
from typing import Callable, Optional
import warnings

import blurhash


_SOURCE_DIR = pathlib.Path("./images/")
_OUTPUT_DIR = pathlib.Path("./static/images/")
_URL_BASE = "/images"


# Images are snake-case.
_IMAGE_NAME_PATTERN = r"[a-z\-]+"
_IMAGE_NAME_RE = re.compile(_IMAGE_NAME_PATTERN)

# All source image extensions.
_SOURCE_END_PATTERN = r"\.(png|webp)"

# Output images have a width, a hash and an extension.
_OUTPUT_END_PATTERN = r"-(\d+)\.[a-z0-9]{10}\.(webp|jpeg)"


class SourceImage:
    """A source image that gets automatically resized and converted."""

    def __init__(self, name: "ImageName", path: pathlib.Path):
        self._image_name = name
        self._path = path

    def rescaled_width(self, scale: float) -> int:
        return int(scale * self.width)

    @functools.cached_property
    def size(self) -> tuple[int, int]:
        """Returns the width and height of this image."""
        [width, height] = subprocess.getoutput(
            f"identify -ping -format '%w,%h' {self._path}[0]"
        ).split(",")
        return (int(width), int(height))

    @property
    def path(self) -> pathlib.Path:
        return self._path

    @property
    def ts_name(self) -> str:
        return self._image_name.camel_case

    @property
    def width(self) -> int:
        return self.size[0]

    @property
    def aspect_ratio(self) -> float:
        return self.size[0] / self.size[1]

    @functools.cached_property
    def blurhash(self) -> str:
        with self._path.open("rb") as img_file:
            return blurhash.encode(img_file, x_components=4, y_components=4)

    @property
    def generated_files(self) -> list["GeneratedImage"]:
        return self._image_name.generated_images

    def generate(self, scale: float, ext: str) -> bool:
        """Generates a scaled and converted version of this image.

        Returns true if it generated a new file.
        """

        width = self.rescaled_width(scale)

        if self._image_name._is_generated_file_up_to_date(width, ext):
            return False

        args = ["convert"]
        if scale < 1:
            args.extend(["-resize", f"{scale:.0%}%"])
        args.append(str(self._path))

        self._image_name._create_generated_file(
            width,
            ext,
            lambda output_path: subprocess.check_call(args + [output_path]),
        )

        return True


class GeneratedImage:
    """An automatically generated image."""

    def __init__(
        self,
        name: "ImageName",
        source: Optional[pathlib.Path],
        path: pathlib.Path,
        width: int,
        ext: str,
    ):
        output_re = re.compile(f"{_IMAGE_NAME_PATTERN}{_OUTPUT_END_PATTERN}")
        if not output_re.fullmatch(path.name):
            warnings.warn(
                f"Generated image {path.name} does not match '{output_re.pattern}'"
            )

        self._name = name
        self._source = source
        self._path = path
        self._width = width
        self._ext = ext

    def __repr__(self):
        return f"<GeneratedImage '{self._path.name}'>"

    @property
    def path(self) -> pathlib.Path:
        return self._path

    @property
    def width(self) -> int:
        return self._width

    @property
    def extension(self) -> str:
        return self._ext

    @property
    def url(self) -> str:
        return f"{_URL_BASE}/{self._path.name}"

    def is_up_to_date(self) -> bool:
        """Whether this image is at least as new as its source."""
        if not self._source:
            return False

        return self._source.stat().st_mtime < self._path.stat().st_mtime


class ImageName:
    """An image in this project that gets automatically resized and converted."""

    def __init__(self, name: str):
        if not _IMAGE_NAME_RE.fullmatch(name):
            raise ValueError(f"'{name}' does not match '{_IMAGE_NAME_RE.pattern}'")

        self._name = name
        self._camel_case = "".join([part.capitalize() for part in name.split("-")])

    def __repr__(self):
        return f"Image({repr(self._name)})"

    @property
    def camel_case(self) -> str:
        return self._camel_case

    @property
    def source(self) -> Optional[SourceImage]:
        """The path to the source file for this image, if the file exists."""
        for file in _SOURCE_DIR.glob(f"{self._name}.*"):
            if re.fullmatch(_SOURCE_END_PATTERN, file.suffix):
                return SourceImage(self, file)

        return None

    @functools.cached_property
    def generated_images(self) -> list[GeneratedImage]:
        """The generated files for this image."""

        if not _OUTPUT_DIR.exists():
            return []

        regexp = re.compile(f"{self._name}{_OUTPUT_END_PATTERN}")

        source = self.source
        source_path = source.path if source else None

        files = []
        for file in _OUTPUT_DIR.iterdir():
            if match := regexp.fullmatch(file.name):
                files.append(
                    GeneratedImage(
                        self,
                        source=source_path,
                        path=file,
                        width=int(match.group(1)),
                        ext=match.group(2),
                    )
                )

        return files

    def _is_generated_file_up_to_date(self, width: int, ext: str) -> bool:
        for generated_image in self.generated_images:
            if generated_image.width == width and generated_image.extension == ext:
                return generated_image.is_up_to_date()
        
        return False

    def _create_generated_file(
        self,
        width: int,
        ext: str,
        generator: Callable[[pathlib.Path], None],
    ):
        """Creates a hashed file with the rescaled and converted version of the image."""

        # Reset the generated images cache.
        del self.generated_images

        if not _OUTPUT_DIR.exists():
            _OUTPUT_DIR.mkdir()

        initial_path = _OUTPUT_DIR / f"{self._name}-{width}.{ext}"
        generator(initial_path)
        hash = hashlib.shake_128(initial_path.read_bytes()).hexdigest(5)
        return initial_path.rename(_OUTPUT_DIR / f"{self._name}-{width}.{hash}.{ext}")


def find_all_images() -> list[ImageName]:
    """Finds all source images and generated images in the project."""

    source_re = re.compile(f"({_IMAGE_NAME_PATTERN}){_SOURCE_END_PATTERN}")
    output_re = re.compile(f"({_IMAGE_NAME_PATTERN}){_OUTPUT_END_PATTERN}")

    image_names = set()
    for file in _SOURCE_DIR.iterdir():
        if match := source_re.fullmatch(file.name):
            image_names.add(match.group(1))
    if _OUTPUT_DIR.exists():
        for file in _OUTPUT_DIR.iterdir():
            if match := output_re.fullmatch(file.name):
                image_names.add(match.group(1))

    return [ImageName(name) for name in image_names]
