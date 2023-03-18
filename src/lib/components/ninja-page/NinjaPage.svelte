<script>
	import Navbar from '$lib/components/navigation/Navbar.svelte';

	import NinjaThumbnailsWebpSrcset from './ninja-yt-thumbnails-1033.png?w=1033;800;600&webp&srcset&imagetools';
	import NinjaThumbnailsJpegSrcset from './ninja-yt-thumbnails-1033.png?w=1033;800;600&jpeg&srcset&imagetools';
	import { mainContentSizesList } from '$lib/layout/layout';
</script>

<div class="main-content">
	<Navbar />

	<div class="slideshow">
		<!-- <Slideshow delayMs={3000} images={SLIDESHOW} /> -->
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
