<script lang="ts">
  import { getFlyout } from './flyout';

  const currentFlyoutId = getFlyout();

  let isFlyoutOpen = $derived($currentFlyoutId !== undefined);
  let visibility = $derived(isFlyoutOpen ? 'visible' : 'hidden');

  const hideFlyout = () => {
    currentFlyoutId.set(undefined);
  };
</script>

<div onclick={hideFlyout} onkeyup={hideFlyout} class={visibility}></div>

<style lang="scss">
  @use '$lib/layout/layout';

  .hidden {
    display: none;
  }

  .visible {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;

    z-index: layout.$z-index-focus-backdrop;

    background-color: black;
    opacity: 0.8;

    animation: 0.3s appear;
  }

  @keyframes appear {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 0.8;
    }
  }
</style>
