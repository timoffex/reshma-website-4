let enteredObserver: IntersectionObserver | undefined;
let exitedObserver: IntersectionObserver | undefined;

const ATTRIBUTE = "data-fade-in-out-state";

if (typeof (window) !== 'undefined') {
    exitedObserver = new IntersectionObserver(
        (entries) => {
            for (const node of entries) {
                if (!node.isIntersecting) {
                    const above = node.boundingClientRect.bottom < 0;
                    node.target.setAttribute(ATTRIBUTE, above ? "above" : "below");
                }
            }
        },
        {
            // Run callback when target leaves viewport.
            threshold: 0.0,
        }
    )
    enteredObserver = new IntersectionObserver(
        (entries) => {
            for (const node of entries) {
                if (node.isIntersecting) {
                    node.target.removeAttribute(ATTRIBUTE);
                }
            }
        },
        {
            // Run callback when target comes in contact with area in viewport.
            rootMargin: '-100px',
            threshold: 0.0,
        }
    );
}

/** Makes an element fade in when it enters the viewport. */
export const fadeInOut = (node: HTMLElement) => {
    exitedObserver?.observe(node);
    enteredObserver?.observe(node);

    node.classList.add("animate-fade-in-out");

    return {
        destroy: () => {
            exitedObserver?.unobserve(node);
            enteredObserver?.unobserve(node);

            node.classList.remove("animate-fade-in-out");
        }
    };
};