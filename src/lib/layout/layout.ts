export const spacingPx = 8;

const gridACols = 6;
const gridBCols = 4;

const gridGapLength = `${spacingPx}px`;
const mainMaximizedMarginX = `${2 * spacingPx}px`;
const mainMaxWidth = '55rem';

const gridColumnWidthCalc = (numCols: number, mainWidthCalc: string) => {
  // Keep in sync with layout-styles.scss
  return `((${mainWidthCalc}) - ${gridGapLength} * (${numCols} - 1)) / ${numCols}`;
};

const gridSizesList = (colsInSubgrid: number, cols: number) => {
  const gridGaps = `${cols - 1}*${gridGapLength}`;
  const columnWidthCalc = (mainWidthCalc: string) =>
    gridColumnWidthCalc(colsInSubgrid, mainWidthCalc);

  // If width > 45rem+16px, then each column can be expressed in rem units.
  const colRemsCalculation = `calc(${cols} * (${columnWidthCalc(mainMaxWidth)}) + ${gridGaps})`;

  // Otherwise, each column can be expressed in vw units.
  const colVwsCalculation = `calc(${cols} * (${columnWidthCalc(`100vw - ${mainMaximizedMarginX}`)}) + ${gridGaps})`;

  return (
    `(min-width: calc(${mainMaxWidth} + 16px)) ${colRemsCalculation},` +
    ` ${colVwsCalculation}`
  );
};

/** Returns a CSS expression for the width of main-content. */
export const mainContentSizeExpr = `min(${mainMaxWidth}, 100vw - ${mainMaximizedMarginX})`;

/** Returns a sizes string for a tile spanning the given number of grid A columns. */
export const gridASizesList = (cols: number) => gridSizesList(gridACols, cols);

/** Returns a sizes string for a tile spanning the given number of grid B columns. */
export const gridBSizesList = (cols: number) => gridSizesList(gridBCols, cols);
