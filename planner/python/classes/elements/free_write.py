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
#   Entry for week. Fills content for one half sheet.
#_______________________________________________________________________

import svgwrite.container
import svgwrite.shapes
import svgwrite.text
import copy

from classes.constants.strings import PlannerStrings as Strings
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font

from classes.elements.entry_group import EntryRow
from classes.elements.entry_table import EntryTable
from classes.elements.entry_table import NumberedTable
from classes.elements.entry_table import PromptTable
from classes.elements.header_box import HeaderBox
from classes.elements.table_rows import TableRows
from classes.elements.table_rows import DoubleTableRows
from classes.elements.text_box import TextBox
from classes.elements.rows import RowGroup


from utils.utils import PlannerUtils as Utils

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout


#_______________________________________________________________________
class FreeWrite(OnePageHalfLetterLayout):
  """
  Free write layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  , page_header: str = ''
  , prompt: str = ''
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , padding=padding
    )

    self.page_header_: str = page_header
    self.prompt_: str      = prompt

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Parameters:
      None

    Side Effects:
      Populates self.entries_ class variable.

    Returns:
      None
    """
    super().create_content()

    row_line0: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(0,0)
        , end=(self.content_wdth_, 0)
        , stroke=Colors.CYAN
        )

    row_line1: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(0,0)
        , end=(self.content_wdth_, 0)
        , stroke=Colors.BORDER_COLOR
        )

    row_line2: svgwrite.shapes.Line =\
        svgwrite.shapes.Line\
        ( start=(0,0)
        , end=(self.content_wdth_, 0)
        , stroke=Colors.FLUX_MAG
        )




    self.entries_: list =\
    [ RowGroup\
      ( wdth=self.content_wdth_
      , total_hght=self.content_hght_/2
      , show_outline=True
      , obj_list=[row_line0, row_line1, row_line2]
      )
    ]

#[ DoubleTableRows\
    #  ( wdth=self.content_wdth_
    #  , hght=self.content_hght_
    #  , show_outline=True
    #  , row_count = 30
    #  , row_hght=TableRows.DEF_ROW_HGHT
    #  )
    #]
    #  [ TextBox\
    #    ( wdth=self.content_wdth_
    #    , hght=self.content_hght_
    #    , font=Font.FONT_FAMILY_HEADER
    #    #, show_outline=True
    #    , txt='hellllllllllooooooooo this is a bunch of text that will be split into different lines I hope this works. this is more text flux is a bunny. so is bella. trevor is a monster. duke is a dog. caitlyn is our dog sitter. my name is rebecca. I wonder if this is enough text......'
    #    )
    #  ]

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.WEEK_PAGE_HEADER_SIZE
    font_family: str = Font.FONT_FAMILY_HEADER

    page_header = super().create_page_header\
      ( header_txt=Strings.SHORT_QUOTE_0
      , font_size=font_size
      , font=font_family
      , box_fill_color=Colors.DEF_PAGE_HEADER_COLOR
      )

    return page_header
