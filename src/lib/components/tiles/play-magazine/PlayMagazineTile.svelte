<script>
	import TilePicture from "$lib/layout/TilePicture.svelte";
  import ButtonTile from "$lib/widgets/ButtonTile.svelte";

  import PlayMagazineWebp348 from './play-magazine-cover-348.webp';
  import PlayMagazineWebp174 from './play-magazine-cover-174.webp';
  import PlayMagazineWebp87 from './play-magazine-cover-87.webp';

  import PlayMagazineJpeg174 from './play-magazine-cover-174.webp?jpeg&imagetools';
  import PlayMagazineJpeg87 from './play-magazine-cover-87.webp?jpeg&imagetools';
</script>

<ButtonTile areaName="play-magazine">
  <TilePicture
      slot="content"
      imgClass="fill-cover image-color-on-hover-2"
      loading="lazy"
      picture={{
        case: 'gridB-1',
        alt: 'PLAY! Magazine',

        webp348: PlayMagazineWebp348,
        webp174: PlayMagazineJpeg174,
        webp87: PlayMagazineJpeg87,

        jpeg174: PlayMagazineJpeg174,
        jpeg87: PlayMagazineJpeg87,
      }} />
  
  <div slot="description">
    <p>
      I started PLAY! Magazine, a digital arts and creative writing
      publication, on my university campus. <a target='_blank' href='https://www.artstation.com/artwork/baP55r'>
        Read more here.</a>
    </p>
  </div>
</ButtonTile>