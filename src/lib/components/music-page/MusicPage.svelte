<script>
	import Navbar from '../navigation/Navbar.svelte';

	import ThirdEyeBlindWebm from './3EB.webm';
	import ThirdEyeBlindMp4 from './3EB.mp4';

	const THIRD_EYE_BLIND_ASPECT_RATIO = 1920 / 1080;
</script>

<div class="main-content extra-padding-bottom">
	<Navbar />
</div>

<!-- svelte-ignore a11y-media-has-caption -->
<video
	class="full-bleed-1920"
	controls
	preload="metadata"
	style="aspect-ratio: {THIRD_EYE_BLIND_ASPECT_RATIO};"
>
	<source src={ThirdEyeBlindWebm} type="video/webm" />
	<source src={ThirdEyeBlindMp4} type="video/mp4" />
</video>

<div class="main-content text-align-right">
	<p>
		Client: Third Eye Blind<br />
		Agency: XX Artists<br />
		Creative Director: Mackenna Millet<br />
		Director of Talent: Melissa Mondello<br />
	</p>
</div>

<style>
	.extra-padding-bottom {
		padding-bottom: 24px;
	}

	.full-bleed-1920 {
		display: block;

		width: 100%;
		max-width: 1920px;
		margin: 0 auto;
		padding: 0;
	}

	.text-align-right {
		text-align: right;
	}
</style>
