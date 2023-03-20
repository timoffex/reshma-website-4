<script lang="ts">
	import { gridASizesList, gridBSizesList } from './layout';

	export let imgClass: string;
	export let loading: 'lazy' | undefined = undefined;

	export let alt: string;

	export let subgrid: 'A' | 'B';
	export let columns: number;

	$: sizes = subgrid === 'A' ? gridASizesList(columns) : gridBSizesList(columns);

	export let mobileWebp: string;
	export let mobileJpeg: string;
	export let webpWidthSrcset: string;
	export let jpegWidthSrcset: string;
	export let jpegSrc: string;
</script>

<picture>
	<!--
		Mobile phones tend to have very high resolution, but since they're
		often used on slower connections, we don't want them to download super
		large images.
	-->
	<source media="(max-width: 400px)" type="image/webp" srcset={mobileWebp} />
	<source media="(max-width: 400px)" type="image/jpeg" srcset={mobileJpeg} />
	<source type="image/webp" srcset={webpWidthSrcset} {sizes} />
	<source type="image/jpeg" srcset={jpegWidthSrcset} {sizes} />
	<img class={imgClass} {loading} {alt} src={jpegSrc} />
</picture>
