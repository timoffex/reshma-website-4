<script lang="ts">
  import Navbar from '$lib/components/navigation/Navbar.svelte';
  import { MarinaAbramovic } from '$lib/generated-images';
  import { mainContentSizeExpr, spacingPx } from '$lib/layout/layout';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';

  import WeTransferLogo from './wetransfer-logo.svg';

  import EarthdaySlide1 from './earthday-slide1.mp4';
  import EarthdaySlide2 from './earthday-slide2.mp4';
  import EarthdaySlide3 from './earthday-slide3.mp4';

  import GirlInRed1 from './girl-in-red1.mp4';
  import GirlInRed2 from './girl-in-red2.mp4';

  import MarinaAbramovicIntro from './marina-abramovic-intro.mp4';

  import HumblebragIntro from './humblebrag-intro.mp4';
  import Humblebrag2 from './humblebrag-2.mp4';

  import CollectBoards from './collect-boards.mp4';

  const gridColSizesList = `calc((${mainContentSizeExpr} - ${spacingPx}px) / 2)`;
</script>

<!-- svelte-ignore a11y_media_has_caption -->

<div class="main-content">
  <Navbar>
    {#snippet logo()}
      <img src={WeTransferLogo} alt="" class="fill-contain-left" />
    {/snippet}
  </Navbar>

  <div class="wetransfer-gallery-grid">
    <!-- Earth Day -->
    <div class="wetransfer-gallery-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={EarthdaySlide1} />
      </video>
    </div>

    <div class="wetransfer-gallery-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={EarthdaySlide2} />
      </video>
    </div>

    <div class="wetransfer-gallery-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={EarthdaySlide3} />
      </video>
    </div>

    <div class="wetransfer-gallery-grid__text">
      <p>
        Suite of assets for social made for Earth Day, or World Environment Day.
        Client used these on Instagram and Linkedin.<br /><br />
        AD: Nate Makuch
      </p>
    </div>

    <!-- Girl In Red -->
    <div class="wetransfer-gallery-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={GirlInRed2} />
      </video>
    </div>

    <div class="wetransfer-gallery-grid__9x16">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={GirlInRed1} />
      </video>
    </div>

    <div class="wetransfer-gallery-grid__text next-to-9x16">
      <p>
        Assets made for WEPRESENT's collaboration with Tillie Walden and girl in
        red. Used on Instagram and Twitter.<br /><br />
        AD: Nate Makuch
      </p>
    </div>

    <!-- Marina Abramovic -->
    <div class="wetransfer-gallery-grid__9x16">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={MarinaAbramovicIntro} />
      </video>
    </div>

    <div class="wetransfer-gallery-grid__1x1">
      <GeneratedImage
        image={{
          alt: 'Marina Abramovic quote',
          ...MarinaAbramovic
        }}
        sizes={gridColSizesList}
        imgClass="fill-cover"
      />
    </div>

    <div class="wetransfer-gallery-grid__text next-to-9x16">
      <p>
        Suite of assets made for WEPRESENT's guest curator series with Marina
        Abramović. These assets were used on WEPRESENT's Instagram Story and in
        Feed. Read more about the 5 artists she selected <a
          target="_blank"
          href="https://wepresent.wetransfer.com/series/guest-curator-marina-abramovic"
          >here</a
        >.
        <br /><br />
        AD: Nate Makuch
      </p>
    </div>

    <!-- Humblebrag -->
    <div class="wetransfer-gallery-grid__1x1--9x16">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={HumblebragIntro} />
      </video>
    </div>

    <div class="wetransfer-gallery-grid__1x1--9x16">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={Humblebrag2} />
      </video>
    </div>

    <!-- Collect Boards -->
    <div class="wetransfer-gallery-grid__2x2">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={CollectBoards} />
      </video>
    </div>
  </div>
</div>

<style lang="scss">
  @use '$lib/layout/layout';

  .wetransfer-gallery-grid {
    display: grid;

    grid-template-columns: 1fr 1fr;

    grid-gap: layout.$spacing;
  }

  .wetransfer-gallery-grid__1x1,
  .wetransfer-gallery-grid__1x1--9x16,
  .wetransfer-gallery-grid__9x16,
  .wetransfer-gallery-grid__2x2 {
    display: block;
    border: 1px solid black;
    border-radius: layout.$spacing;
    min-height: 0;
    overflow: hidden;
  }

  .wetransfer-gallery-grid__1x1 {
    grid-row: span 1;
    grid-column: span 1;
    aspect-ratio: 1;
  }

  .wetransfer-gallery-grid__1x1--9x16 {
    grid-row: span 1;
    grid-column: span 1;
    aspect-ratio: 9 / 16;
  }

  .wetransfer-gallery-grid__9x16 {
    grid-row: span 2;
    grid-column: span 1;
    aspect-ratio: 9 / 16;
  }

  .wetransfer-gallery-grid__2x2 {
    grid-row: span 1;
    grid-column: span 2;
    aspect-ratio: 1;
  }

  .wetransfer-gallery-grid__text {
    display: flex;
    flex-direction: column;
    justify-content: center;

    text-align: center;

    container-type: inline-size;

    > * {
      padding: 0 15%;
      font-size: min(1em, 5cqw);
    }
  }

  // An imperfect way to get an item below a 1x1 square and
  // next to a 9x16 rectangle to take up the remaining space.
  .next-to-9x16 {
    aspect-ratio: 9 / 7;
  }
</style>
