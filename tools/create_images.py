import itertools
import os
import pathlib


from src import images


SCALES = [1.0, 0.8, 0.5, 0.2]
EXTENSIONS = ["webp", "jpeg"]
IMAGES_TS = pathlib.Path("src/lib/generated-images.ts")


source_images: list[images.SourceImage] = []


for image in images.find_all_images():
    # Delete generated images whose source files got deleted.
    if not image.source:
        print(f"{image.camel_case} does not exist, deleting generated images:")
        for generated_image in image.generated_images:
            print(f"\tDeleting {generated_image.path}")
            os.remove(generated_image.path)
        continue

    source_images.append(image.source)

    scaled_widths = list(map(image.source.rescaled_width, SCALES))

    # Delete generated images with unused scales or extensions.
    for generated_image in image.generated_images:
        if (
            generated_image.width not in scaled_widths
            or generated_image.extension not in EXTENSIONS
        ):
            print(
                f"Unused width/extension combination, deleting {generated_image.path}"
            )
            os.remove(generated_image.path)

    # Generate scaled and converted versions of all images.
    for ext, scale in itertools.product(EXTENSIONS, SCALES):
        print(f"Generating {ext} {scale}x of {image.camel_case}")
        generated = image.source.generate(scale=scale, ext=ext)
        if not generated:
            print("\t... already up to date!")


with IMAGES_TS.open("w") as images_ts:
    images_ts.write(f"// AUTO-GENERATED BY {pathlib.Path(__file__).name}\n\n")

    for image in source_images:
        webp_sources = ",".join(
            [
                f"{{ src: '{generated_img.url}', width: {generated_img.width} }}"
                for generated_img in image.generated_files
                if generated_img.extension == "webp"
            ]
        )
        jpeg_sources = ",".join(
            [
                f"{{ src: '{generated_img.url}', width: {generated_img.width} }}"
                for generated_img in image.generated_files
                if generated_img.extension == "jpeg"
            ]
        )

        images_ts.write(
            f"export const {image.ts_name} = {{\n"
            f"    blurhash: '{image.blurhash}',\n"
            f"    aspectRatio: {image.aspect_ratio},\n"
            f"    webpSources: [{webp_sources}],\n"
            f"    jpegSources: [{jpeg_sources}],\n"
            f"}};\n"
        )
