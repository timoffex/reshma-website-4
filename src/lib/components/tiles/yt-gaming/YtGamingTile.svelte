<script>
  if (typeof window !== 'undefined') import("@lottiefiles/lottie-player");

  import ButtonTile from "$lib/widgets/ButtonTile.svelte";
</script>

<ButtonTile
    areaName="yt-gaming"
    buttonClass="bg-black">
  <lottie-player
      slot="content"
      autoplay
      loop
      src="yt-gaming-logo.jsonlottie"
      class="fill image-color-on-hover">
  </lottie-player>

  <div slot="description">
    <p>
      Motion Designer for <a target="_blank" href="https://twitter.com/YouTubeGaming">
      YouTube Gaming</a> responsible for creating video and
      static design for social. <a target="_blank" href="https://www.figma.com/proto/IswuUG18DXTh663103z0oo/Reshma-Zachariah%27s-work-for-YouTube-Gaming?node-id=1-3&scaling=scale-down&page-id=0%3A1">
        See my work here</a>.
    </p>
    <p>Agency: XX Artists</p>
  </div>
</ButtonTile>
