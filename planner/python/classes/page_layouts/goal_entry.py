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
#   Layout for daily entry.
#_______________________________________________________________________

import svgwrite.container
import svgwrite.text

from classes.constants.dims import PlannerDims as Dims
from classes.constants.strings import PlannerStrings as Strings
from classes.constants.style import PlannerColors as Colors
from classes.constants.style import PlannerFontStyle as Font

from classes.elements.daily_schedule import DaySchedule as DaySched
from classes.elements.entry_table import EntryTable
from classes.elements.entry_table import PromptTable
from classes.elements.header_box import HeaderBox

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
  def add_content(self) -> None:
    """
    Add content to layout.

    Parameters:
      None

    Returns:
      None
    """
    super().add_content()

    insert_x: int = self.content_insert_pt_x_
    insert_y: int = self.content_insert_pt_y_

    for entry in self.entries_:

      entry['transform'] =\
      f'translate({insert_x},{insert_y})'

      insert_y = insert_y + entry.total_hght_

      self.add(entry)

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """

    Side Effects:
      Populates the following class variables.

    Parameters:
      None

    Returns:
      None
    """

    super().create_content()

    self.entries_: list =\
    [ HeaderBox\
      ( wdth=self.content_wdth_
      , text_lst=[Strings.GOAL_CHECKLIST]
      , font_size=9
      , box_brdr_color='none'
      , box_fill_color='none'
      , pad_top=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , text_lst=[Strings.GOAL_ACTIONS]
      , entry_row_count=7
      , pad_top=True
      , show_outline=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , text_lst=[Strings.GOAL_MEASUREMENT]
      , entry_row_count=2
      , pad_top=True
      , show_outline=False
      )

    , PromptTable\
      ( wdth=self.content_wdth_
      , txt=Strings.GOAL_COST
      , entry_row_count=3
      , pad_top=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , text_lst=[Strings.GOAL_BENCHMARKS]
      , entry_row_count=5
      , pad_top=True
      , show_outline=True
      )

    , EntryTable\
      ( wdth=self.content_wdth_
      , text_lst=[Strings.GOAL_LIFE_IMPROVEMENT]
      , entry_row_count=4
      , pad_top=True
      , show_outline=False
      )
    ]


    # Calculate remaining height to evenly distribute spanning tables
    remaining_hght: int = self.content_hght_

    for entry in self.entries_:
      remaining_hght = remaining_hght - entry.total_hght_

    self.entries_ = self.entries_ +\
    [ PromptTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , txt=Strings.GOAL_PLAN
      , pad_top=True
      )

    , PromptTable\
      ( wdth=self.content_wdth_
      , hght=remaining_hght / 2
      , txt=Strings.GOAL_REWARD
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

    page_header = super().create_page_header\
      ( header_txt=Strings.GOAL_PAGE_HEADER
      , font_size=font_size
      , font=font_family
      )

    return page_header
