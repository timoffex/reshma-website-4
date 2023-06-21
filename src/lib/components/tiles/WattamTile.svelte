<script>
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';
	import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';

	import { Wattam } from '$lib/generated-images';
	import { gridBSizesList } from '$lib/layout/layout';
</script>

<ButtonTile areaName="wattam">
	<GeneratedImage
		slot="content"
		imgClass="fill-cover image-color-on-hover"
		image={{
			alt: 'Wattam',
			...Wattam
		}}
		sizes={gridBSizesList(2)}
	/>

	<div slot="description">
		<p>
			I performed technical assurance and build reliability tasks as a QA intern for PlayStation 4
			game,{' '}
			<a target="_blank" href="https://www.funomena.com/wattamgame"> Wattam</a>.
		</p>
		<p>Studio: Funomena</p>
		<p>Publisher: Annapurna Interactive</p>
	</div>
</ButtonTile>
