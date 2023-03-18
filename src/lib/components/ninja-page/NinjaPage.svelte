<script>
	import Navbar from '$lib/components/navigation/Navbar.svelte';
	import { mainContentSizesList } from '$lib/layout/layout';
	import Slideshow from '$lib/widgets/Slideshow.svelte';

	import NinjaThumbnailsWebpSrcset from './ninja-yt-thumbnails-1033.png?w=1033;800;600&webp&srcset&imagetools';
	import NinjaThumbnailsJpegSrcset from './ninja-yt-thumbnails-1033.png?w=1033;800;600&jpeg&srcset&imagetools';

	import MinecraftWebpSrcset from './slides/minecraft.png?w=1000;800;600&webp&srcset&imagetools';
	import MinecraftJpegSrcset from './slides/minecraft.png?w=1000;800;600&jpeg&srcset&imagetools';

	import VictoryRoyaleWebpSrcset from './slides/victory-royale.png?w=1000;800;600&webp&srcset&imagetools';
	import VictoryRoyaleJpegSrcset from './slides/victory-royale.png?w=1000;800;600&jpeg&srcset&imagetools';

	import LotsOfDamageWebpSrcset from './slides/lots-of-damage.png?w=1000;800;600&webp&srcset&imagetools';
	import LotsOfDamageJpegSrcset from './slides/lots-of-damage.png?w=1000;800;600&jpeg&srcset&imagetools';

	import FirstTimePlayingWebpSrcset from './slides/first-time.png?w=1000;800;600&webp&srcset&imagetools';
	import FirstTimePlayingJpegSrcset from './slides/first-time.png?w=1000;800;600&jpeg&srcset&imagetools';

	import UnstoppableWebpSrcset from './slides/unstoppable.png?w=1000;800;600&webp&srcset&imagetools';
	import UnstoppableJpegSrcset from './slides/unstoppable.png?w=1000;800;600&jpeg&srcset&imagetools';

	import TiktokStreamerWebpSrcset from './slides/tiktok-streamer.png?w=1000;800;600&webp&srcset&imagetools';
	import TiktokStreamerJpegSrcset from './slides/tiktok-streamer.png?w=1000;800;600&jpeg&srcset&imagetools';

	import RickAndMortyWebpSrcset from './slides/rick-and-morty.png?w=1000;800;600&webp&srcset&imagetools';
	import RickAndMortyJpegSrcset from './slides/rick-and-morty.png?w=1000;800;600&jpeg&srcset&imagetools';

	import CallOfDutyWebpSrcset from './slides/warzone.png?w=1000;800;600&webp&srcset&imagetools';
	import CallOfDutyJpegSrcset from './slides/warzone.png?w=1000;800;600&jpeg&srcset&imagetools';

	import EpicWeaponWebpSrcset from './slides/epic-weapon.png?w=1000;800;600&webp&srcset&imagetools';
	import EpicWeaponJpegSrcset from './slides/epic-weapon.png?w=1000;800;600&jpeg&srcset&imagetools';
</script>

<div class="main-content">
	<Navbar />

	<div class="slideshow">
		<Slideshow
			delayMs={3000}
			sizes={mainContentSizesList}
			images={[
				{
					alt: '"Minecraft" thumbnail',
					webpSrcset: MinecraftWebpSrcset,
					jpegSrcset: MinecraftJpegSrcset
				},
				{
					alt: '"Victory Royale" thumbnail',
					webpSrcset: VictoryRoyaleWebpSrcset,
					jpegSrcset: VictoryRoyaleJpegSrcset
				},
				{
					alt: '"Lots of Damage" thumbnail',
					webpSrcset: LotsOfDamageWebpSrcset,
					jpegSrcset: LotsOfDamageJpegSrcset
				},
				{
					alt: '"First Time Playing" thumbnail',
					webpSrcset: FirstTimePlayingWebpSrcset,
					jpegSrcset: FirstTimePlayingJpegSrcset
				},
				{
					alt: '"Unstoppable" thumbnail',
					webpSrcset: UnstoppableWebpSrcset,
					jpegSrcset: UnstoppableJpegSrcset
				},
				{
					alt: '"Tiktok Streamer!?" thumbnail',
					webpSrcset: TiktokStreamerWebpSrcset,
					jpegSrcset: TiktokStreamerJpegSrcset
				},
				{
					alt: '"Rick and Morty" thumbnail',
					webpSrcset: RickAndMortyWebpSrcset,
					jpegSrcset: RickAndMortyJpegSrcset
				},
				{
					alt: '"Call of Duty Warzone" thumbnail',
					webpSrcset: CallOfDutyWebpSrcset,
					jpegSrcset: CallOfDutyJpegSrcset
				},
				{
					alt: '"Epic Weapon" thumbnail',
					webpSrcset: EpicWeaponWebpSrcset,
					jpegSrcset: EpicWeaponJpegSrcset
				}
			]}
		/>
	</div>

	<div class="description-text">
		<div class="client-description">
			Client: Ninja<br />
			Agency: XX Artists<br />
			Creative Director: Nate Makuch<br />
		</div>
		<div class="work-description">
			Designed numerous thumbnails for esports talent, Ninja.<br />
			Videos have over 100K views each.<br />
			<br />
			2021
		</div>
	</div>

	<picture>
		<source type="image/webp" srcset={NinjaThumbnailsWebpSrcset} sizes={mainContentSizesList} />
		<source type="image/jpeg" srcset={NinjaThumbnailsJpegSrcset} sizes={mainContentSizesList} />
		<img src="" alt="Ninja's YouTube thumbnails" class="thumbnails" />
	</picture>
</div>

<style lang="scss">
	.thumbnails {
		display: block;
	}

	.description-text {
		text-align: right;
	}

	.client-description {
		margin-top: 3rem;
		font-size: 0.8rem;
	}

	.work-description {
		margin-top: 3rem;
		margin-bottom: 3rem;
	}

	.slideshow {
		width: 100%;
		height: min(35rem, 63vw);
	}
</style>
