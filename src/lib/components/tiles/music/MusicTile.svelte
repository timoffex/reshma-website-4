<script>
	import TilePicture from '$lib/layout/TilePicture.svelte';

	import RecordPlayerWebp540 from './record-player2-1080.webp?w=540&imagetools';
	import RecordPlayerWebp270 from './record-player2-1080.webp?w=270&imagetools';
	import RecordPlayerWebp135 from './record-player2-1080.webp?w=135&imagetools';
	import RecordPlayerJpeg540 from './record-player2-1080.webp?w=540&jpeg&imagetools';
	import RecordPlayerJpeg270 from './record-player2-1080.webp?w=270&jpeg&imagetools';
	import RecordPlayerJpeg135 from './record-player2-1080.webp?w=135&jpeg&imagetools';
</script>

<a href="/music" class="display-block tile grid-area-music">
	<TilePicture
		imgClass="fill-cover"
		alt="Music Clients"
		subgrid="A"
		columns={2}
		mobileWebp={RecordPlayerWebp135}
		mobileJpeg={RecordPlayerJpeg135}
		webpWidthSrcset={`${RecordPlayerWebp540} 540w, ${RecordPlayerWebp270} 270w, ${RecordPlayerWebp135} 135w`}
		jpegWidthSrcset={`${RecordPlayerJpeg540} 540w, ${RecordPlayerJpeg270} 270w, ${RecordPlayerJpeg135} 135w`}
		jpegSrc={RecordPlayerJpeg135}
	/>
</a>
