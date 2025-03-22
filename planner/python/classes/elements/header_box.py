import svgwrite.container
import svgwrite.shapes
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font


#_______________________________________________________________________
class HeaderBox(svgwrite.container.Group):
  """
  Container for entry table. Header is filled background.
  """

  #_____________________________________________________________________
  def __init__(self
  , wdth: int = 0
  , text_lst: str = ['header0', 'header1']
  , font_color: str = Colors.NORMAL
  , font_size: int = Font.NORMAL_SIZE
  , font: str = Font.FONT_FAMILY_NORMAL
  , box_fill_color: str = Colors.LIGHT_GREY
  , box_brdr_color: str = Colors.BORDER_COLOR
  , pad_top: bool = False
  , pad_bot: bool = False
  , pad_rgt: bool = False
  , pad_lft: bool = False
  ):

    super().__init__()

    self.wdth_: int = wdth

    self.pad_top_: bool = pad_top
    self.pad_bot_: bool = pad_bot
    self.pad_rgt_: bool = pad_rgt
    self.pad_lft_: bool = pad_lft

    self.text_lst_: str = text_lst

    self.font_color_: str = font_color
    self.font_size_: int = font_size
    self.font_: str = font

    self.box_hght_: int = self.font_size_ + 2 * Font.TEXT_PADDING
    self.hght_: int = self.box_hght_ + self.pad_top_ + self.pad_bot_

    self.box_fill_color_: str = box_fill_color
    self.box_brdr_color_: str = box_brdr_color


    if (pad_rgt):
      self.wdth_ = self.wdth_ - Dims.BRD_MARGIN_PX

    if (pad_lft):
      self.wdth_ = self.wdth_ - Dims.BRD_MARGIN_PX

    self.create_header()

    return

  #_____________________________________________________________________
  def create_header(self):
    """
    Create boxed header.
    """

    # Width of each header
    header_wdth: int = self.wdth_ / len(self.text_lst_)

    insert_box_x: int = Dims.BRD_MARGIN_PX * self.pad_lft_
    insert_box_y: int = Dims.BRD_MARGIN_PX * self.pad_top_


    header_box: svgwrite.shapes.Rect =\
      svgwrite.shapes.Rect\
      ( size=(self.wdth_, self.box_hght_)
      , insert=(insert_box_x, insert_box_y)
      , stroke=self.box_brdr_color_
      , fill=self.box_fill_color_
      )

    self.add(header_box)

    insert_txt_x: int = insert_box_x + Font.TEXT_PADDING
    insert_txt_y: int = insert_box_y + self.box_hght_ - Font.TEXT_PADDING

    for header in self.text_lst_:

      # Note: The SVG to PDF tool rsvg-convert only seems to support
      # 'text-after-edge' for alignment baseline, so this option
      # is selected to accurately render the svg to reflect how the
      # pdf will be created
      header_txt: svgwrite.text.Text =\
        svgwrite.text.Text\
        ( header
        , insert=(insert_txt_x, insert_txt_y)
        , text_anchor='start'
        , alignment_baseline='text-after-edge'
        , fill=self.font_color_
        , font_size=self.font_size_
        , font_family=self.font_
        )

      self.add(header_txt)

      insert_txt_x = insert_txt_x + Font.TEXT_PADDING + header_wdth

    return


