<script>
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';

	if (typeof window !== 'undefined') import('@lottiefiles/lottie-player');

	const LOTTIE_PATH = 'wetransfer3.jsonlottie';
</script>

<ButtonTile areaName="wetransfer" buttonClass="bg-black highlight:bg-red">
	<lottie-player slot="content" autoplay loop src={LOTTIE_PATH} class="fill image-color-on-hover" />

	<p slot="description">
		I created motion graphics for WeTransfer, Collect, and WEPRESENT's Twitter, Instagram and
		LinkedIn. See <a href="/wetransfer">here</a>.
	</p>
</ButtonTile>
