<!-- @component Block element of a hand holding a 16x9 div. -->
<script lang="ts">
  import type { Snippet } from 'svelte';
  import HandVideoContainer from './hand-video-container.svg';

  interface Props {
    children?: Snippet;
  }

  let { children }: Props = $props();

  const WIDTH = 788.22;
  const HEIGHT = 810.88;

  const INNER_WIDTH = 720;
  const INNER_HEIGHT = 405;
  const INNER_CENTER_X = 387.6375;
  const INNER_CENTER_Y = 445.693;
  const INNER_X = INNER_CENTER_X - INNER_WIDTH / 2;
  const INNER_Y = INNER_CENTER_Y - INNER_HEIGHT / 2;

  const TOP = (100 * INNER_Y) / HEIGHT;
  const BOTTOM = 100 * (1 - (INNER_Y + INNER_HEIGHT) / HEIGHT);
  const LEFT = (100 * INNER_X) / WIDTH;
  const RIGHT = 100 * (1 - (INNER_X + INNER_WIDTH) / WIDTH);
</script>

<div style="position: relative; aspect-ratio: {WIDTH}/{HEIGHT};">
  <img style="position: absolute; inset: 0;" alt="" src={HandVideoContainer} />
  <div
    style="position: absolute;
           top: {TOP}%;
           bottom: {BOTTOM}%;
           right: {RIGHT}%;
           left: {LEFT}%;"
  >
    {@render children?.()}
  </div>
</div>
