<script>
  import Navbar from '../navigation/Navbar.svelte';

  import YtgLogo from './ytg-logo.svg';

  import YtgBento1Mp4 from './ytg-bento-1.mp4';
  import YtgBento1Webm from './ytg-bento-1.webm';
  import YtgBento2Mp4 from './ytg-bento-2.mp4';
  import YtgBento2Webm from './ytg-bento-2.webm';
  import YtgBento3Mp4 from './ytg-bento-3.mp4';
  import YtgBento3Webm from './ytg-bento-3.webm';
</script>

<div class="main-content">
  <Navbar>
    {#snippet logo()}
      <img src={YtgLogo} alt="" class="fill-contain-left" />
    {/snippet}
  </Navbar>

  <div class="yt-gaming-grid">
    <div class="yt-gaming-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={YtgBento1Webm} type="video/webm" />
        <source src={YtgBento1Mp4} type="video/mp4" />
      </video>
    </div>
    <div class="yt-gaming-grid__1x1 yt-gaming-grid__text ytg-gradient-1">
      <p>
        In 2020, I was brought on board XX Artists' Design team as a Motion
        Designer for my experience in the gaming industry.
      </p>
      <p>
        During my time on the team, @YouTubeGaming saw steady growth on Twitter,
        growing from 1.5 million followers to over 2.3 million in the span of
        three years.
      </p>
    </div>

    <div class="yt-gaming-grid__16x9">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={YtgBento2Webm} type="video/webm" />
        <source src={YtgBento2Mp4} type="video/mp4" />
      </video>
    </div>

    <div class="yt-gaming-grid__1x1 yt-gaming-grid__text ytg-gradient-2">
      <p>
        As part of YouTube Gaming's Always On social team, I created crisp
        motion graphics, fun GIFs and illustrations for numerous campaigns
        pitched in-house and for paid social.
      </p>
    </div>
    <div class="yt-gaming-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={YtgBento3Webm} type="video/webm" />
        <source src={YtgBento3Mp4} type="video/mp4" />
      </video>
    </div>
  </div>

  <div class="tile bottom-tile">
    <p class="text-align-center">
      I helped maintain and devise a cohesive brand identity across all assets.
      Some campaigns I worked on include #MinecraftMuseum, #YouTubeGameOn,
      Pride, Earth Day, uTure, and League of Legends Worlds 2022, among others.
    </p>
    <p class="text-align-center">
      <a
        href="https://www.figma.com/proto/IswuUG18DXTh663103z0oo/Reshma-Zachariah's-work-for-YouTube-Gaming?node-id=1-3&p=f&t=O19d8BdL2pUzvDD7-0&scaling=scale-down&content-scaling=fixed&page-id=0%3A1"
        class="bottom-tile__link">See More on Figma.</a
      >
    </p>
    <p class="text-align-right text-small">
      Agency: XX Artists<br />
      Creative Director: Mackenna Millet, Erin Taj<br />
      YouTube Product Marketing Manager: Kate Bryant<br />
    </p>
  </div>
</div>

<style lang="scss">
  @use '$lib/layout/layout';

  .yt-gaming-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: layout.$spacing;
  }

  .yt-gaming-grid__text {
    display: flex;
    flex-direction: column;
    justify-content: center;

    text-align: center;

    container-type: inline-size;

    border-radius: layout.$spacing;

    > * {
      padding: 0 15%;
      font-size: min(1em, 5cqw);
    }
  }

  .yt-gaming-grid__1x1 {
    overflow: hidden;
    grid-row: span 1;
    grid-column: span 1;
    aspect-ratio: 1;
  }

  .yt-gaming-grid__16x9 {
    overflow: hidden;
    grid-row: span 1;
    grid-column: span 2;
    aspect-ratio: 16 / 9;
  }

  .bottom-tile {
    padding: 0 7%;

    background-color: #212121;
    color: white;
  }

  .bottom-tile__link:link {
    color: cyan;
  }

  .bottom-tile__link:visited {
    color: magenta;
  }

  .ytg-gradient-1 {
    color: white;
    background: radial-gradient(
      circle,
      rgba(222, 108, 224, 1) 0%,
      rgba(116, 163, 237, 1) 100%
    );
  }
  .ytg-gradient-2 {
    background: radial-gradient(
      circle,
      rgba(227, 227, 227, 1) 0%,
      rgba(148, 187, 233, 1) 100%
    );
  }
</style>
