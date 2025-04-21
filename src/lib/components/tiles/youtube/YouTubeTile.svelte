<script>
  import ButtonTile from '$lib/widgets/ButtonTile.svelte';
</script>

<ButtonTile areaName="youtube">
  {#snippet content()}
    <div class="fill padding-2 bg-black">
      <enhanced:img
        alt="YouTube Core"
        src="./youtube-logo.svg"
        class="fill-contain image-color-on-hover-2"
      />
    </div>
  {/snippet}

  {#snippet description()}
    <p>
      In 2020, I was brought on board XX Artists' Design team as a Motion
      Designer. I worked as part of a team of designers, illustrators,
      copywriters and account managers to deliver top of the line content for
      social in response to the ever-evolving zeitgeist of online culture. XX
      was YouTube's agency of record until it was acquired by media.monks in
      2023.
    </p>
  {/snippet}
</ButtonTile>

<style lang="scss">
  @use '$lib/layout/layout';

  .padding-2 {
    box-sizing: border-box;
    padding: 2 * layout.$spacing;
  }
</style>
