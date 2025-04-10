<script>
  import { fadeInOut } from '$lib/fade-in-out';

  if (typeof window !== 'undefined') import('@lottiefiles/lottie-player');

  const LOTTIE_PATH = 'wetransfer3.jsonlottie';
</script>

<a
  href="/wetransfer"
  aria-label="WeTransfer"
  class="display-block tile grid-area-wetransfer bg-black highlight:bg-red"
  use:fadeInOut
>
  <lottie-player
    autoplay
    loop
    src={LOTTIE_PATH}
    class="fill image-color-on-hover"
  ></lottie-player>
</a>
