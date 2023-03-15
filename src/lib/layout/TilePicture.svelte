<script lang="ts">
  import type { PictureA3, PictureB1, PictureB2 } from "./TilePicture";

  export let imgClass: string;
  export let loading: "lazy"|undefined = undefined;
  export let picture: PictureA3|PictureB1|PictureB2;
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
  
  <img
      class={imgClass}
      loading={loading} 
      alt={picture.alt}
      src={picture.jpeg175} />
{:else if (picture.case === 'gridB-1')}
  <source
      type="image/webp"
      srcset="{picture.webp174} 1x, {picture.webp348} 2x"
      width=174
      media="(min-width: calc(45rem + 16px))">

  <source
      type="image/webp"
      srcset="{picture.webp87} 1x, {picture.webp174} 2x"
      width=87>
  
  <source
      type="image/jpeg"
      srcset={picture.jpeg174}
      width=174
      media="(min-width: calc(45rem + 16px))">
  
  <source
      type="image/jpeg"
      srcset="{picture.jpeg87} 1x, {picture.jpeg174} 2x"
      width=87>
  
  <img
      class={imgClass}
      loading={loading} 
      alt={picture.alt}
      src={picture.jpeg87} />
{:else if (picture.case === 'gridB-2')}
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
  
  <img
      class={imgClass}
      loading={loading} 
      alt={picture.alt}
      src={picture.jpeg175} />
{/if}

</picture>