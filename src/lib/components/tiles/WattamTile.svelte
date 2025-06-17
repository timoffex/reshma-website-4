<script>
  import ButtonTile from '$lib/widgets/ButtonTile.svelte';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';

  import { Wattam } from '$lib/generated-images';
  import { gridBSizesList } from '$lib/layout/layout';
</script>

<ButtonTile areaName="wattam">
  {#snippet content()}
    <GeneratedImage
      imgClass="fill-cover image-color-on-hover"
      image={Wattam}
      alt="Wattam"
      sizes={gridBSizesList(2)}
    />
  {/snippet}

  {#snippet description()}
    <div>
      <p>
        I performed technical assurance and build reliability tasks as a QA
        intern for PlayStation 4 game,{' '}
        <a
          target="_blank"
          href="https://store.steampowered.com/app/702680/Wattam/"
        >
          Wattam</a
        >.
      </p>
      <p>Studio: Funomena</p>
      <p>Publisher: Annapurna Interactive</p>
    </div>
  {/snippet}
</ButtonTile>
