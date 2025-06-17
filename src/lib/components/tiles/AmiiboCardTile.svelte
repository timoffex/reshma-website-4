<script>
  import ButtonTile from '$lib/widgets/ButtonTile.svelte';
  import FlipCard from '$lib/widgets/FlipCard.svelte';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';

  import { AmiiboBack, AmiiboFront } from '$lib/generated-images';
  import { gridBSizesList } from '$lib/layout/layout';
</script>

<ButtonTile card areaName="amiibo">
  {#snippet content()}
    <FlipCard>
      {#snippet front()}
        <GeneratedImage
          imgClass="fill rounded-border image-color-on-hover"
          image={AmiiboBack}
          alt="Backside of an Animal Crossing Amiibo card"
          sizes={gridBSizesList(1)}
        />
      {/snippet}

      {#snippet back()}
        <GeneratedImage
          imgClass="fill rounded-border"
          image={AmiiboFront}
          alt="Backside of an Animal Crossing Amiibo card"
          sizes={gridBSizesList(1)}
        />
      {/snippet}
    </FlipCard>
  {/snippet}

  {#snippet description()}
    <div>
      <p>
        I illustrated <a
          target="_blank"
          href="https://www.essentiallysports.com/esports-news-animal-crossing-new-horizons-on-the-third-anniversary-of-the-game-pets-of-streamers-including-sykkuno-valkyrae-and-more-joins-the-villagers/"
          >custom Amiibo cards</a
        > for a social activation on YouTube Gaming's twitter. This is QTCinderella's
        cat, Coots.
      </p>
    </div>
  {/snippet}
</ButtonTile>
