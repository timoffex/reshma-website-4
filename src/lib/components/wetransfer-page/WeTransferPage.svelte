<script>
	import Navbar from '$lib/components/navigation/Navbar.svelte';

	import EarthdaySlide1 from './earthday-slide1.mp4';
	import EarthdaySlide2 from './earthday-slide2.mp4';
	import EarthdaySlide3 from './earthday-slide3.mp4';

	import GirlInRed1 from './girl-in-red1.mp4';
	import GirlInRed2 from './girl-in-red2.mp4';
</script>

<!-- svelte-ignore a11y-media-has-caption -->

<div class="main-content">
	<Navbar />

	<div class="wetransfer-gallery-grid">
		<div class="wetransfer-gallery-grid__1x1">
			<video class="fill-cover" autoplay loop muted>
				<source src={EarthdaySlide1} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__1x1">
			<video class="fill-cover" autoplay loop muted>
				<source src={EarthdaySlide2} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__1x1">
			<video class="fill-cover" autoplay loop muted>
				<source src={EarthdaySlide3} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__text">
			<p>
				Suite of assets for social made for Earth Day, or World Environment Day. Client used these
				on Instagram and Linkedin.<br /><br />
				AD: Nate Makuch
			</p>
		</div>
	</div>
	<div class="wetransfer-gallery-grid">
		<div class="wetransfer-gallery-grid__1x1">
			<video class="fill-cover" autoplay loop muted>
				<source src={GirlInRed2} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__9x16">
			<video class="fill-cover" autoplay loop muted>
				<source src={GirlInRed1} />
			</video>
		</div>

		<div class="wetransfer-gallery-grid__text next-to-9x16">
			<p>
				Assets made for WEPRESENT's collaboration with Tillie Walden and girl in red. Used on
				Instagram and Twitter.<br /><br />
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
		grid-row: span 1;
		grid-column: span 1;

		display: block;
		border: 1px solid black;
		border-radius: layout.$spacing;
		aspect-ratio: 1;
		min-height: 0;
		overflow: hidden;
	}

	.wetransfer-gallery-grid__9x16 {
		grid-row: span 2;
		grid-column: span 1;

		display: block;
		border: 1px solid black;
		border-radius: layout.$spacing;
		aspect-ratio: 9 / 16;
		min-height: 0;
		overflow: hidden;
	}

	.wetransfer-gallery-grid__text {
		display: flex;
		flex-direction: column;

		overflow: auto;

		container-type: inline-size;

		> * {
			margin: auto;
			font-size: 6cqw;
		}
	}

	// An imperfect way to get an item below a 1x1 square and
	// next to a 9x16 rectangle to take up the remaining space.
	.next-to-9x16 {
		aspect-ratio: 9 / 7;
	}
</style>
