<script>
	import { GRIDA_3_SIZES } from "$lib/layout/image-sizing";
	import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import AnimatedTigerWebp356 from './animated-tiger-356.webp';
  import AnimatedTigerWebp175 from './animated-tiger-175.webp';
  import AnimatedTigerJpegSrcset from './animated-tiger.webp?w=356;175&jpeg&srcset&imagetools';
  import AnimatedTigerJpeg from './animated-tiger.webp?w=175&jpeg&imagetools';

</script>

<ButtonTile areaName="aapi">

  <picture slot="content">
    <source srcset="{AnimatedTigerWebp356} 356w, {AnimatedTigerWebp175} 175w" type="image/webp">
    <source srcset={AnimatedTigerJpegSrcset} type="image/jpeg">

    <img
        class="fill-cover image-color-on-hover"
        sizes={GRIDA_3_SIZES}
        alt="Tiger animation for AAPI Heritage Month"
        src={AnimatedTigerJpeg} />
  </picture>

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
