<script>
	import TilePicture from "$lib/layout/TilePicture.svelte";
  import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import WattamWebp712 from './wattam.png?webp&w=712&imagetools';
  import WattamWebp356 from './wattam.png?webp&w=356&imagetools';
  import WattamWebp175 from './wattam.png?webp&w=175&imagetools';

  import WattamJpeg356 from './wattam.png?jpeg&w=356&imagetools';
  import WattamJpeg175 from './wattam.png?jpeg&w=175&imagetools';
</script>

<ButtonTile areaName="wattam">
  <TilePicture
      slot="content"
      imgClass="fill-cover image-color-on-hover"
      loading="lazy"
      picture={{
        case: 'gridB-2',
        alt: 'Wattam',

        webp712: WattamWebp712,
        webp356: WattamWebp356,
        webp175: WattamWebp175,

        jpeg356: WattamJpeg356,
        jpeg175: WattamJpeg175,
      }}/>

  <div slot="description">
    <p>
      I performed technical assurance and build reliability tasks as a QA
      intern for PlayStation 4 game,{' '}
      <a target="_blank" href="https://www.funomena.com/wattamgame">
        Wattam</a>.
    </p>
    <p>Studio: Funomena</p>
    <p>Publisher: Annapurna Interactive</p>
  </div>
</ButtonTile>