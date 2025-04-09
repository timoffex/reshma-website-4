<script>
  import TilePicture from '$lib/layout/TilePicture.svelte';
  import ButtonTile from '$lib/widgets/ButtonTile.svelte';

  import PlayMagazineWebp348 from './play-magazine-cover-348.webp';
  import PlayMagazineWebp174 from './play-magazine-cover-174.webp';
  import PlayMagazineWebp87 from './play-magazine-cover-87.webp';

  import PlayMagazineJpeg174 from './play-magazine-cover-174.webp?jpeg&imagetools';
  import PlayMagazineJpeg87 from './play-magazine-cover-87.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="play-magazine">
  {#snippet content()}
    <TilePicture
      imgClass="fill-cover image-color-on-hover-2"
      loading="lazy"
      alt="PLAY! Magazine"
      subgrid="B"
      columns={1}
      mobileWebp={PlayMagazineWebp174}
      mobileJpeg={PlayMagazineJpeg174}
      webpWidthSrcset={`${PlayMagazineWebp348} 348w, ${PlayMagazineWebp174} 174w, ${PlayMagazineWebp87} 87w`}
      jpegWidthSrcset={`${PlayMagazineJpeg174} 174w, ${PlayMagazineJpeg87} 87w`}
      jpegSrc={PlayMagazineJpeg87}
    />
  {/snippet}

  {#snippet description()}
    <div>
      <p>
        I started PLAY! Magazine, a digital arts and creative writing
        publication, on my university campus. <a
          target="_blank"
          href="https://www.artstation.com/artwork/baP55r"
        >
          Read more here.</a
        >
      </p>
    </div>
  {/snippet}
</ButtonTile>
