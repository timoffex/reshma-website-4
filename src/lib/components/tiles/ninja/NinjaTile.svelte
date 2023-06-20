<script>
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';
	import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';

	import { NinjaLogo } from '$lib/generated-images';
	import { gridASizesList } from '$lib/layout/layout';
</script>

<ButtonTile areaName="ninja" buttonClass="bg-black highlight:bg-dark-blue">
	<GeneratedImage
		slot="content"
		imgClass="fill-contain"
		image={{
			alt: 'Ninja (streamer)',
			...NinjaLogo
		}}
		sizes={gridASizesList(3)}
	/>

	<div slot="description">
		<p>
			Designed numerous YouTube thumbnails for eSports personality, Ninja. You can see them
			<a href="/ninja">here</a>.
		</p>
		<p>Agency: XX Artists</p>
	</div>
</ButtonTile>
