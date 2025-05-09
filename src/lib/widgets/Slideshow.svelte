<script lang="ts">
  import { onMount } from 'svelte';

  type SlideshowImage = {
    alt: string;
    defaultSrc: string;
    webpSrcset: string;
    jpegSrcset: string;
  };

  interface Props {
    images: SlideshowImage[];
    sizes: string;
    delayMs: number;
  }

  let { images, sizes, delayMs }: Props = $props();

  let idx = $state(0);

  onMount(() => {
    const t = setInterval(() => {
      idx = mod(idx + 1, images.length);
    }, delayMs);

    return () => clearInterval(t);
  });

  /** Modulo operator that only returns positive numbers. */
  const mod = (a: number, b: number) => {
    return ((a % b) + b) % b;
  };

  let currIdx = $derived(mod(idx, images.length));
  let prevIdx = $derived(mod(idx - 1, images.length));
  let curr = $derived(images[currIdx]);
  let prev = $derived(images[prevIdx]);
</script>

<div class="slides-container">
  {#key prevIdx}
    <picture>
      <source type="image/webp" srcset={prev.webpSrcset} {sizes} />
      <source type="image/jpeg" srcset={prev.jpegSrcset} {sizes} />
      <img src={prev.defaultSrc} alt={prev.alt} class="slide-old" />
    </picture>
  {/key}
  {#key currIdx}
    <picture>
      <source type="image/webp" srcset={curr.webpSrcset} {sizes} />
      <source type="image/jpeg" srcset={curr.jpegSrcset} {sizes} />
      <img src={curr.defaultSrc} alt={curr.alt} class="slide-new" />
    </picture>
  {/key}
</div>

<style lang="scss">
  .slides-container {
    position: relative;
    overflow: hidden;

    width: 100%;
    height: 100%;
  }

  .slide-old {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    object-fit: contain;

    opacity: 0;
    animation: fade-out 0.5s;
  }

  .slide-new {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    object-fit: contain;

    animation: slide-in 0.5s ease-in-out;
  }

  @keyframes slide-in {
    0% {
      transform: translateX(100%);
    }
    100% {
      transform: translateX(0);
    }
  }

  @keyframes fade-out {
    0% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
</style>
