<script>
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';
	import FlipCard from '$lib/widgets/FlipCard.svelte';
	import TilePicture from '$lib/layout/TilePicture.svelte';

	import AmiiboBackWebp348 from './amiibo-back-348.webp';
	import AmiiboBackWebp174 from './amiibo-back-348.webp?w=174&imagetools';
	import AmiiboBackWebp87 from './amiibo-back-348.webp?w=87&imagetools';

	import AmiiboBackJpeg174 from './amiibo-back-348.webp?w=174&jpeg&imagetools';
	import AmiiboBackJpeg87 from './amiibo-back-348.webp?w=87&jpeg&imagetools';

	import AmiiboFrontWebp348 from './amiibo-front-348.webp';
	import AmiiboFrontWebp174 from './amiibo-front-348.webp?w=174&imagetools';
	import AmiiboFrontWebp87 from './amiibo-front-348.webp?w=87&imagetools';

	import AmiiboFrontJpeg174 from './amiibo-front-348.webp?w=174&jpeg&imagetools';
	import AmiiboFrontJpeg87 from './amiibo-front-348.webp?w=87&jpeg&imagetools';
</script>

<ButtonTile card areaName="amiibo">
	<FlipCard slot="content">
		<TilePicture
			slot="front"
			imgClass="fill rounded-border"
			alt="Backside of an Animal Crossing Amiibo card"
			subgrid="B"
			columns={1}
			webpWidthSrcset={`${AmiiboBackWebp348} 348w, ${AmiiboBackWebp174} 174w, ${AmiiboBackWebp87} 87w`}
			jpegWidthSrcset={`${AmiiboBackJpeg174} 174w, ${AmiiboBackJpeg87} 87w`}
			jpegSrc={AmiiboBackJpeg87}
		/>

		<TilePicture
			slot="back"
			imgClass="fill rounded-border"
			alt="Backside of an Animal Crossing Amiibo card"
			subgrid="B"
			columns={1}
			webpWidthSrcset={`${AmiiboFrontWebp348} 348w, ${AmiiboFrontWebp174} 174w, ${AmiiboFrontWebp87} 87w`}
			jpegWidthSrcset={`${AmiiboFrontJpeg174} 174w, ${AmiiboFrontJpeg87} 87w`}
			jpegSrc={AmiiboFrontJpeg87}
		/>
	</FlipCard>

	<div slot="description">
		<p>
			I illustrated custom Amiibo cards for a social activation on YouTube Gaming's twitter. This is
			QTCinderella's cat, Coots.
		</p>
	</div>
</ButtonTile>
