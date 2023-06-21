<script>
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';
	import FlipCard from '$lib/widgets/FlipCard.svelte';
	import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';

	import { AmiiboBack, AmiiboFront } from '$lib/generated-images';
	import { gridBSizesList } from '$lib/layout/layout';
</script>

<ButtonTile card areaName="amiibo">
	<FlipCard slot="content">
		<GeneratedImage
			slot="front"
			imgClass="fill rounded-border"
			image={{
				alt: 'Backside of an Animal Crossing Amiibo card',
				...AmiiboBack
			}}
			sizes={gridBSizesList(1)}
		/>

		<GeneratedImage
			slot="back"
			imgClass="fill rounded-border"
			image={{
				alt: 'Backside of an Animal Crossing Amiibo card',
				...AmiiboFront
			}}
			sizes={gridBSizesList(1)}
		/>
	</FlipCard>

	<div slot="description">
		<p>
			I illustrated <a
				target="_blank"
				href="https://www.essentiallysports.com/esports-news-animal-crossing-new-horizons-on-the-third-anniversary-of-the-game-pets-of-streamers-including-sykkuno-valkyrae-and-more-joins-the-villagers/"
				>custom Amiibo cards</a
			> for a social activation on YouTube Gaming's twitter. This is QTCinderella's cat, Coots.
		</p>
	</div>
</ButtonTile>
