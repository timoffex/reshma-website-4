<script>
  import Navbar from '$lib/components/navigation/Navbar.svelte';
  import { EtafLogoColor } from '$lib/generated-images';
  import {
    EtafByTheNumbers1,
    EtafByTheNumbers2,
    EtafLendAHand3,
    EtafLendAHand4,
    EtafSunnyHostin,
    EtafTakeAction
  } from '$lib/generated-videos';
  import { gridASizesList, halfMainContentSizesList } from '$lib/layout/layout';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';
  import VideoAnimation from '$lib/widgets/VideoAnimation.svelte';
</script>

<div class="main-content">
  <Navbar>
    {#snippet logo()}
      <GeneratedImage
        imgClass="fill-contain-left"
        image={EtafLogoColor}
        alt="Elizabeth Taylor AIDS Foundation"
        sizes={halfMainContentSizesList}
      />
    {/snippet}
  </Navbar>

  <div>
    <p class="text-align-center">
      Elizabeth Taylor established The Elizabeth Taylor AIDS Foundation (ETAF)
      in 1991 to raise funds and awareness to fight the spread of HIV/AIDS. The
      Elizabeth Taylor AIDS Foundation (ETAF) provides direct care and support
      to people with HIV and AIDS. Inspired by Elizabeth's personal passion for
      the cause, ETAF also engages in advocacy and education programs to advance
      the goal of an AIDS-free world.
    </p>
    <p class="text-align-center">
      Follow them on Instagram - Elizabeth Taylor AIDS FDN
      (@elizabethtayloraidsfoundation)
    </p>
  </div>

  <div class="etaf-grid">
    <!-- Row 1 -->
    <div class="etaf-grid__1x1">
      <VideoAnimation video={EtafSunnyHostin} class="fill-cover" />
    </div>
    <div class="etaf-grid__1x1">
      <VideoAnimation video={EtafByTheNumbers1} class="fill-cover" />
    </div>
    <div class="etaf-grid__1x1">
      <VideoAnimation video={EtafByTheNumbers2} class="fill-cover" />
    </div>

    <!-- Row 2 -->
    <div class="etaf-grid__1x1">
      <VideoAnimation video={EtafLendAHand3} class="fill-cover" />
    </div>
    <div class="etaf-grid__1x1">
      <VideoAnimation video={EtafLendAHand4} class="fill-cover" />
    </div>
    <div class="etaf-grid__1x1">
      <VideoAnimation video={EtafTakeAction} class="fill-cover" />
    </div>

    <!-- Row 3 -->
    <div class="etaf-grid__1x1">
      <enhanced:img
        class="fill-cover"
        src="./ETAF_30Years_v3.png?w=540;270;135"
        alt=""
        sizes={gridASizesList(2)}
      />
    </div>
    <div class="etaf-grid__1x1">
      <enhanced:img
        class="fill-cover"
        src="./ETAF_National Women and Girls HIV_AIDS Awareness Day_IG_v1_RZv1.jpg?w=540;270;135"
        alt=""
        sizes={gridASizesList(2)}
      />
    </div>
    <div class="etaf-grid__1x1">
      <enhanced:img
        class="fill-cover"
        src="./ETAF_OneYear_RZ_Slide2_12138.png?w=540;270;135"
        alt=""
        sizes={gridASizesList(2)}
      />
    </div>
  </div>
</div>

<style lang="scss">
  @use '$lib/layout/layout';

  .etaf-grid {
    display: grid;

    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: layout.$spacing;
  }

  .etaf-grid__1x1 {
    grid-row: span 1;
    grid-column: span 1;
    aspect-ratio: 1;
  }
</style>
