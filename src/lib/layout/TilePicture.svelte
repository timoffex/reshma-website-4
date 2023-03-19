<script lang="ts">
	import { gridASizesList, gridBSizesList } from './layout';

	export let imgClass: string;
	export let loading: 'lazy' | undefined = undefined;

	export let alt: string;

	export let subgrid: 'A' | 'B';
	export let columns: number;

	$: sizes = subgrid === 'A' ? gridASizesList(columns) : gridBSizesList(columns);

	export let webpWidthSrcset: string;
	export let jpegWidthSrcset: string;
	export let jpegSrc: string;
</script>

<picture>
	<source type="image/webp" srcset={webpWidthSrcset} {sizes} />
	<source type="image/jpeg" srcset={jpegWidthSrcset} {sizes} />
	<img class={imgClass} {loading} {alt} src={jpegSrc} />
</picture>
