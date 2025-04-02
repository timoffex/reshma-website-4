<script>
	import SalemVideoWebm720 from './salem-PS5-reel-720.webm';
	import SalemVideoMp4720 from './salem-PS5-reel-720.mp4';
	import { fadeInOut } from '$lib/fade-in-out';
</script>

<a href="/salem" class="display-block tile grid-area-salem" use:fadeInOut>
	<video
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
</a>
