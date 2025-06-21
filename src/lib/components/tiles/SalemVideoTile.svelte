<script>
  import { fadeInOut } from '$lib/fade-in-out';
  import VideoAnimation from '$lib/widgets/VideoAnimation.svelte';
  import { SalemPs5Reel } from '$lib/generated-videos';
</script>

<a href="/salem" class="display-block tile grid-area-salem" use:fadeInOut>
  <VideoAnimation
    video={SalemPs5Reel}
    class="fill-contain image-color-on-hover bg-black"
  />
</a>
