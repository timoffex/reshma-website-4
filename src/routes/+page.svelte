<script>
  import '$lib/global.scss';
  import '$lib/layout/layout-styles.scss';

  import Navbar from '$lib/components/navigation/Navbar.svelte';
	import EmailAddress from '$lib/widgets/EmailAddress.svelte';
	import AnimatedTigerTile from '$lib/components/tiles/aapi-heritage/AnimatedTigerTile.svelte';
	import FlyoutScrim from '$lib/flyout/FlyoutScrim.svelte';
</script>

<div class="main-content">
  <Navbar />

  <div class="grid-container">
    <div class="grid-area-yt-gaming tile"></div>
    <div class="grid-area-salem tile"></div>
    <div class="grid-area-sj-sharks tile"></div>
    <div class="grid-area-ninja tile"></div>
    <AnimatedTigerTile />
    <div class="grid-area-nymphs-tower tile"></div>
    <div class="grid-area-eyes tile"></div>
    <div class="grid-area-reel tile"></div>
    <div class="grid-area-pokemon tile"></div>
    <div class="grid-area-amiibo tile"></div>
    <div class="grid-area-play-magazine tile"></div>
    <div class="grid-area-wattam tile"></div>
  </div>

  <div id="contact" class="lets-collaborate">
    <span class="lets-collaborate__1">let's</span>
    <br />
    <span class="lets-collaborate__2">collaborate</span>
  </div>
  <div class="reshma-email">
    <a target="_blank" href="https://www.canva.com/design/DAFdB-ifsjA/vdLPP5e-seBxAO-OUWKYgA/view?utm_content=DAFdB-ifsjA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton">
      Resum&eacute;</a><br />
    Email me to see my client work
    <br />
    <EmailAddress email="reshmasz.art@gmail.com" />
  </div>
  <div class="developer-credits">
    <span>
      Custom-developed by Timofey Peshin
        (<EmailAddress email="timoffex@gmail.com" />)
    </span>
    <br />
    <span>
      Website mocked in Figma
    </span>
    <br />
    <span>
      Animated in After Effects and Lottie
    </span>
  </div>
</div>
<FlyoutScrim />

<style>
  .lets-collaborate {
    margin-top: 2rem;
    line-height: 0.8;
  }

  .lets-collaborate__1 {
    font-family: "adobe-caslon-pro", serif;
    font-weight: 600;
    font-style: italic;
    letter-spacing: -0.2rem;

    font-size: 3rem;
  }

  .lets-collaborate__2 {
    font-family: "Roboto Mono";
    font-size: 2rem;
  }

  .reshma-email {
    font-family: "Roboto Mono";
    text-align: right;
    margin-top: 1rem;
  }

  .developer-credits {
    text-align: right;
    margin-top: 1rem;
    font-size: 0.5rem;
    color: #1e1e1e;
  }
</style>