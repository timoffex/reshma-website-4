<!-- @component A responsive video element that displays a silent, looping video.

This is a <video> element with display: block.
-->
<script lang="ts">
  import { onMount } from 'svelte';
  import type { ClassValue } from 'svelte/elements';

  interface Props {
    video: {
      /** Where to get the WebM versions of the video. */
      webmSources: Array<VideoSource>;

      /** Where to get the MP4 versions of the video. */
      mp4Sources: Array<VideoSource>;
    };

    class?: ClassValue;
  }

  interface VideoSource {
    src: string;
    width: number;
  }

  let { video, class: classList }: Props = $props();

  let elem: HTMLVideoElement;
  let bestWebM: string | undefined = $state();
  let bestMp4: string | undefined = $state();

  const bestSrcForSize = (
    srcs: Array<VideoSource>,
    width: number
  ): string | undefined => {
    let best: VideoSource | undefined;

    for (const source of srcs) {
      if (source.width == width) return source.src;

      if (
        // If there's no best choice, the first choice is best.
        best === undefined ||
        // If the best is below target width, any bigger choice is better.
        (best.width < width && source.width > best.width) ||
        // Otherwise, any smaller choice above target width is better.
        (best.width > width &&
          width < source.width &&
          source.width < best.width)
      ) {
        best = source;
      }
    }

    return best?.src;
  };

  onMount(() => {
    const initialWidth = elem.clientWidth;

    bestWebM = bestSrcForSize(video.webmSources, initialWidth);
    bestMp4 = bestSrcForSize(video.mp4Sources, initialWidth);
  });
</script>

<video
  bind:this={elem}
  autoplay
  loop
  muted
  playsinline
  tabindex={-1}
  class={['display-block', classList]}
>
  {#if bestWebM}
    <source type="video/webm" src={bestWebM} />
  {/if}
  {#if bestMp4}
    <source type="video/mp4" src={bestMp4} />
  {/if}
</video>
