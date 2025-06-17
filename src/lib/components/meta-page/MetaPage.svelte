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
        image={MetaBlueprint}
        alt="Meta"
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

    <p class="text-align-right text-small">
      Client: Meta Blueprint<br />
      Agency: IntraEdge<br />
      Art Director: Josh Koll<br />
    </p>
  </div>

  <div class="videos">
    <iframe
      class="video-rounded-border"
      width="420"
      height="746"
      src="https://www.youtube.com/embed/XN7TSbna3UU"
      title="Getting Started with Reels Ads 1"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
    <iframe
      class="video-rounded-border"
      width="420"
      height="746"
      src="https://www.youtube.com/embed/QSduabwjF0c"
      title="How to Create Reels Ads 2"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
    <iframe
      class="video-rounded-border"
      width="420"
      height="746"
      src="https://www.youtube.com/embed/7vvIyt2opao"
      title="How To Improve Your Ads on Facebook and IG Reels 3"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
    <iframe
      width="420"
      height="746"
      src="https://www.youtube.com/embed/71vOfNC7rAM"
      title="Using Different Types of Reels 4"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
    <iframe
      width="420"
      height="746"
      src="https://www.youtube.com/embed/2kqld3QaMr8"
      title="How to structure reels ads 5"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
  </div>
</div>

<style lang="scss">
  @use '$lib/layout/layout';

  .videos {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    gap: layout.$spacing;
  }

  .video-rounded-border {
    border: 1px solid black;
    border-radius: layout.$spacing;
  }
</style>
