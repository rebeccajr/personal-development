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
from classes.entries.daily_schedule import DailySchedule as Sched
from classes.entries.header_box import HeaderBox
from classes.page_layouts.half_letter_layout import HalfLetterSize


#_______________________________________________________________________
class DayLayout(HalfLetterSize):
  """
  Daily entry layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , is_dbl_sided: bool = False
  , file_path: str = Strings.DEF_DAY_LAYOUT_PATH):
    """
    Constructor for class. Assumes landscape orientation.
    """
    super().__init__\
      ( is_portrait=False
      , is_dbl_sided=is_dbl_sided
      , file_path=file_path
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

    self.create_content()

    insert_sched_x: int =\
      self.insert_pt_content_0_[0]\
    + self.content_wdth_ - self.schedule_wdth_

    insert_x_px: int = insert_sched_x
    insert_y_px: int = self.insert_pt_content_0_[1]

    self.schedule_['transform'] =\
      f'translate({insert_x_px}, {insert_y_px})'

    self.page_header_['transform'] =\
      f'translate({self.insert_pt_content_0_[0]}, {self.insert_pt_content_0_[1]})'

    #self.pri_efforts_box_['transform'] =\
    #  f'translate({self.insert_pt_content_0_[0] }, {self.insert_pt_content_0_[1] + self.page_header_.hght_})'

    self.layout_dwg_.add(self.page_header_)
    #self.layout_dwg_.add(self.pri_efforts_box_)
    self.layout_dwg_.add(self.schedule_)

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """

    Side Effects:
      Populates the following class variables:
      self.schedule_

    Parameters:
      None

    Returns:
      None

    """



    # Width of daily schedule content group
    self.schedule_wdth_: int = self.content_wdth_ * 0.25
    self.schedule_hght_: int = self.content_hght_

    self.schedule_ =\
      Sched\
      ( strt_time_str = Sched.DEF_STRT_24
      , stop_time_str = Sched.DEF_STOP_24
      , wdth=self.schedule_wdth_
      , hght=self.schedule_hght_
      , time_inc_min=30
      , use_24=True
      )

    self.main_content_wdth_: int = self.content_wdth_\
      - self.schedule_.wdth_\
      - Dims.BRD_MARGIN_PX

    #self.pri_efforts_box_ =\
    # EntryTable\
    #  ( wdth=main_content_wdth_
    #  , hght=self.content_hght_
    #  , text_lst=['Primary Efforts', 'Alignment']
    #  , font_size=Font.PROMPT_SIZE
    #  , font=Font.FONT_FAMILY_PROMPT
    #  )

    self.create_page_header()
    return

  def create_page_header(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.HEAD_1_SIZE
    font_family: str = Font.FONT_FAMILY_NORMAL
    sp: str ='\u00A0\u00A0'

    days: str =\
      'Mon' + sp +\
      'Tue' + sp +\
      'Wed' + sp +\
      'Thu' + sp +\
      'Fri' + sp +\
      'Sat' + sp +\
      'Sun'

    self.page_header_ =\
      HeaderBox\
      ( wdth=self.content_wdth_
      , text_lst=[days]
      , font_size=font_size
      , font=font_family
      )

    date_str: str = '____ / ____ / 20 ____'

    insert_date_x: int = self.content_wdth_ - Font.TEXT_PADDING
    insert_date_y: int = font_size + Font.TEXT_PADDING

    date_txt: svgwrite.text.Text =\
      svgwrite.text.Text\
      ( text=date_str
      , insert=(insert_date_x, insert_date_y)
      , text_anchor='end'
      , alignment_baseline='text-after-edge'
      , fill=Colors.NORMAL
      , font_size=font_size
      , font_family=font_family
      )

    self.page_header_.add(date_txt)

    return


  #_____________________________________________________________________
  #_____________________________________________________________________

