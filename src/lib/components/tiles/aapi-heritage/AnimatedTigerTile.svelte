<script>
	import TilePicture from '$lib/layout/TilePicture.svelte';
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';

	import AnimatedTigerWebp600 from './animated-tiger-600.webp';
	import AnimatedTigerWebp356 from './animated-tiger-356.webp';
	import AnimatedTigerWebp175 from './animated-tiger-175.webp';
	import AnimatedTigerJpeg356 from './animated-tiger-356.webp?jpeg&imagetools';
	import AnimatedTigerJpeg175 from './animated-tiger-175.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="aapi">
	<TilePicture
		slot="content"
		imgClass="fill-cover image-color-on-hover"
		alt="Tiger animation for AAPI Heritage Month"
		subgrid="A"
		columns={3}
		mobileWebp={AnimatedTigerWebp356}
		mobileJpeg={AnimatedTigerJpeg356}
		webpWidthSrcset={`${AnimatedTigerWebp600} 600w, ${AnimatedTigerWebp356} 356w, ${AnimatedTigerWebp175} 175w`}
		jpegWidthSrcset={`${AnimatedTigerJpeg356} 356w, ${AnimatedTigerJpeg175} 175w`}
		jpegSrc={AnimatedTigerJpeg175}
	/>

	<div slot="description">
		<p>Motion Graphic Design and Illustration for AAPI heritage month.</p>
		<p>Agency: <a target="_blank" href="https://www.instagram.com/p/CeCSTQABzkw/">XX Artists</a></p>
	</div>
</ButtonTile>
