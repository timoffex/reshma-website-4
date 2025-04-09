<script lang="ts">
  import type { Snippet } from 'svelte';
  import { fadeInOut } from '$lib/fade-in-out';
  import DescriptionFlyout from '$lib/flyout/DescriptionFlyout.svelte';
  import { getFlyout } from '$lib/flyout/flyout';

  interface Props {
    /** The name of the grid area where to put the button. */
    areaName: string;
    /** Additional global styles for the button. */
    buttonClass?: string;
    /** If set, this uses additional styling for buttons containing a FlipCard. */
    card?: boolean;
    content?: Snippet;
    description?: Snippet;
  }

  let {
    areaName,
    buttonClass = undefined,
    card = false,
    content,
    description
  }: Props = $props();

  const currentFlyoutId = getFlyout();

  let extraButtonClasses = $derived(buttonClass ? ` ${buttonClass}` : '');
  let isShowingFlyout = $derived($currentFlyoutId === areaName);

  const toggleFlyout = () => {
    currentFlyoutId.update((id) => (id === areaName ? undefined : areaName));
  };
</script>

<button
  class="grid-area-{areaName} tile image-button{extraButtonClasses}"
  class:tile--no-outline={card}
  class:card-button={card}
  onclick={toggleFlyout}
  data-focused-card={isShowingFlyout}
  use:fadeInOut
>
  {@render content?.()}
</button>
<DescriptionFlyout {areaName}>
  {@render description?.()}
</DescriptionFlyout>

<style lang="scss">
  .image-button {
    padding: 0;
    border: none;
    cursor: pointer;

    // For the overlay pseudo-element.
    position: relative;

    // Briefly dim the button on click.
    &:active::after {
      content: '';
      pointer-events: none;

      display: block;
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;

      opacity: 0.2;

      background-color: black;
    }
  }

  .card-button {
    perspective: 1000px;
    background: transparent;
    overflow: visible;
  }
</style>
