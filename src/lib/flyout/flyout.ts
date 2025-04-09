import { getContext, setContext } from 'svelte';
import { writable, type Writable } from 'svelte/store';

const currentFlyoutIdSymbol = Symbol();

export const setupFlyoutContext = () => {
  setContext(currentFlyoutIdSymbol, writable(undefined));
};

export const getFlyout = (): Writable<string | undefined> => {
  return getContext(currentFlyoutIdSymbol);
};
