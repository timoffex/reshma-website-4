<script>
	import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import AnimatedTigerWebp356 from './animated-tiger-356.webp';
  import AnimatedTigerWebp175 from './animated-tiger-175.webp';
  import AnimatedTigerJpeg175 from './animated-tiger.webp?w=175&jpeg&imagetools';
	import TilePicture from "$lib/layout/TilePicture.svelte";

</script>

<ButtonTile areaName="aapi">

  <TilePicture slot="content"
      imgClass="fill-cover image-color-on-hover"
      picture={{
        case: 'gridA-3',
        alt: 'Tiger animation for AAPI Heritage Month',
        webp356: AnimatedTigerWebp356,
        webp175: AnimatedTigerWebp175,
        jpeg356: AnimatedTigerWebp356,
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
