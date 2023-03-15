<script lang="ts">
  import type { PictureA3 } from "./TilePicture";

  export let imgClass: string;
  export let picture: PictureA3;
</script>

<picture>

{#if (picture.case === 'gridA-3')}
  <source
      type="image/webp"
      srcset="{picture.webp356} 1x, {picture.webp712} 2x"
      width=356
      media="(min-width: calc(45rem + 16px))">

  <source
      type="image/webp"
      srcset="{picture.webp175} 1x, {picture.webp356} 2x"
      width=175>
  
  <source
      type="image/jpeg"
      srcset={picture.jpeg356}
      width=356
      media="(min-width: calc(45rem + 16px))">
  
  <source
      type="image/jpeg"
      srcset="{picture.jpeg175} 1x, {picture.jpeg356} 2x"
      width=175>
  
  <img class={imgClass} alt={picture.alt} src={picture.jpeg175} />
{/if}

</picture>