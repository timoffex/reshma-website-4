<script lang="ts">
  import type { Snippet } from 'svelte';

  interface Props {
    animationSeconds: number;
    children?: Snippet;
  }

  let { animationSeconds, children }: Props = $props();
</script>

<div class="marquee" style="--animation-duration: {animationSeconds}s;">
  <div class="marquee__text">{@render children?.()}</div>
  <div class="marquee__text" aria-hidden="true">{@render children?.()}</div>
</div>

<style>
  .marquee {
    display: flex;
    overflow: hidden;
    position: relative;
    user-select: none;

    --animation-duration: 10s;
  }

  .marquee__text {
    flex-shrink: 0;
    min-width: 100%;
    animation: var(--animation-duration) linear infinite scroll;
  }

  @keyframes scroll {
    from {
      transform: translateX(0);
    }

    to {
      transform: translateX(-100%);
    }
  }
</style>
