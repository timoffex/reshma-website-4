<script>
	import TilePicture from "$lib/layout/TilePicture.svelte";
  import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import NymphsTowerWebp256 from './nymphtower-vertical-256.webp';
  import NymphsTowerWebp174 from './nymphtower-vertical-174.webp';
  import NymphsTowerWebp87 from './nymphtower-vertical-87.webp';

  import NymphsTowerJpeg174 from './nymphtower-vertical-174.webp?jpeg&imagetools';
  import NymphsTowerJpeg87 from './nymphtower-vertical-87.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="nymphs-tower">
  <TilePicture
      slot="content"
      imgClass="fill-cover image-color-on-hover"
      loading="lazy"
      picture={{
        case: 'gridB-1',
        alt: "Nymph's Tower game recording",

        webp348: NymphsTowerWebp256,
        webp174: NymphsTowerWebp174,
        webp87: NymphsTowerWebp87,

        jpeg174: NymphsTowerJpeg174,
        jpeg87: NymphsTowerJpeg87,
      }} />

  <div slot="description">
    <p>
      I'm a game developer and artist, and love interactive media.
      Play some <a target="_blank" href="https://reshmush.itch.io/">here</a>.
    </p>
  </div>
</ButtonTile>