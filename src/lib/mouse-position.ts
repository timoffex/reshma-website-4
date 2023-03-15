import { readable } from "svelte/store";

export const mousePosition = readable<{x: number, y: number}|undefined>(
  undefined,
  (set) => {
    function handler(evt: MouseEvent) {
      set({x: evt.clientX, y: evt.clientY});
    }

    addEventListener('mousemove', handler);
    return () => removeEventListener('mousemove', handler);
  });
