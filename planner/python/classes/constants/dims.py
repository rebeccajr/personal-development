from typing import Tuple

class PlannerDims:
  """
  Dimensions used in planner creation
  """

  LETTER_SIZE_LNGTH: int = 11
  LETTER_SIZE_WIDTH: int = 8.5

  BINDER_MARGIN: int = 0.75
  STD_MARGIN: int = 0.3



  #_____________________________________________________________________
  def to_in_str(dim: int) -> str:
    """
    Converts integer value to string appended with 'in'.

    Parameters:
    dim - Dimension to convert

    Returns:
    String indicating value appended with 'in'
    """
    return f'{dim}in'

  #_____________________________________________________________________
  def to_px_str(dim: int) -> str:
    """
    Converts integer value to string appended with 'px'.

    Parameters:
    dim - Dimension to convert

    Returns:
    String indicating value appended with 'px'
    """
    return f'{dim}px'

  #_____________________________________________________________________
  def calc_mid_margin_width(dbl_sided: bool) -> int:
    """
    Calculates the middle margin width. Doubles binder margin for
    double-sided print. Binder + standard margin for single-sided print.

    Parameters:
    dbl_sided - is the layout intended to be printed double-sided

    Returns:
    Width of middle margin
    """

    if (dbl_sided):
      return 2 * PlannerDims.BINDER_MARGIN

    return PlannerDims.BINDER_MARGIN + PlannerDims.STD_MARGIN

  #_____________________________________________________________________
  def calc_content_size(is_portrait: bool) -> Tuple:
    """
    Calculates the size of the content container depending on page
    orientation. Portrait orientation means that each half sheet is
    of landscape orientation.

    Parameters:
    is_portrait - is the page intended to be printed as a portrait

    Returns:
    width, height of content
    """

    Dims = PlannerDims

    long_side: int = 0.5 * (
      Dims.LETTER_SIZE_LNGTH \
      - 2 * (Dims.STD_MARGIN) \
      - 2 * (Dims.BINDER_MARGIN)
    )

    short_side: int =\
      Dims.LETTER_SIZE_WIDTH - 2 * Dims.STD_MARGIN

    if (is_portrait):
      content_hght = short_side
      content_wdth = long_side

    else:
      content_wdth = short_side
      content_hght = long_side

    return (content_wdth, content_hght)


