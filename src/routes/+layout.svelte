<script lang="ts">
	import '$lib/global.scss';
	import '$lib/layout/layout-styles.scss';

	import { afterNavigate, beforeNavigate } from '$app/navigation';
	import { onMount } from 'svelte';

	/* Use smooth-scroll except when navigating between pages. */

	let root: HTMLElement;
	onMount(() => {
		root = document.getElementsByTagName('html')[0];
	});

	beforeNavigate(() => {
		root.style.scrollBehavior = 'auto';
	});

	afterNavigate(() => {
		root.style.scrollBehavior = 'smooth';
	});
</script>

<slot />
