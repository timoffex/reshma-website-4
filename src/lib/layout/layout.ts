const spacingPx = 8;

const gridACols = 6;
const gridBCols = 4;

const gridGapLength = `${spacingPx}px`;
const mainMaximizedMarginX = `${2 * spacingPx}px`;


const gridColumnWidthCalc = (numCols: number, mainWidthCalc: string) => {
  // Keep in sync with layout-styles.scss
  return `((${mainWidthCalc}) - ${gridGapLength} * (${numCols} - 1)) / ${numCols}`;
};


const gridSizesList = (colsInSubgrid: number, cols: number) => {
  const gridGaps = `${cols - 1}*${gridGapLength}`;
  const columnWidthCalc = (mainWidthCalc: string) => gridColumnWidthCalc(colsInSubgrid, mainWidthCalc);

  // If width > 45rem+16px, then each column can be expressed in rem units.
  const colRemsCalculation = `calc(${cols} * (${columnWidthCalc('45rem')}) + ${gridGaps})`;

  // Otherwise, each column can be expressed in vw units. 
  const colVwsCalculation = `calc(${cols} * (${columnWidthCalc(`100vw - ${mainMaximizedMarginX}`)}) + ${gridGaps})`;

  return `(min-width: calc(45rem + 16px)) ${colRemsCalculation},` +
    ` ${colVwsCalculation}`;
};


export const gridASizesList = (cols: number) => gridSizesList(gridACols, cols);
export const gridBSizesList = (cols: number) => gridSizesList(gridBCols, cols);
