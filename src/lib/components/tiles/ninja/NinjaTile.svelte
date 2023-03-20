<script>
	import TilePicture from '$lib/layout/TilePicture.svelte';
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';

	import NinjaLogoWebp712 from './ninja-logo.png?w=712&webp&imagetools';
	import NinjaLogoWebp356 from './ninja-logo.png?w=356&webp&imagetools';
	import NinjaLogoWebp175 from './ninja-logo.png?w=175&webp&imagetools';
	import NinjaLogoJpeg356 from './ninja-logo.png?w=356&jpeg&imagetools';
	import NinjaLogoJpeg175 from './ninja-logo.png?w=175&jpeg&imagetools';
</script>

<ButtonTile areaName="ninja" buttonClass="bg-black highlight:bg-dark-blue">
	<TilePicture
		slot="content"
		imgClass="fill-contain"
		alt="Ninja (streamer)"
		subgrid="A"
		columns={3}
		mobileWebp={NinjaLogoWebp356}
		mobileJpeg={NinjaLogoJpeg356}
		webpWidthSrcset={`${NinjaLogoWebp712} 712w, ${NinjaLogoWebp356} 356w, ${NinjaLogoWebp175} 175w`}
		jpegWidthSrcset={`${NinjaLogoJpeg356} 356w, ${NinjaLogoJpeg175} 175w`}
		jpegSrc={NinjaLogoJpeg175}
	/>

	<div slot="description">
		<p>
			Designed numerous YouTube thumbnails for eSports personality, Ninja. You can see them
			<a href="/ninja">here</a>.
		</p>
		<p>Agency: XX Artists</p>
	</div>
</ButtonTile>
