<script>
  import { fadeInOut } from '$lib/fade-in-out';
  import { NinjaLogo } from '$lib/generated-images';
  import { gridASizesList } from '$lib/layout/layout';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';
</script>

<a
  href="/ninja"
  class="display-block tile grid-area-ninja bg-black highlight:bg-dark-blue"
  use:fadeInOut
>
  <GeneratedImage
    imgClass="fill-contain"
    image={{
      alt: 'Ninja (streamer)',
      ...NinjaLogo
    }}
    sizes={gridASizesList(3)}
  />
</a>
