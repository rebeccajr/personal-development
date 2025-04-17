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
#   Entry for goal. Fills content for one half sheet.
#_______________________________________________________________________

import svgwrite.container
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font

from classes.elements.entry_table import EntryTable
from classes.elements.entry_table import NumberedTable
from classes.elements.entry_table import PromptTable
from classes.elements.header_box import HeaderBox
from classes.elements.rows import TextRowGroup

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout



#_______________________________________________________________________
class GoalEntry(OnePageHalfLetterLayout):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , padding: int = 0
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( total_hght=total_hght
      , total_wdth=total_wdth
      , padding=padding
      )

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """
    Side Effects:
      Populates self.entries_ class variable.

    Parameters:
      None

    Returns:
      None
    """

    super().create_content()

    self.entries_: list =\
    [ HeaderBox\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_CHECKLIST
      , font_size=9
      , box_brdr_color='none'
      , box_fill_color='none'
      , pad_top=True
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_ACTIONS
      , prepend_txt='[]'
      , row_count=4
      , pad_top=True
      , show_outline=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_MEASUREMENT
      , row_count=2
      , pad_top=True
      , show_outline=False
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_COST
      , row_count=2
      , pad_top=True
      , font_color=Colors.NORMAL_TXT
      , box_brdr_color='none'
      , box_fill_color='none'
      , show_outline=True
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_BENCHMARKS
      , prepend_txt=Strings.GOAL_MONTHS
      , row_count=3
      , pad_top=True
      , show_outline=True
      )

    , NumberedTable\
      ( wdth=self.content_wdth_
      , header_txt=Strings.GOAL_LIFE_IMPROVEMENT
      , row_count=2
      , pad_top=True
      , show_outline=False
      )
    ]

    # Calculate remaining height to evenly distribute spanning tables
    remaining_hght: int = self.calc_remaining_hght()

    self.entries_ = self.entries_ +\
    [ PromptTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , header_txt=Strings.GOAL_PLAN
      , pad_top=True
      )

    , PromptTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , header_txt=Strings.GOAL_REWARD
      , pad_top=True
      )
    ]

    return

  #_____________________________________________________________________
  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.GOAL_HEADER_SIZE
    font_family: str = Font.FONT_FAMILY_HEADER

    page_header =\
      TextRowGroup\
      ( text=Strings.GOAL_PAGE_HEADER
      , total_wdth=self.content_wdth_
      , font_size=font_size
      , font_family=font_family
      , show_outline=True
      , inner_pad_top=2
      , inner_pad_bot=2
      , inner_pad_lft=True
      ).text_row_group_

    return super().create_page_header\
      ( header_txt=Strings.GOAL_PAGE_HEADER
      , font_size=Font.GOAL_HEADER_SIZE
      )
