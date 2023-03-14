<script>
	import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import AnimatedTigerWebp from './animated-tiger.webp';

</script>

<ButtonTile areaName="aapi">

  <img
      slot="content"
      class="fill-cover image-color-on-hover"
      alt="Tiger animation for AAPI Heritage Month"
      src={AnimatedTigerWebp} />

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
