<div class="container">
	<div class="card-front">
		<slot name="front" />
	</div>
	<div class="card-back">
		<slot name="back" />
	</div>
</div>

<style lang="scss">
	.container {
		position: relative;
		width: 100%;
		height: 100%;

		transition: transform 0.6s;
		transform-style: preserve-3d;
	}

	.card-front,
	.card-back {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;

		-webkit-backface-visibility: hidden;
		backface-visibility: hidden;

		// An element without a 3D transform is rendered as part of its
		// parent element's plane, meaning backface-visibility doesn't
		// apply!
		transform: translate3d(0, 0, 0);
	}

	.card-back {
		transform: rotateY(180deg) translateZ(-1px);
	}

	:global(:hover),
	:global(:focus-visible) {
		& > .container {
			transform: rotateY(180deg);
		}
	}

	// If hover isn't available, flip when child of a focused card.
	@media not screen and (any-hover: hover) {
		:global([data-focused-card='true']) .container {
			transform: rotateY(180deg);
		}
	}
</style>
