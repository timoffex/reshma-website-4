<script>
  import { fadeInOut } from '$lib/fade-in-out';
  import { MetaBlueprint } from '$lib/generated-images';
  import { gridASizesList } from '$lib/layout/layout';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';
</script>

<a
  href="/meta"
  class="display-block tile grid-area-meta meta-gradient"
  use:fadeInOut
>
  <GeneratedImage
    imgClass="fill-contain image-color-on-hover"
    image={{
      alt: 'Meta',
      ...MetaBlueprint
    }}
    sizes={gridASizesList(3)}
  />
</a>

<style lang="scss">
  .meta-gradient {
    --outer-gradient-color: rgba(148, 187, 233, 1);
    background: radial-gradient(
      circle,
      rgba(227, 227, 227, 1) 0%,
      var(--outer-gradient-color) 100%
    );
  }

  // Match image-color-on-hover behavior.
  @media (any-hover: hover) {
    .meta-gradient {
      --outer-gradient-color: rgba(148, 148, 148, 1);

      &:hover,
      &:focus-visible {
        --outer-gradient-color: rgba(148, 187, 233, 1);
      }
    }
  }
</style>
