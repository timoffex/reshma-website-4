<script>
  import { fadeInOut } from '$lib/fade-in-out';

  if (typeof window !== 'undefined') import('@lottiefiles/lottie-player');

  const LOTTIE_PATH = 'yt-gaming-logo.jsonlottie';
</script>

<svelte:head>
  <link rel="preload" href={LOTTIE_PATH} as="fetch" />
</svelte:head>

<a
  href="/youtube-gaming"
  aria-label="YouTube Gaming"
  class="display-block tile grid-area-yt-gaming bg-black"
  use:fadeInOut
>
  <lottie-player
    autoplay
    loop
    src={LOTTIE_PATH}
    class="fill image-color-on-hover"
  ></lottie-player>
</a>
