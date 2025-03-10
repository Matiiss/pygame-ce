/* Auto generated file: with make_docs.py .  Docs go in docs/reST/ref/ . */
#define DOC_MASK "pygame module for image masks."
#define DOC_MASK_FROMSURFACE "from_surface(surface) -> Mask\nfrom_surface(surface, threshold=127) -> Mask\nCreates a Mask from the given surface"
#define DOC_MASK_FROMTHRESHOLD "from_threshold(surface, color) -> Mask\nfrom_threshold(surface, color, threshold=(0, 0, 0, 255), othersurface=None, palette_colors=1) -> Mask\nCreates a mask by thresholding Surfaces"
#define DOC_MASK_MASK "Mask(size=(width, height)) -> Mask\nMask(size=(width, height), fill=False) -> Mask\npygame object for representing 2D bitmasks"
#define DOC_MASK_MASK_COPY "copy() -> Mask\nReturns a new copy of the mask"
#define DOC_MASK_MASK_GETSIZE "get_size() -> (width, height)\nReturns the size of the mask"
#define DOC_MASK_MASK_GETRECT "get_rect(**kwargs) -> Rect\nReturns a Rect based on the size of the mask"
#define DOC_MASK_MASK_GETAT "get_at(pos) -> int\nGets the bit at the given position"
#define DOC_MASK_MASK_SETAT "set_at(pos) -> None\nset_at(pos, value=1) -> None\nSets the bit at the given position"
#define DOC_MASK_MASK_OVERLAP "overlap(other, offset) -> (x, y)\noverlap(other, offset) -> None\nReturns the point of intersection"
#define DOC_MASK_MASK_OVERLAPAREA "overlap_area(other, offset) -> numbits\nReturns the number of overlapping set bits"
#define DOC_MASK_MASK_OVERLAPMASK "overlap_mask(other, offset) -> Mask\nReturns a mask of the overlapping set bits"
#define DOC_MASK_MASK_FILL "fill() -> None\nSets all bits to 1"
#define DOC_MASK_MASK_CLEAR "clear() -> None\nSets all bits to 0"
#define DOC_MASK_MASK_INVERT "invert() -> None\nFlips all the bits"
#define DOC_MASK_MASK_SCALE "scale((width, height)) -> Mask\nResizes a mask"
#define DOC_MASK_MASK_DRAW "draw(other, offset) -> None\nDraws a mask onto another"
#define DOC_MASK_MASK_ERASE "erase(other, offset) -> None\nErases a mask from another"
#define DOC_MASK_MASK_COUNT "count() -> bits\nReturns the number of set bits"
#define DOC_MASK_MASK_CENTROID "centroid() -> (x, y)\nReturns the centroid of the set bits"
#define DOC_MASK_MASK_ANGLE "angle() -> theta\nReturns the orientation of the set bits"
#define DOC_MASK_MASK_OUTLINE "outline() -> [(x, y), ...]\noutline(every=1) -> [(x, y), ...]\nReturns a list of points outlining an object"
#define DOC_MASK_MASK_CONVOLVE "convolve(other) -> Mask\nconvolve(other, output=None, offset=(0, 0)) -> Mask\nReturns the convolution of this mask with another mask"
#define DOC_MASK_MASK_CONNECTEDCOMPONENT "connected_component() -> Mask\nconnected_component(pos) -> Mask\nReturns a mask containing a connected component"
#define DOC_MASK_MASK_CONNECTEDCOMPONENTS "connected_components() -> [Mask, ...]\nconnected_components(minimum=0) -> [Mask, ...]\nReturns a list of masks of connected components"
#define DOC_MASK_MASK_GETBOUNDINGRECTS "get_bounding_rects() -> [Rect, ...]\nReturns a list of bounding rects of connected components"
#define DOC_MASK_MASK_TOSURFACE "to_surface() -> Surface\nto_surface(surface=None, setsurface=None, unsetsurface=None, setcolor=(255, 255, 255, 255), unsetcolor=(0, 0, 0, 255), dest=(0, 0)) -> Surface\nReturns a surface with the mask drawn on it"
