<script lang="ts">
  import Navbar from '../navigation/Navbar.svelte';

  import SalemAnimated320 from './salem-animated-320.gif';
  import SalemSpritesheet322 from './salem-spritesheet-322.png';
</script>

<div class="main-content">
  <Navbar />

  <iframe
    class="salem-ps5-youtube-embed"
    src="https://www.youtube.com/embed/WRVonH0TTS8?si=KaPMz0EYsGnKOK9Z"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
  ></iframe>

  <p class="text-align-center">
    I created the fun and cute pixel art graphic effects for salem ilese's music
    video, PS5, in 2022. This was a super fun project and I had a lot of
    creative freedom to illustrate the bright, retro and playful MapleStory
    inspired GFX in this video. The assets are optimized for the potential to
    create a 2D platformer game in the future.
  </p>
  <p class="text-align-center">
    I worked with director Christina Xing and producer Laura Burhenn to create
    every instance of 2D animation in the final music video, with the approval
    of salem and the record label, Universal Music Group.
  </p>

  <img
    alt="spritesheet of an animation of salem ilese"
    src={SalemSpritesheet322}
    class="full-width-pixel-image"
  />

  <p class="margin-auto text-small">
    Production Company: Our Secret Handshake<br />
    Director: Christina Xing<br />
    Producer: Laura Burhenn<br />
    Cinematographer: Justin McWilliams<br />
    1st AC: Walter Watkins<br />
    2nd AC/DIT: John Landry<br />
    Gaffer: Hiram Borges<br />
    Key Grip: Michael Roseman<br />
    First Lighting Tech: Joy Wang<br />
    Second Lighting Tech: Malik Dowdy<br />
    BBG: Taylor Reick<br />
    Grip: Andrew Soltay<br />
    1st AD: Jasmine Osean Thomas<br />
    Production Designer: Ava Jones<br />
    Set Decorators: Ethan Kankula & Daniel Richmond<br />
    Editor: Joan Pabon<br />
    Editorial Team: Digital Sword, Jack Melanson, Estefania Parra<br />
    Additional Editing: Neon Pig, Alex Familian, Anjoum Agrama<br />
    GFX: Reshma Zachariah<br />
    VFX: Ethan Madison<br />
    Color: Cameron Marygold<br />
    Line Producer: Erikx DiSantis<br />
    Production Coordinator: Brianna Liebling<br />
    PAs: Sydney Shelton, Aubrey Fowler, Rolando Rodas<br />
    BTS Photographer: Morgan Foitle<br />
    Director Rep: Jen Herrara for Las Bandas
  </p>

  <img
    alt="animated salem ilese sprite"
    src={SalemAnimated320}
    class="full-width-pixel-image"
  />
</div>

<style lang="scss">
  .salem-ps5-youtube-embed {
    width: 100%;
    aspect-ratio: 560 / 315;
  }

  .text-align-center {
    text-align: center;
  }

  .margin-auto {
    margin: 0 auto;
  }

  .full-width-pixel-image {
    display: block;
    width: 100%;
    image-rendering: pixelated;
  }
</style>
