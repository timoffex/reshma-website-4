<script>
  import Navbar from '$lib/components/navigation/Navbar.svelte';
  import { MetaBlueprint } from '$lib/generated-images';
  import { halfMainContentSizesList } from '$lib/layout/layout';
  import GeneratedImage from '$lib/widgets/GeneratedImage.svelte';
</script>

<div class="main-content">
  <Navbar>
    {#snippet logo()}
      <GeneratedImage
        imgClass="fill-contain-left"
        image={{
          alt: 'Meta',
          ...MetaBlueprint
        }}
        sizes={halfMainContentSizesList}
      />
    {/snippet}
  </Navbar>

  <div>
    <p class="text-align-center">
      I worked with the Meta Blueprint team in San Francisco to create a suite
      of 5 Instagram ready explainer videos for how to create more effective
      reels.
    </p>

    <p class="text-align-center">
      I worked under Art Director Josh Koll to create storyboards in Figma, get
      approvals from stakeholders internally, and edit the footage he filmed
      (employee UGC) into snappy, eye-catching reels.
    </p>

    <p class="text-align-center">
      <b>As part of the Business Education Creative team, I:</b>
    </p>

    <ul>
      <li>
        worked with visual designers, UX leads, and education designers to
        create animated videos for Meta Business Education
      </li>
      <li>adhered to the Meta, Facebook and Instagram brand guidelines</li>
      <li>
        created UI mocks, visual storyboards and project trackers in Figma
      </li>
      <li>
        utilized After Effects and Premiere Pro to create videos for Meta
        Blueprint
      </li>
    </ul>
  </div>
</div>

<style>
  .text-align-center {
    text-align: center;
  }
</style>
