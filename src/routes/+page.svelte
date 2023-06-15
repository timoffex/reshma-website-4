<script>
	import { setupFlyoutContext } from '$lib/flyout/flyout';

	import Navbar from '$lib/components/navigation/Navbar.svelte';
	import AnimatedTigerTile from '$lib/components/tiles/aapi-heritage/AnimatedTigerTile.svelte';
	import NinjaTile from '$lib/components/tiles/ninja/NinjaTile.svelte';
	import NymphsTowerTile from '$lib/components/tiles/nymphs-tower/NymphsTowerTile.svelte';
	import PlayMagazineTile from '$lib/components/tiles/play-magazine/PlayMagazineTile.svelte';
	import SjSharksTile from '$lib/components/tiles/sj-sharks/SjSharksTile.svelte';
	import FlyoutScrim from '$lib/flyout/FlyoutScrim.svelte';
	import EmailAddress from '$lib/widgets/EmailAddress.svelte';
	import WattamTile from '$lib/components/tiles/wattam/WattamTile.svelte';
	import YtGamingTile from '$lib/components/tiles/yt-gaming/YtGamingTile.svelte';
	import Eyes from '$lib/components/tiles/eyes/Eyes.svelte';
	import MotionGraphicReel from '$lib/components/tiles/motion-graphic-reel/MotionGraphicReel.svelte';
	import PokemonCardTile from '$lib/components/tiles/pokemon-card/PokemonCardTile.svelte';
	import AmiiboCardTile from '$lib/components/tiles/amiibo/AmiiboCardTile.svelte';
	import SalemVideoTile from '$lib/components/tiles/salem/SalemVideoTile.svelte';
	import MusicTile from '$lib/components/tiles/music/MusicTile.svelte';
	import MarqueeText from '$lib/widgets/MarqueeText.svelte';

	setupFlyoutContext();
</script>

<div class="main-content">
	<Navbar />

	<div class="grid-container">
		<YtGamingTile />
		<SalemVideoTile />
		<SjSharksTile />
		<NinjaTile />
		<AnimatedTigerTile />
		<NymphsTowerTile />
		<Eyes />
		<MotionGraphicReel />
		<PokemonCardTile />
		<AmiiboCardTile />
		<PlayMagazineTile />
		<WattamTile />
		<MusicTile />
		<div class="tile grid-area-music-blank"></div>
	</div> 
</div>

<MarqueeText animationSeconds={60}>
	Universal Music Group &#x2726;
	YouTube Gaming &#x2726;
	YouTube Shorts &#x2726;
	YouTube (#MinecraftMuseum, Pride 2022, 2021 &amp; 2020, Kids &amp; Family) &#x2726;
	XQ Institute &#x2726;
	Elizabeth Taylor AIDS Foundation &#x2726;
	San Jos&eacute; Sharks &#x2726;
	Third Eye Blind &#x2726;
	Soundgarden &#x2726;
	311 &#x2726;
	The Used &#x2726;
	Michael Bubl&eacute; &#x2726;
	WeTransfer &#x2726;
	Robinhood &#x2726;
	Ninja &#x2726;
	Lee Trink (FaZe Clan) &#x2726;
	Brie Larson &#x2726;
	Lilly Singh &#x2726;
	Roblox Splash's Virtual Influencer Kai &#x2726;
	Riot Games - WORLDS 2022 &#x2726;&nbsp;
</MarqueeText>

<div class="main-content">
	<div id="contact" class="lets-collaborate">
		<span class="lets-collaborate__1">let's</span>
		<br />
		<span class="lets-collaborate__2">collaborate</span>
	</div>
	<div class="reshma-email">
		<a
			target="_blank"
			href="https://www.canva.com/design/DAFdB-ifsjA/vdLPP5e-seBxAO-OUWKYgA/view?utm_content=DAFdB-ifsjA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
		>
			Resum&eacute;</a
		><br />
		Email me to see my client work
		<br />
		<EmailAddress email="reshmasz.art@gmail.com" />
	</div>
	<div class="developer-credits">
		<span>
			Custom-developed by Timofey Peshin (<EmailAddress email="timoffex@gmail.com" />)
		</span>
		<br />
		<span> Website mocked in Figma </span>
		<br />
		<span> Animated in After Effects and Lottie </span>
	</div>
</div>
<FlyoutScrim />

<style>
	.lets-collaborate {
		margin-top: 2rem;
		line-height: 0.8;
	}

	.lets-collaborate__1 {
		font-family: 'adobe-caslon-pro', serif;
		font-weight: 600;
		font-style: italic;
		letter-spacing: -0.2rem;

		font-size: 3rem;
	}

	.lets-collaborate__2 {
		font-family: 'Roboto Mono';
		font-size: 2rem;
	}

	.reshma-email {
		font-family: 'Roboto Mono';
		text-align: right;
		margin-top: 1rem;
	}

	.developer-credits {
		text-align: right;
		margin-top: 1rem;
		font-size: 0.5rem;
		color: #1e1e1e;
	}
</style>
