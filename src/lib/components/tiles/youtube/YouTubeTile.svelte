<script>
  import { fadeInOut } from '$lib/fade-in-out';
</script>

<a
  href="/youtube"
  class={[
    'display-block',
    'tile',
    'grid-area-youtube',
    'bg-black',
    'padding-2',
    'ytg-gradient-1',
    'image-color-on-hover-2'
  ]}
  use:fadeInOut
>
  <div class="fill padding-2">
    <enhanced:img
      alt="YouTube Core"
      src="$lib/components/youtube-logo.svg"
      class="fill-contain"
    />
  </div>
</a>

<style lang="scss">
  @use '$lib/layout/layout';

  @media (any-hover: hover) {
    .ytg-gradient-1 {
      &:hover,
      &:focus-visible {
        color: white;
        background: radial-gradient(circle, rgba(0 92 255) 100%);
      }
    }
  }

  .padding-2 {
    box-sizing: border-box;
    padding: 2 * layout.$spacing;
  }
</style>
