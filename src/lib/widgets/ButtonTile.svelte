<script lang="ts">
  import DescriptionFlyout from "$lib/flyout/DescriptionFlyout.svelte";
  import { currentFlyoutId } from "$lib/flyout/flyout";

  export let areaName: string;
  export let buttonClass: string|undefined = undefined;

  $: extraButtonClasses = buttonClass ? ` ${buttonClass}` : '';
  $: isShowingFlyout = $currentFlyoutId === areaName;

  const toggleFlyout = () => {
    currentFlyoutId.update((id) => id === areaName ? undefined : areaName);
  };
</script>

<button
    class="grid-area-{areaName} tile image-button{extraButtonClasses}"
    on:click={toggleFlyout}
    data-focused-card={isShowingFlyout}>
  <slot name="content" />
</button>
<DescriptionFlyout {areaName}>
  <slot name="description" />
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
      content: "";
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
</style>