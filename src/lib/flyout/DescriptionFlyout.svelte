<script lang="ts">
	import { currentFlyoutId } from "./flyout";

  export let areaName: string;

  $: isOpen = $currentFlyoutId === areaName;
  $: visibility = isOpen ? 'visible' : 'hidden';
</script>

<div class="grid-desc-{areaName} {visibility}">
  <slot />
</div>

<style lang="scss">
  @use '$lib/layout/layout';

  .hidden { display: none; }

  .visible {
    z-index: layout.$z-index-description-flyout;

    color: white;
    :global(a:link) { color: cyan; }
    :global(a:visited) { color: magenta; }

    animation: 0.3s flyout;
  }

  @keyframes flyout {
    0% { transform: translateY(-100%); opacity: 0; }
    100% { transform: none; opacity: 1; }
  }
</style>