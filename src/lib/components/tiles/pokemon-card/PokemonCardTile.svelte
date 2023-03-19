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
			alt="Backside of a Pokemon card"
			subgrid="B"
			columns={1}
			webpWidthSrcset={`${BacksideWebp348} 348w, ${BacksideWebp174} 174w, ${BacksideWebp87} 87w`}
			jpegWidthSrcset={`${BacksideJpeg174} 174w, ${BacksideJpeg87} 87w`}
			jpegSrc={BacksideJpeg87}
		/>

		<TilePicture
			slot="back"
			imgClass="fill rounded-border"
			alt="Custom Pokemon card for YouTuber GlitchxCity"
			subgrid="B"
			columns={1}
			webpWidthSrcset={`${GlitchCityWebp348} 348w, ${GlitchCityWebp174} 174w, ${GlitchCityWebp87} 87w`}
			jpegWidthSrcset={`${GlitchCityJpeg174} 174w, ${GlitchCityJpeg87} 87w`}
			jpegSrc={GlitchCityJpeg87}
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
