<script>
	if (typeof window !== 'undefined') import('@lottiefiles/lottie-player');

	import ButtonTile from '$lib/widgets/ButtonTile.svelte';

	const LOTTIE_PATH = 'yt-gaming-logo.jsonlottie';
</script>

<svelte:head>
	<link rel="preload" href={LOTTIE_PATH} as="fetch" />
</svelte:head>

<ButtonTile areaName="yt-gaming" buttonClass="bg-black">
	<lottie-player slot="content" autoplay loop src={LOTTIE_PATH} class="fill image-color-on-hover" />

	<div slot="description">
		<p>
			Motion Designer for YouTube Gaming responsible for creating video and static design for
			social. <a
				target="_blank"
				href="https://www.figma.com/proto/IswuUG18DXTh663103z0oo/Reshma-Zachariah%27s-work-for-YouTube-Gaming?node-id=1-3&scaling=scale-down&page-id=0%3A1"
			>
				See my work here</a
			>.
		</p>
		<p>Agency: XX Artists</p>
	</div>
</ButtonTile>
