<script>
	import Navbar from '$lib/components/navigation/Navbar.svelte';
	import { mainContentSizeExpr } from '$lib/layout/layout';
	import Slideshow from '$lib/widgets/Slideshow.svelte';

	import NinjaThumbnailsWebpSrcset from './ninja-yt-thumbnails-1033.png?w=1033;800;600&webp&srcset&imagetools';
	import NinjaThumbnailsJpegSrcset from './ninja-yt-thumbnails-1033.png?w=1033;800;600&jpeg&srcset&imagetools';

	import MinecraftWebpSrcset from './slides/minecraft.png?w=1000;800;600&webp&srcset&imagetools';
	import MinecraftJpegSrcset from './slides/minecraft.png?w=1000;800;600&jpeg&srcset&imagetools';
	import MinecraftJpeg from './slides/minecraft.png?w=600&jpeg&imagetools';

	import VictoryRoyaleWebpSrcset from './slides/victory-royale.png?w=1000;800;600&webp&srcset&imagetools';
	import VictoryRoyaleJpegSrcset from './slides/victory-royale.png?w=1000;800;600&jpeg&srcset&imagetools';
	import VictoryRoyaleJpeg from './slides/victory-royale.png?w=600&jpeg&imagetools';

	import LotsOfDamageWebpSrcset from './slides/lots-of-damage.png?w=1000;800;600&webp&srcset&imagetools';
	import LotsOfDamageJpegSrcset from './slides/lots-of-damage.png?w=1000;800;600&jpeg&srcset&imagetools';
	import LotsOfDamageJpeg from './slides/lots-of-damage.png?w=600&jpeg&imagetools';

	import FirstTimePlayingWebpSrcset from './slides/first-time.png?w=1000;800;600&webp&srcset&imagetools';
	import FirstTimePlayingJpegSrcset from './slides/first-time.png?w=1000;800;600&jpeg&srcset&imagetools';
	import FirstTimePlayingJpeg from './slides/first-time.png?w=600&jpeg&imagetools';

	import UnstoppableWebpSrcset from './slides/unstoppable.png?w=1000;800;600&webp&srcset&imagetools';
	import UnstoppableJpegSrcset from './slides/unstoppable.png?w=1000;800;600&jpeg&srcset&imagetools';
	import UnstoppableJpeg from './slides/unstoppable.png?w=600&jpeg&imagetools';

	import TiktokStreamerWebpSrcset from './slides/tiktok-streamer.png?w=1000;800;600&webp&srcset&imagetools';
	import TiktokStreamerJpegSrcset from './slides/tiktok-streamer.png?w=1000;800;600&jpeg&srcset&imagetools';
	import TiktokStreamerJpeg from './slides/tiktok-streamer.png?w=600&jpeg&imagetools';

	import RickAndMortyWebpSrcset from './slides/rick-and-morty.png?w=1000;800;600&webp&srcset&imagetools';
	import RickAndMortyJpegSrcset from './slides/rick-and-morty.png?w=1000;800;600&jpeg&srcset&imagetools';
	import RickAndMortyJpeg from './slides/rick-and-morty.png?w=600&jpeg&imagetools';

	import CallOfDutyWebpSrcset from './slides/warzone.png?w=1000;800;600&webp&srcset&imagetools';
	import CallOfDutyJpegSrcset from './slides/warzone.png?w=1000;800;600&jpeg&srcset&imagetools';
	import CallOfDutyJpeg from './slides/warzone.png?w=600&jpeg&imagetools';

	import EpicWeaponWebpSrcset from './slides/epic-weapon.png?w=1000;800;600&webp&srcset&imagetools';
	import EpicWeaponJpegSrcset from './slides/epic-weapon.png?w=1000;800;600&jpeg&srcset&imagetools';
	import EpicWeaponJpeg from './slides/epic-weapon.png?w=600&jpeg&imagetools';
</script>

<div class="main-content">
	<Navbar />

	<div class="slideshow">
		<Slideshow
			delayMs={5000}
			sizes={mainContentSizeExpr}
			images={[
				{
					alt: '"Minecraft" thumbnail',
					defaultSrc: MinecraftJpeg,
					webpSrcset: MinecraftWebpSrcset,
					jpegSrcset: MinecraftJpegSrcset
				},
				{
					alt: '"Victory Royale" thumbnail',
					defaultSrc: VictoryRoyaleJpeg,
					webpSrcset: VictoryRoyaleWebpSrcset,
					jpegSrcset: VictoryRoyaleJpegSrcset
				},
				{
					alt: '"Lots of Damage" thumbnail',
					defaultSrc: LotsOfDamageJpeg,
					webpSrcset: LotsOfDamageWebpSrcset,
					jpegSrcset: LotsOfDamageJpegSrcset
				},
				{
					alt: '"First Time Playing" thumbnail',
					defaultSrc: FirstTimePlayingJpeg,
					webpSrcset: FirstTimePlayingWebpSrcset,
					jpegSrcset: FirstTimePlayingJpegSrcset
				},
				{
					alt: '"Unstoppable" thumbnail',
					defaultSrc: UnstoppableJpeg,
					webpSrcset: UnstoppableWebpSrcset,
					jpegSrcset: UnstoppableJpegSrcset
				},
				{
					alt: '"Tiktok Streamer!?" thumbnail',
					defaultSrc: TiktokStreamerJpeg,
					webpSrcset: TiktokStreamerWebpSrcset,
					jpegSrcset: TiktokStreamerJpegSrcset
				},
				{
					alt: '"Rick and Morty" thumbnail',
					defaultSrc: RickAndMortyJpeg,
					webpSrcset: RickAndMortyWebpSrcset,
					jpegSrcset: RickAndMortyJpegSrcset
				},
				{
					alt: '"Call of Duty Warzone" thumbnail',
					defaultSrc: CallOfDutyJpeg,
					webpSrcset: CallOfDutyWebpSrcset,
					jpegSrcset: CallOfDutyJpegSrcset
				},
				{
					alt: '"Epic Weapon" thumbnail',
					defaultSrc: EpicWeaponJpeg,
					webpSrcset: EpicWeaponWebpSrcset,
					jpegSrcset: EpicWeaponJpegSrcset
				}
			]}
		/>
	</div>

	<p class="text-align-right text-smaller">
		Client: Ninja<br />
		Agency: XX Artists<br />
		Creative Director: Nate Makuch<br />
	</p>
	<p class="text-align-right">
		Designed numerous thumbnails for esports talent, Ninja.<br />
		Videos have over 100K views each.<br />
		<br />
		2021
	</p>

	<picture>
		<source type="image/webp" srcset={NinjaThumbnailsWebpSrcset} sizes={mainContentSizeExpr} />
		<source type="image/jpeg" srcset={NinjaThumbnailsJpegSrcset} sizes={mainContentSizeExpr} />
		<img src="" alt="Ninja's YouTube thumbnails" class="thumbnails" />
	</picture>
</div>

<style lang="scss">
	.thumbnails {
		display: block;
	}

	.text-align-right {
		text-align: right;
	}

	.text-smaller {
		font-size: 0.8rem;
	}

	.slideshow {
		width: 100%;
		height: min(35rem, 63vw);
	}
</style>
