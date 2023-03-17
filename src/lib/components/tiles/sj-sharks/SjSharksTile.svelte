<script>
	import TilePicture from '$lib/layout/TilePicture.svelte';
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';

	import ReshmaWebp720 from './reshma-zachariah-720.webp';
	import ReshmaWebp356 from './reshma-zachariah-356.webp';
	import ReshmaWebp175 from './reshma-zachariah-175.webp';

	import ReshmaJpeg356 from './reshma-zachariah-356.webp?jpeg&imagetools';
	import ReshmaJpeg175 from './reshma-zachariah-175.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="sj-sharks">
	<TilePicture
		slot="content"
		imgClass="fill-cover image-color-on-hover"
		alt="Reshma painting at an SJ Sharks game"
		subgrid="A"
		columns={3}
		webpWidthSrcset={`${ReshmaWebp720} 720w, ${ReshmaWebp356} 356w, ${ReshmaWebp175} 175w`}
		jpegWidthSrcset={`${ReshmaJpeg356} 356w, ${ReshmaJpeg175} 175w`}
	/>
</ButtonTile>
