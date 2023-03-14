import { writable } from "svelte/store";

export const currentFlyoutId = writable<string|undefined>(undefined);
