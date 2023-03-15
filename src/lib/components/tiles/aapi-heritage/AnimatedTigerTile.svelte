<script>
	import TilePicture from "$lib/layout/TilePicture.svelte";
	import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import AnimatedTigerWebp600 from './animated-tiger-600.webp';
  import AnimatedTigerWebp356 from './animated-tiger-356.webp';
  import AnimatedTigerWebp175 from './animated-tiger-175.webp';
  import AnimatedTigerJpeg356 from './animated-tiger-356.webp?jpeg&imagetools';
  import AnimatedTigerJpeg175 from './animated-tiger-175.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="aapi">

  <TilePicture slot="content"
      imgClass="fill-cover image-color-on-hover"
      picture={{
        case: 'gridA-3',
        alt: 'Tiger animation for AAPI Heritage Month',

        webp712: AnimatedTigerWebp600,
        webp356: AnimatedTigerWebp356,
        webp175: AnimatedTigerWebp175,

        jpeg356: AnimatedTigerJpeg356,
        jpeg175: AnimatedTigerJpeg175,
      }} />

  <div slot="description">
    <p>
      Motion Graphic Design and Illustration for AAPI heritage month.
    </p>
    <p>
      Agency: XX Artists{' '}
      <a href="https://www.thedrum.com/news/2022/07/01/mediamonks-merges-with-la-talent-agency-xx-artists"
         target="_blank">
        (merged with Media.Monks in 2022)
      </a>
    </p>  
  </div>

</ButtonTile>
