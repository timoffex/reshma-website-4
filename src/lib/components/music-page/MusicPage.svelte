<script>
	import Navbar from '$lib/components/navigation/Navbar.svelte';
	import Hand16x9 from '$lib/widgets/Hand16x9.svelte';

	import ThirdEyeBlindWebm from './3EB.webm';
	import ThirdEyeBlindMp4 from './3EB.mp4';

	import ThreeOneOneWebm from './311.webm';
	import ThreeOneOneMp4 from './311.mp4';
</script>

<div class="main-content">
	<Navbar />

	<Hand16x9>
		<!-- svelte-ignore a11y-media-has-caption -->
		<video class="fill" controls preload="metadata" style="aspect-ratio: 1920/1080;">
			<source src={ThirdEyeBlindWebm} type="video/webm" />
			<source src={ThirdEyeBlindMp4} type="video/mp4" />
		</video>
	</Hand16x9>

	<p class="text-align-right">
		Client: Third Eye Blind<br />
		Agency: XX Artists<br />
		Creative Director: Mackenna Millet<br />
		Director of Talent: Melissa Mondello<br />
	</p>

	<div class="separating-space" />

	<Hand16x9>
		<!-- svelte-ignore a11y-media-has-caption -->
		<video class="fill" controls preload="metadata" style="aspect-ratio: 1920/1080;">
			<source src={ThreeOneOneWebm} type="video/webm" />
			<source src={ThreeOneOneMp4} type="video/mp4" />
		</video>
	</Hand16x9>

	<p class="text-align-right">
		Client: 311<br />
		Agency: XX Artists<br />
		Creative Director: Mackenna Millet<br />
		Director of Talent: Melissa Mondello<br />
	</p>
</div>

<style>
	.separating-space {
		height: 100px;
	}

	.text-align-right {
		text-align: right;
	}
</style>
