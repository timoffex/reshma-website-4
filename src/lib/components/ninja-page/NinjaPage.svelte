<script>
  import Navbar from '$lib/components/navigation/Navbar.svelte';
  import { mainContentSizeExpr } from '$lib/layout/layout';
</script>

<div class="main-content">
  <Navbar />

  <p class="text-align-right text-small">
    Client: Ninja<br />
    Agency: XX Artists<br />
    Creative Director: Nate Makuch<br />
  </p>
  <p class="text-align-right">
    Designed numerous thumbnails for esports talent, Ninja.<br />
    Videos have over 100K views each.<br />
    <br />
    2021
  </p>

  <enhanced:img
    src="./ninja-yt-thumbnails-1033.png?w=1033;800;600"
    alt="Ninja's YouTube thumbnails"
    sizes={mainContentSizeExpr}
    class="thumbnails"
  />
</div>

<style lang="scss">
  .thumbnails {
    display: block;
    width: 100%;
    height: auto;
  }
</style>
