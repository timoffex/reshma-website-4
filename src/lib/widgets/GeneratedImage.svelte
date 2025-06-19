<!-- @component A picture element that displays an auto-generated image. -->
<script lang="ts">
  interface Props {
    image: {
      /** Where to get the WebP versions of the image. */
      webpSources: Array<{ src: string; width: number }>;

      /** Where to get the JPEG versions of the image. */
      jpegSources: Array<{ src: string; width: number }>;
    };

    /** The alt text for the image. */
    alt: string;

    /** Sizes attribute for source elements. */
    sizes: string;

    /** Additional class for the img element. */
    imgClass?: string;
  }

  let { image, alt, sizes, imgClass }: Props = $props();

  /** Transparent 1x1 image to show as an image background. */
  const TRANSPARENT_1x1 =
    'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNgYAAAAAMAASsJTYQAAAAASUVORK5CYII=';

  /** Converts a list of sources to an srcset. */
  const srcsetFrom = (
    sources: Array<{ src: string; width: number }>
  ): string => {
    if (sources.length === 1) {
      return sources[0].src;
    } else {
      return sources.map((s) => `${s.src} ${s.width}w`).join(',');
    }
  };
</script>

<picture>
  {#if image.webpSources}
    <source type="image/webp" srcset={srcsetFrom(image.webpSources)} {sizes} />
  {/if}
  {#if image.jpegSources}
    <source type="image/jpeg" srcset={srcsetFrom(image.jpegSources)} {sizes} />
  {/if}
  <img {alt} src={TRANSPARENT_1x1} class={imgClass} />
</picture>
