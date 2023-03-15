<script>
	import TilePicture from "$lib/layout/TilePicture.svelte";
  import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import NinjaLogoWebp712 from './ninja-logo.png?w=712&webp&imagetools';
  import NinjaLogoWebp356 from './ninja-logo.png?w=356&webp&imagetools';
  import NinjaLogoWebp175 from './ninja-logo.png?w=175&webp&imagetools';
  import NinjaLogoJpeg356 from './ninja-logo.png?w=356&jpeg&imagetools';
  import NinjaLogoJpeg175 from './ninja-logo.png?w=175&jpeg&imagetools';

</script>

<ButtonTile
    areaName="ninja"
    buttonClass="bg-black highlight:bg-dark-blue">
  <TilePicture
      slot="content"
      imgClass="fill-contain"
      picture={{
        case: 'gridA-3',
        alt: 'Ninja (streamer)',

        webp712: NinjaLogoWebp712,
        webp356: NinjaLogoWebp356,
        webp175: NinjaLogoWebp175,

        jpeg356: NinjaLogoJpeg356,
        jpeg175: NinjaLogoJpeg175,
      }} />
  
  <div slot="description">
    <p>
      Designed numerous YouTube thumbnails for eSports personality,
      Ninja.
    </p>
    <p>Agency: XX Artists</p>
  </div>
</ButtonTile>
