<script>
	import { gridASizesList } from '$lib/layout/layout';
	import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';
	import { fadeInOut } from '$lib/fade-in-out';

	import { MusicClientsRecord } from '$lib/generated-images';
</script>

<a href="/music" class="display-block tile grid-area-music" use:fadeInOut>
	<GeneratedImage
		imgClass="fill-cover"
		image={{
			alt: 'Music Clients',
			...MusicClientsRecord
		}}
		sizes={gridASizesList(2)}
	/>
</a>
