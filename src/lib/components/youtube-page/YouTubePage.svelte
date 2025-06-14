<script>
  import Navbar from '$lib/components/navigation/Navbar.svelte';
  import { EtafLogoColor } from '$lib/generated-images';
  import { gridASizesList, halfMainContentSizesList } from '$lib/layout/layout';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';

  import ICYMI1 from './ICYMI_saltwaterstitches_9x16_RZ.mp4';
  import ICYMI2 from './ICYMI_frogphone_9x16_RZ_v2.mp4';
  import ICYMI3 from './ICYMI_Mittens_9x16_v5.mp4';
  import ICYMISticker from './Sticker_ICYMI.webm';
  import CreatorMilestone from './YT_CreatorMilestone_IG_RZ.mp4';
  import YTGPride from './YTG_Pride_CommCard_Jaiden Animations_4x5_db_np_v3.webm';
  import Pride from './4- Tarek Ali_YT_Pride_Comments Are Everything_v2_OA.mp4';
  import Iconic from './YTC_Iconic_Minecraft_Frame2_20227_RZ_FQ_v2.mp4';
  import Pride2 from './YTC_TWIT_6-6_Frame1Intro_RZ.mp4';
  import MarioOrSonic from './YTCore_MarioOrSonic_RZ.mp4';
  import OverheardOnYT from './Overheard on YT_1x1_Compilation_RZ.mp4';
  import Slideshow from './YTC_6-7_Slideshow_RZ.mp4';
  import Calendar from './YTCore_JuneCal_1x1_02_RZ.mp4';
  import Slideshow2 from './YTC_Edu Assets Week of 6-14_Slideshow_RZ.mp4';
  import YTGGTC from './YTGaming_GuessThatCreator_Frame1_9x16_RZ_17051 (1).mp4';
  import YTMShortsList from './YTM_ShortsList_RZ_9x16_v2.mp4';
</script>

<div class="main-content">
  <Navbar>
    {#snippet logo()}
      <enhanced:img
        alt="YouTube Core"
        src="$lib/components/yt-logo-gray.svg"
        class="fill-contain"
      />
    {/snippet}
  </Navbar>

  <div>
    <p class="text-align-center">
      In 2020, I was brought on board XX Artists' Design team as a Motion
      Designer. I worked as part of a team of designers, illustrators,
      copywriters and account managers to deliver top of the line content for
      social in response to the ever-evolving zeitgeist of online culture. 
      Our team was awarded <a
      href="https://winners.webbyawards.com/2022/social/features/best-overall-social-presence-brand/220973/best-overall-social-presence-youtube-social"
      class="bottom-tile__link">Best Overall Social Presence</a
      > 
      by the webby awards 
      in 2022 as YouTube's agency of record. 
    </p>
    <p class="text-align-center">
      <a
        href="/youtube-gaming"
        class="bottom-tile__link">See my work for YouTube Gaming here.</a
      >
    </p>
    <p class="text-align-right text-small">
      Agency: XX Artists<br />
      Creative Director: Mackenna Millet, David Badounts, Erin Taj<br />
      YouTube Product Marketing Manager: Kate Bryant<br />
    </p>
  </div>

  <div class="yt-grid">
    {#snippet autoVideo(src)}
      <video
        class="fill-contain display-block"
        autoplay
        loop
        muted
        playsinline
        tabindex={-1}
      >
        <source {src} />
      </video>
    {/snippet}

    <!-- Row 1 -->
    <div class="yt-grid__9x16">{@render autoVideo(ICYMI1)}</div>
    <div class="yt-grid__9x16">{@render autoVideo(ICYMI2)}</div>
    <div class="yt-grid__9x16">{@render autoVideo(ICYMI3)}</div>

    <!-- Row 2 -->
    <div class="yt-grid__9x16">{@render autoVideo(Iconic)}</div>
    <div class="yt-grid__9x16">{@render autoVideo(CreatorMilestone)}</div>
    <div class="yt-grid__9x16">{@render autoVideo(MarioOrSonic)}</div>

     <!-- Row 3 -->
    <div class="yt-grid__1x1">{@render autoVideo(OverheardOnYT)}</div>
    <div class="yt-grid__1x1">{@render autoVideo(YTGPride)}</div>
    <div class="yt-grid__1x1">{@render autoVideo(Slideshow)}</div>

     <!-- Row 4 -->
     <div class="yt-grid__9x16">{@render autoVideo(Pride2)}</div>
     <div class="yt-grid__9x16">{@render autoVideo(YTGGTC)}</div>
     <div class="yt-grid__9x16">{@render autoVideo(YTMShortsList)}</div>

      <!-- Row 5 -->
      <div class="yt-grid__1x1">{@render autoVideo(Calendar)}</div>
      <div class="yt-grid__1x1">{@render autoVideo(ICYMISticker)}</div>
      <div class="yt-grid__1x1">{@render autoVideo(Slideshow2)}</div>

  </div>
</div>

<style lang="scss">
  @use '$lib/layout/layout';

  .yt-grid {
    display: grid;

    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: layout.$spacing;
  }

  .yt-grid__1x1 {
    grid-row: span 1;
    grid-column: span 1;
    aspect-ratio: 1;
  }

  .yt-grid__9x16 {
    grid-row: span 1;
    grid-column: span 1;
    aspect-ratio: 9/16;
  }
</style>
