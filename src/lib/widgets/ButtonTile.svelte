<script lang="ts">
	import DescriptionFlyout from '$lib/flyout/DescriptionFlyout.svelte';
	import { getFlyout } from '$lib/flyout/flyout';

  /** The name of the grid area where to put the button. */
	export let areaName: string;

  /** Additional global styles for the button. */
	export let buttonClass: string | undefined = undefined;

  /** If set, this uses additional styling for buttons containing a FlipCard. */
	export let card: boolean = false;

	const currentFlyoutId = getFlyout();

	$: extraButtonClasses = buttonClass ? ` ${buttonClass}` : '';
	$: isShowingFlyout = $currentFlyoutId === areaName;

	const toggleFlyout = () => {
		currentFlyoutId.update((id) => (id === areaName ? undefined : areaName));
	};
</script>

<button
	class="grid-area-{areaName} tile image-button{extraButtonClasses}"
	class:tile--no-outline={card}
  class:card-button={card}
	on:click={toggleFlyout}
	data-focused-card={isShowingFlyout}
>
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
