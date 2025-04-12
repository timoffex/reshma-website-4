Sveltekit + Firebase implementation for https://reshma.page/.

I originally started with plain HTML and CSS files (not in this repository's
git history), wanting to keep it simple, but the JS code for even a little bit
of interactivity was too ugly. The files were also growing too large to
maintain, so I moved to React, using Parcel as the build system (not in this
repository's git history).

React is great, but then I wanted to try Svelte, so I rewrote the app. This
also gave me an opportunity to structure the code a little better, which was
a plus. And it turns out Vite is way better than Parcel (which is way better
than Webpack, which was my previous experience).

## Developing

Once, at the beginning: `npm install`

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open

# generate static/images/ directory from images/
python tools/create_images.py
```

## Building

```bash
npm run build
```

## Deploying

First, log in to Firebase

```bash
firebase login  # `--reauth` to force 
```

After building:

```bash
# To a temporary URL:
firebase hosting:channel:deploy dev

# To prod:
firebase deploy
```

## Project overview

### Structure

All the code for the website lives under [src](src). It is a SvelteKit project
and is [structured as such](https://svelte.dev/docs/kit/project-structure).

The [src/lib/components](src/lib/components) folder is for unique,
non-reusable parts of the website, like entire subpages or tiles on
the home page grid. Page components are referenced directly by [src/routes](src/routes)
files which correspond to different subpages on the site (`/`, `/wetransfer`,
`/music`, etc.).

The [src/lib/widgets](src/lib/widgets) folder is for general,
potentially-reusable parts of the website. Many widgets here are only used once,
but they're not specific to the portfolio site, so they don't count as
"components".

### Styling

[global-defaults.scss](src/lib/global-defaults.scss) contains global styles
that are included on every page.

[global.scss](src/lib/global.scss) contains globally-available CSS classes,
sort of like Tailwind. I want this to be like a project-specific design
vocabulary, which is read and understood in its entirety and hence isn't
broken into multiple files.

[layout-styles.scss](src/lib/layout/layout-styles.scss) contains
globally-available CSS classes for _layout_ purposes. Mainly, it defines
the "main-content" area which is reused by all pages, and the grid on
the home page which could in theory be reused by some pages.

The `main-content` CSS class uses a calculation with `rem`, `vw` and `px` units
to scale responsively, and most layout-related styling builds on top of that
logic. The [layout.scss](src/lib/layout/layout.scss) and [layout.ts](src/lib/layout/layout.ts)
files are reusable Sass and TypeScript versions of layout-related constants
and calculations.
