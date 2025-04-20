<script>
  import { fadeInOut } from '$lib/fade-in-out';

  import VinylRecordPlayerWebp from './vinyl-record-player.webp';
  import VinylRecordPlayerGif from './vinyl-record-player.gif';
</script>

<a
  href="/music"
  class="display-block tile grid-area-music"
  use:fadeInOut
>
  <picture>
    <source type="image/webp" srcset={VinylRecordPlayerWebp} />
    <img
      src={VinylRecordPlayerGif}
      alt=""
      class="image-color-on-hover fill-cover"
    />
  </picture>
  <div class="music-clients-text">
    Music Clients
  </div>
</a>

<style lang="scss">
  .music-clients-text {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;

    // Allow mouse hover to pass through to image.
    pointer-events: none;

    text-align: center;
    align-content: center;

    color: white;
    font-size: 2rem;
  }
</style>
