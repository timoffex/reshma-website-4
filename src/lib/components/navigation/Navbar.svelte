<script lang="ts">
  import type { Snippet } from 'svelte';

  interface Props {
    /**
     * An optional logo to display inside the header.
     *
     * It will be put in a div with a completely determined size
     * and overflow set to hidden. The size will be at most half
     * the main content width.
     */
    logo?: Snippet;
  }

  let { logo }: Props = $props();
</script>

<div class="navbar" class:navbar--with-logo={logo !== undefined}>
  {#if logo}
    <div class="logo">
      {@render logo()}
    </div>
  {/if}

  <div class="navbar__gap"></div>

  <h1 class="name">
    <a href="/">Reshma</a>
  </h1>
</div>

<style lang="scss">
  @use '$lib/layout/layout';

  .navbar {
    display: flex;

    font-family: 'Clearface', serif;
    font-size: 4rem;

    // When the logo is present, take up approximately half
    // the width in the Clearface font.
    &--with-logo {
      font-size: min(4rem, calc(layout.$main-content-width / 10));
    }
  }

  .navbar__gap {
    flex-grow: 1;
  }

  .logo {
    width: calc(layout.$main-content-width / 2);
    height: 1em;
    overflow: hidden;
  }

  .name {
    // Reset h1 default styles.
    font-weight: normal;
    font-size: 1em;

    // Center vertically (also overrides h1 default styling).
    margin: auto 0;

    // Remove link styling.
    & a {
      text-decoration: none;
      color: inherit;
    }
  }
</style>
