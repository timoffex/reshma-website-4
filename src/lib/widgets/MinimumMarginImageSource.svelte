<!-- @component A source for hiding images based on the size of the margins.
 
The source uses a media query that causes it to be selected if the margin
outside of main-content is smaller than a given size. The source image is
completely transparent.

Meant for use inside a picture element. This is an HTML-only way of preventing
an image from downloading on narrow screens.
-->
<script lang="ts">
  import { mainContentSizeExpr } from "$lib/layout/layout";

  interface Props {
    doubleMinimumMarginExpr: string;
  }

  let { doubleMinimumMarginExpr }: Props = $props();
</script>

<source
  srcset="data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs="
  media="(max-width: calc({mainContentSizeExpr} + {doubleMinimumMarginExpr}))"
/>
