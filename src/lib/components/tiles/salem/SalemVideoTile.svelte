<script>
	import ButtonTile from '$lib/widgets/ButtonTile.svelte';

	import SalemVideoWebm720 from './salem-PS5-reel-720.webm';
	import SalemVideoMp4720 from './salem-PS5-reel-720.mp4';
</script>

<ButtonTile areaName="salem">
	<video
		slot="content"
		autoplay
		loop
		muted
		playsinline
		class="fill-contain image-color-on-hover bg-black"
		tabIndex={-1}
	>
		<source src={SalemVideoWebm720} type="video/webm" />
		<source src={SalemVideoMp4720} type="video/mp4" />

		<a href="https://drive.google.com/file/d/1rKDYnoZy0isK_Yy09Ulm6rZahQca85UZ/view?usp=share_link">
			Reel of contributions to Salem Ilese's "PS5" music video
		</a>
	</video>

	<div slot="description">
		<p>
			I created retro game inspired pixel art VFX that complemented director Christina Xing's vision
			for <a target="_blank" href="https://youtu.be/WRVonH0TTS8">Salem Ilese's music video, PS5</a>.
		</p>
		<p>Production House: Our Secret Handshake</p>
	</div>
</ButtonTile>
