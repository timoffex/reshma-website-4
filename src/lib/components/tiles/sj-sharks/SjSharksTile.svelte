<script>
	import TilePicture from "$lib/layout/TilePicture.svelte";
  import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import ReshmaWebp720 from './reshma-zachariah-720.webp';
  import ReshmaWebp356 from './reshma-zachariah-356.webp';
  import ReshmaWebp175 from './reshma-zachariah-175.webp';

  import ReshmaJpeg356 from './reshma-zachariah-356.webp?jpeg&imagetools';
  import ReshmaJpeg175 from './reshma-zachariah-175.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="sj-sharks">

  <TilePicture slot="content"
      imgClass="fill-cover image-color-on-hover"
      picture={{
        case: 'gridA-3',
        alt: 'Reshma painting at an SJ Sharks game',

        webp712: ReshmaWebp720,
        webp356: ReshmaWebp356,
        webp175: ReshmaWebp175,

        jpeg356: ReshmaJpeg356,
        jpeg175: ReshmaJpeg175,
      }} />

</ButtonTile>