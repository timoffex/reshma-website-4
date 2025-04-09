<script lang="ts">
  import EyeballImage from './eyeball.png';

  import { onMount } from 'svelte';
  import { Spring } from 'svelte/motion';

  interface Props {
    lookAt: { x: number; y: number } | undefined;
  }

  let { lookAt }: Props = $props();

  let eyeballContainer: HTMLElement | undefined = $state();

  const offset = new Spring({ x: 0, y: 0 });

  onMount(() => {
    let interval = setInterval(() => {
      if (!lookAt) return;

      const rect = eyeballContainer!.getBoundingClientRect();
      const centerX = rect.x + rect.width / 2;
      const centerY = rect.y + rect.height / 2;

      let diffX = lookAt.x - centerX;
      let diffY = lookAt.y - centerY;

      const m2 = diffX * diffX + diffY * diffY;

      const maxOffset = rect.height * 0.19;
      if (m2 > maxOffset * maxOffset) {
        const m = Math.sqrt(m2);
        diffX *= maxOffset / m;
        diffY *= maxOffset / m;
      }

      offset.set({
        x: diffX,
        y: diffY
      });
    }, 50);

    return () => clearInterval(interval);
  });
</script>

<div class="container" bind:this={eyeballContainer}>
  <img src={EyeballImage} alt="" class="eyeball" />
  <svg
    viewBox="0 0 100 100"
    xmlns="http://www.w3.org/2000/svg"
    class="iris"
    style="transform: translate({offset.current.x}px, {offset.current.y}px)"
  >
    <circle cx="50" cy="50" r="50" fill="black" />
  </svg>
</div>

<style lang="scss">
  .container {
    position: relative;
    aspect-ratio: 1;
  }

  .eyeball {
    display: block;

    object-fit: contain;
    width: 100%;
    height: 100%;
  }

  .iris {
    position: absolute;
    top: 20%;
    left: 20%;
    width: 60%;
    height: 60%;
  }
</style>
