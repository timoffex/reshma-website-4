<script>
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';
	import FlipCard from '$lib/widgets/FlipCard.svelte';
	import TilePicture from '$lib/layout/TilePicture.svelte';

	import BacksideWebp348 from './pokemon-card-back-348.webp';
	import BacksideWebp174 from './pokemon-card-back-348.webp?w=174&imagetools';
	import BacksideWebp87 from './pokemon-card-back-348.webp?w=87&imagetools';

	import BacksideJpeg174 from './pokemon-card-back-348.webp?w=174&jpeg&imagetools';
	import BacksideJpeg87 from './pokemon-card-back-348.webp?w=87&jpeg&imagetools';

	import GlitchCityWebp348 from './glitch-city-348.webp';
	import GlitchCityWebp174 from './glitch-city-348.webp?w=174&imagetools';
	import GlitchCityWebp87 from './glitch-city-348.webp?w=87&imagetools';

	import GlitchCityJpeg174 from './glitch-city-348.webp?w=174&jpeg&imagetools';
	import GlitchCityJpeg87 from './glitch-city-348.webp?w=87&jpeg&imagetools';
</script>

<ButtonTile card areaName="pokemon">
	<FlipCard slot="content">
		<TilePicture
			slot="front"
			imgClass="fill rounded-border"
			picture={{
				case: 'gridB-1',
				alt: 'Backside of a Pokemon card',

				webp348: BacksideWebp348,
				webp174: BacksideWebp174,
				webp87: BacksideWebp87,

				jpeg174: BacksideJpeg174,
				jpeg87: BacksideJpeg87
			}}
		/>

		<TilePicture
			slot="back"
			imgClass="fill rounded-border"
			picture={{
				case: 'gridB-1',
				alt: 'Custom Pokemon card for YouTuber GlitchxCity',

				webp348: GlitchCityWebp348,
				webp174: GlitchCityWebp174,
				webp87: GlitchCityWebp87,

				jpeg174: GlitchCityJpeg174,
				jpeg87: GlitchCityJpeg87
			}}
		/>
	</FlipCard>

	<div slot="description">
		<p>
			For Pok&eacute;mon Day 2023, I <a
				target="_blank"
				href="https://dotesports.com/pokemon/news/youtube-gaming-celebrated-pokemon-day-with-custom-tcg-cards-for-content-creators"
			>
				illustrated four Pok&eacute;mon cards</a
			> of top creators and their buddy pokemon.
		</p>
	</div>
</ButtonTile>
