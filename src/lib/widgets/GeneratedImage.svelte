<!-- @component A picture element that displays an auto-generated image. -->
<script lang="ts">
  import { decode } from 'blurhash';
  import { onMount } from 'svelte';

  interface Props {
    image: {
      /** The blurhash for the image (https://blurha.sh). */
      blurhash: string;

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

  let img: HTMLImageElement | undefined = $state();

  // On mount (so in JavaScript) render the image's blurhash while it loads.
  onMount(() => {
    // Don't do anything if the image already loaded.
    // https://stackoverflow.com/a/1977898/2640146
    if (img!.complete && img!.naturalWidth > 0) return;

    const urlForBlurhash = (() => {
      const pixels = decode(image.blurhash, 32, 32);

      const canvas = document.createElement('canvas');
      canvas.width = 32;
      canvas.height = 32;

      const ctx = canvas.getContext('2d')!;
      const imageData = ctx.createImageData(32, 32);
      imageData.data.set(pixels);
      ctx.putImageData(imageData, 0, 0);

      return canvas.toDataURL();
    })();

    img!.style.backgroundImage = `url("${urlForBlurhash}")`;
    img!.style.backgroundSize = '100% 100%';

    // Remove the background on load to avoid breaking transparent images.
    img!.addEventListener('load', () => {
      img!.style.backgroundImage = 'unset';
      img!.style.backgroundSize = 'unset';
    });
  });
</script>

<picture>
  {#if image.webpSources}
    <source type="image/webp" srcset={srcsetFrom(image.webpSources)} {sizes} />
  {/if}
  {#if image.jpegSources}
    <source type="image/jpeg" srcset={srcsetFrom(image.jpegSources)} {sizes} />
  {/if}
  <img bind:this={img} {alt} src={TRANSPARENT_1x1} class={imgClass} />
</picture>
