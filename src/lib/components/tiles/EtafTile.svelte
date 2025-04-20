<script>
  import { fadeInOut } from '$lib/fade-in-out';
  import { EtafLogo } from '$lib/generated-images';
  import { gridASizesList } from '$lib/layout/layout';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';
</script>

<a
  href="/etaf"
  class="display-block tile grid-area-etaf bg-black highlight:etaf-purple"
  use:fadeInOut
>
  <GeneratedImage
    imgClass="fill-contain image-color-on-hover"
    image={{
      alt: 'Elizabeth Taylor AIDS Foundation',
      ...EtafLogo
    }}
    sizes={gridASizesList(3)}
  />
</a>

<style lang="scss">
  @media (any-hover: hover) {
    .highlight\:etaf-purple {
      &:hover,
      &:focus-visible {
        background: #6720a5;
      }
    }
  }
</style>
