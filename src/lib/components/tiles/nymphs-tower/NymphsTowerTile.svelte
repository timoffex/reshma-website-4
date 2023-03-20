<script>
	import TilePicture from '$lib/layout/TilePicture.svelte';
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';

	import NymphsTowerWebp256 from './nymphtower-vertical-256.webp';
	import NymphsTowerWebp174 from './nymphtower-vertical-174.webp';
	import NymphsTowerWebp87 from './nymphtower-vertical-87.webp';

	import NymphsTowerJpeg174 from './nymphtower-vertical-174.webp?jpeg&imagetools';
	import NymphsTowerJpeg87 from './nymphtower-vertical-87.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="nymphs-tower">
	<TilePicture
		slot="content"
		imgClass="fill-cover image-color-on-hover"
		loading="lazy"
		alt="Nymph's Tower game recording"
		subgrid="B"
		columns={1}
		mobileWebp={NymphsTowerWebp174}
		mobileJpeg={NymphsTowerJpeg174}
		webpWidthSrcset={`${NymphsTowerWebp256} 256w, ${NymphsTowerWebp174} 174w, ${NymphsTowerWebp87} 87w`}
		jpegWidthSrcset={`${NymphsTowerJpeg174} 174w, ${NymphsTowerJpeg87} 87w`}
		jpegSrc={NymphsTowerJpeg87}
	/>

	<div slot="description">
		<p>
			I'm a game developer and artist, and love interactive media. Play some <a
				target="_blank"
				href="https://reshmush.itch.io/">here</a
			>.
		</p>
	</div>
</ButtonTile>
