<script>
	import Navbar from '$lib/components/navigation/Navbar.svelte';

	import EarthdaySlide1 from './earthday-slide1.mp4';
	import EarthdaySlide2 from './earthday-slide2.mp4';
	import EarthdaySlide3 from './earthday-slide3.mp4';
</script>

<!-- svelte-ignore a11y-media-has-caption -->

<div class="main-content">
	<Navbar />

	<div class="wetransfer-gallery-grid">
		<div class="wetransfer-gallery-grid__1x1">
			<video class="fill-cover" autoplay muted>
				<source src={EarthdaySlide1} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__1x1">
			<video class="fill-cover" autoplay muted>
				<source src={EarthdaySlide2} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__1x1">
			<video class="fill-cover" autoplay muted>
				<source src={EarthdaySlide3} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__1x1text">
			<p>
				Suite of assets for social made for Earth Day, or World Environment Day. Client used these
				on Instagram and Linkedin.<br />
				AD: Nate Makuch
			</p>
		</div>
	</div>
</div>

<style lang="scss">
	@use '$lib/layout/layout';

	.wetransfer-gallery-grid {
		display: grid;

		grid-template-columns: 1fr 1fr;
		grid-gap: layout.$spacing;
	}

	.wetransfer-gallery-grid__1x1 {
		display: block;
		border: 1px solid black;
		border-radius: layout.$spacing;
		aspect-ratio: 1;
		min-height: 0;
		overflow: hidden;
	}

	.wetransfer-gallery-grid__1x1text {
		display: flex;
		flex-direction: column;

		aspect-ratio: 1;

		overflow: auto;

		container-type: inline-size;

		> * {
			margin: auto;
			font-size: 6cqw;
		}
	}
</style>
