<script>
	import Eyeball from '$lib/widgets/Eyeball.svelte';
	import { mousePosition } from '$lib/mouse-position';

  // TODO: On mobile, look around randomly.
  // TODO: Also consider looking at focused item.
</script>

<div class="grid-area-eyes tile container">
	<div class="eyeball-wrapper">
		<Eyeball lookAt={$mousePosition} />
	</div>
	<div class="eyeball-wrapper">
		<Eyeball lookAt={$mousePosition} />
	</div>
</div>

<style lang="scss">
	@use '$lib/layout/layout';

	.container {
		display: flex;
		align-items: center;

		gap: layout.$spacing;
		padding: layout.$spacing;

		background-color: black;
	}

	.eyeball-wrapper {
		flex-grow: 1;
	}
</style>
