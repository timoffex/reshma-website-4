<script>
  import Navbar from '../navigation/Navbar.svelte';

  import YtgBento1Mp4 from './ytg-bento-1.mp4';
  import YtgBento1Webm from './ytg-bento-1.webm';
  import YtgBento2Mp4 from './ytg-bento-2.mp4';
  import YtgBento2Webm from './ytg-bento-2.webm';
  import YtgBento3Mp4 from './ytg-bento-3.mp4';
  import YtgBento3Webm from './ytg-bento-3.webm';
</script>

<div class="main-content">
  <Navbar />

  <div class="yt-gaming-grid">
    <div class="yt-gaming-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={YtgBento1Webm} type="video/webm" />
        <source src={YtgBento1Mp4} type="video/mp4" />
      </video>
    </div>
    <div class="yt-gaming-grid__1x1 yt-gaming-grid__text">
      <p>
        In 2020, I was brought on board XX Artists' Design team as a Motion
        Designer. I was key to the YouTube Gaming social team because of my
        previous work in the Gaming industry, and familiarity with social first
        Gaming content. During my time on the team, @YouTubeGaming saw steady
        growth on Twitter, growing from 1.5 million followers to over 2.3 million
        in the span of three years.
      </p>
    </div>

    <div class="yt-gaming-grid__16x9">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={YtgBento2Webm} type="video/webm" />
        <source src={YtgBento2Mp4} type="video/mp4" />
      </video>
    </div>

    <div class="yt-gaming-grid__1x1 yt-gaming-grid__text">
      <p>
        As part of YouTube Gaming's Always On social team, I created crisp
        motion graphics, fun GIFs and illustrations for numerous campaigns
        pitched in-house or for paid social. I helped maintain and devise a
        cohesive brand identity across all assets. Some campaigns I worked on
        include Minecraft Museum, #YouTubeGameOn, Pride, Earth Day, uTure, and
        League of Legends Worlds 2022, among others.
      </p>
    </div>
    <div class="yt-gaming-grid__1x1">
      <video class="fill-cover" autoplay loop muted playsinline tabindex={-1}>
        <source src={YtgBento3Webm} type="video/webm" />
        <source src={YtgBento3Mp4} type="video/mp4" />
      </video>
    </div>
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

    text-wrap: balance;
    text-align: center;

    container-type: inline-size;

    > * {
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
</style>
