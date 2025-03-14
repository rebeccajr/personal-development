#_______________________________________________________________________
#_______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#   Copyright 2024, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#_______________________________________________________________________
#   DESCRIPTION
#   Half-letter sheet layout
#_______________________________________________________________________

import svgwrite

from typing import Tuple

from classes.constants.dims import PlannerDims as Dims
from classes.constants.style import PlannerColors as Colors


#_______________________________________________________________________
class HalfLetterSize:
  """
  Layout for half letter size prints. Intended to print two pages on
  one sheet and cut in half.
  """

  #_____________________________________________________________________
  def __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_path: str = 'layout.svg'
  ):

    self.is_portrait_: bool   = is_portrait
    self.is_dbl_sided_: bool  = is_dbl_sided
    self.file_path_: str = file_path

    self.layout_dwg_ = self.create_dwg()

    self.content_wdth_, self.content_hght_ =\
       Dims.calc_content_size(self.is_portrait_)

    self.content_wdth_str_: int = Dims.to_in_str(self.content_wdth_)
    self.content_hght_str_: int = Dims.to_in_str(self.content_hght_)

    # Content insertion points for top left
    self.insert_pt_0_, self.insert_pt_1_ =\
      self.determine_insertion_pts()

    # Content insertion points as strings
    self.insert_pt_0_str_: Tuple =\
    ( Dims.to_in_str(self.insert_pt_0_[0])
    , Dims.to_in_str(self.insert_pt_0_[1])
    )

    self.insert_pt_1_str_: Tuple =\
    ( Dims.to_in_str(self.insert_pt_1_[0])
    , Dims.to_in_str(self.insert_pt_1_[1])
    )

    self.create_layout()
    self.add_content()

  #_____________________________________________________________________
  def create_dwg(self) -> svgwrite.Drawing:
    """
    Creates Drawing object with height and width of letter size paper.

    Parameters:
      None

    Returns:
      svgwrite.Drawing
    """

    hght: int = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH)
    wdth: int = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH)

    if (self.is_portrait_):
      hght = Dims.to_in_str(Dims.LETTER_SIZE_LNGTH)
      wdth = Dims.to_in_str(Dims.LETTER_SIZE_WIDTH)

    return svgwrite.Drawing(self.file_path_
      , profile='tiny'
      , size=(wdth, hght)
    )

  #_____________________________________________________________________
  def save_svg(self) -> None:
    """
    Saves layout as svg file.

    Parameters:
      None

    Returns:
      None
    """
    self.layout_dwg_.save()

  #_____________________________________________________________________
  def create_layout(self) -> None:
    """
    Parameters:
      file_path: resulting svg path

    Returns:
      None
    """

    content_box_0: svgwrite.shapes.Rect =\
      self.create_content_box(self.insert_pt_0_str_)

    content_box_1: svgwrite.shapes.Rect =\
      self.create_content_box(self.insert_pt_1_str_)

    self.layout_dwg_.add(content_box_0)
    self.layout_dwg_.add(content_box_1)

  #_____________________________________________________________________
  def determine_insertion_pts(self) -> Tuple:
    """
    Determines top left insertion points for content boxes.

    Returns:
    Tuple of tuples
    ((x_content_box0, y_content_box0), (x_content_box1, y_content_box1))
    """

    content_wdth, content_hght =\
      Dims.calc_content_size(self.is_portrait_)

    if (self.is_portrait_):
      insert_pos00 = Dims.STD_MARGIN
      insert_pos01 = Dims.BND_MARGIN

      insert_pos10 = Dims.STD_MARGIN
      insert_pos11 = content_hght\
        + Dims.STD_MARGIN\
        + 2 * Dims.BND_MARGIN

      if (self.is_dbl_sided_):
        insert_pos01 = Dims.STD_MARGIN

    else:
      insert_pos00 = Dims.BND_MARGIN
      insert_pos01 = Dims.STD_MARGIN
      insert_pos11 = Dims.STD_MARGIN

      insert_pos10 = content_wdth\
        + Dims.STD_MARGIN\
        + 2 * Dims.BND_MARGIN

      if (self.is_dbl_sided_):
        insert_pos00 = Dims.STD_MARGIN

    insert_pos0: Tuple = (insert_pos00, insert_pos01)
    insert_pos1: Tuple = (insert_pos10, insert_pos11)

    return(insert_pos0, insert_pos1)

  #_____________________________________________________________________
  def create_content_box(self
  , insert_position: Tuple
  ) -> svgwrite.shapes.Rect:
    """
    Creates rectangle that will contain content.

    Parameters:

    Returns:
      svgwrite rectangle the size of the content
    """
    size: Tuple = Dims.calc_content_size(self.is_portrait_)
    w: str = Dims.to_in_str(size[0])
    h: str = Dims.to_in_str(size[1])

    content_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect(size=(w, h)
      , id="flux"
      , insert=insert_position
      , stroke=Colors.MEDIUM_GREY
      , fill='none')

    return content_box

  #_____________________________________________________________________
  def add_content(self) -> None:
    return
