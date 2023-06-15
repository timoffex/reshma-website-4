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
