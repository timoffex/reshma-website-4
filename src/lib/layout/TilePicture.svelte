<script lang="ts">
  import { gridASizesList, gridBSizesList } from './layout';

  interface Props {
    imgClass: string;
    loading?: 'lazy';
    alt: string;
    subgrid: 'A' | 'B';
    columns: number;
    mobileWebp: string;
    mobileJpeg: string;
    webpWidthSrcset: string;
    jpegWidthSrcset: string;
    jpegSrc: string;
  }

  let {
    imgClass,
    loading = undefined,
    alt,
    subgrid,
    columns,
    mobileWebp,
    mobileJpeg,
    webpWidthSrcset,
    jpegWidthSrcset,
    jpegSrc
  }: Props = $props();

  let sizes = $derived(
    subgrid === 'A' ? gridASizesList(columns) : gridBSizesList(columns)
  );
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
