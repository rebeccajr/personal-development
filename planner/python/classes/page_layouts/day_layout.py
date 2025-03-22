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

from classes.page_layouts.half_letter_layout import TwoPageHalfLetterSize
from classes.page_layouts.half_letter_layout import TwoPageHalfLetterSize_
from classes.page_layouts.day_entry import DayEntry


#_______________________________________________________________________
class DayLayout(TwoPageHalfLetterSize):
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
    super().add_content()

    #___________________________________________________________________
    sched_insert_x: int = self.insert_pt_content_0_[0]\
      + self.content_wdth_\
      - self.schedule_wdth_\
      + Dims.BRD_MARGIN_PX * self.sched_.pad_lft_

    sched_insert_y: int = self.insert_pt_content_0_[1]\

    self.sched_['transform'] =\
      f'translate({sched_insert_x},{sched_insert_y})'

    #___________________________________________________________________
    # Entry insert calculations
    #___________________________________________________________________
    insert_x: int = self.insert_pt_content_0_[0]
    insert_y: int = self.insert_pt_content_0_[1]
    #___________________________________________________________________
    self.pri_efforts_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.pri_efforts_.total_hght_
    #___________________________________________________________________
    self.checklist_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.checklist_.total_hght_
    #___________________________________________________________________
    self.focus_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.focus_.total_hght_
    #___________________________________________________________________
    self.todo_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.todo_.total_hght_
    #___________________________________________________________________
    self.gratitude_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.gratitude_.total_hght_
    #___________________________________________________________________
    self.prompt0_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.prompt0_.total_hght_
    #___________________________________________________________________
    self.prompt1_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.prompt1_.total_hght_
    #___________________________________________________________________
    self.prompt2_['transform'] =\
      f'translate({insert_x},{insert_y})'

    insert_y: int = insert_y\
      + self.prompt2_.total_hght_
    #___________________________________________________________________

    self.test_=svgwrite.container.Group()

    self.test_.add(self.sched_)
    self.test_.add(self.pri_efforts_)
    self.test_.add(self.checklist_)
    self.test_.add(self.focus_)
    self.test_.add(self.todo_)
    self.test_.add(self.gratitude_)
    self.test_.add(self.prompt0_)
    self.test_.add(self.prompt1_)
    self.test_.add(self.prompt2_)

    self.layout_dwg_.add(self.test_)

    return

  #_____________________________________________________________________
  def create_content(self) -> None:
    """

    Side Effects:
      Populates the following class variables:
      self.sched_

    Parameters:
      None

    Returns:
      None

    """

    super().create_content()

    # Width of daily schedule content group
    self.schedule_wdth_: int = self.content_wdth_ * 0.25
    self.main_content_wdth_: int =\
      self.content_wdth_ - self.schedule_wdth_

    self.sched_: DaySched =\
      DaySched\
      ( wdth=self.schedule_wdth_
      , hght=self.content_hght_0_
      , time_inc_min=30
      , use_24=True
      )

    self.pri_efforts_: EntryTable =\
      EntryTable\
      ( wdth=self.main_content_wdth_
      , hght=100
      , text_lst=Strings.DAY_PRIMARY_EFFORTS
      , entry_row_count=4
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    self.checklist_: HeaderBox=\
      HeaderBox\
      ( wdth=self.main_content_wdth_
      , text_lst=Strings.DAY_CHECKLIST
      , box_brdr_color='none'
      , box_fill_color='none'
      , pad_top=True
      , pad_rgt=True
      )

    self.focus_: EntryTable =\
      EntryTable\
      ( wdth=self.main_content_wdth_
      , hght=50
      , text_lst=[Strings.DAY_FOCUS]
      , entry_row_count=1
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    self.todo_: EntryTable =\
      EntryTable\
      ( wdth=self.main_content_wdth_
      , hght=100
      , text_lst=['To Do']
      , entry_row_count=4
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    self.gratitude_: EntryTable =\
      EntryTable\
      ( wdth=self.main_content_wdth_
      , hght=50
      , text_lst=[Strings.DAY_GRATITUDE]
      , entry_row_count=1
      , pad_top=True
      , pad_rgt=True
      , show_outline=True
      )

    self.prompt0_: PromptTable =\
      PromptTable\
      ( wdth=self.main_content_wdth_
      , hght=100
      , txt=Strings.DAY_PROMPTS[0]
      , entry_row_count=3
      , pad_top=True
      , pad_rgt=True
      )

    self.prompt1_: PromptTable =\
      PromptTable\
      ( wdth=self.main_content_wdth_
      , hght=100
      , txt=Strings.DAY_PROMPTS[1]
      , entry_row_count=3
      , pad_top=True
      , pad_rgt=True
      )

    self.prompt2_: PromptTable =\
      PromptTable\
      ( wdth=self.main_content_wdth_
      , hght=100
      , txt=Strings.DAY_PROMPTS[2]
      , entry_row_count=3
      , pad_top=True
      , pad_rgt=True
      )

    return

  #_____________________________________________________________________
  def create_page_headers(self) -> svgwrite.container.Group:
    """
    Creates page header and saves it to class variable.

    Parameters:
      None

    Returns:

    """
    font_size: int = Font.NORMAL_SIZE
    font_family: str = Font.FONT_FAMILY_NORMAL
    sp: str ='\u00A0\u00A0'

    days: str =\
      'Mon' + sp + sp +\
      'Tue' + sp + sp +\
      'Wed' + sp + sp +\
      'Thu' + sp + sp +\
      'Fri' + sp + sp +\
      'Sat' + sp + sp +\
      'Sun'

    page_header_0 = super().create_page_header\
      ( header_txt=days
      , font_size=font_size
      , font=font_family
      )

    page_header_1 = super().create_page_header\
      ( header_txt=Strings.QUOTE0
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

    page_header_0.add(date_txt)

    return page_header_0, page_header_1


#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
#_______________________________________________________________________
class OneDayLayout(TwoPageHalfLetterSize_):

  #_____________________________________________________________________
  def  __init__(self
  , is_portrait: bool = False
  , is_dbl_sided: bool = False
  , file_path: str = Strings.DEF_LAYOUT_PATH
  ):
    super().__init__\
      ( is_portrait=is_portrait
      , is_dbl_sided=is_dbl_sided
      , file_path=file_path
      )
    return

  #_____________________________________________________________________
  def create_content(self):
    super().create_content()

    self.content_0_ =\
      DayEntry\
      ( total_hght=self.content_hght_
      , total_wdth=self.content_wdth_
      , padding=Dims.BRD_MARGIN_PX
      )

    return

  #_____________________________________________________________________
  def add_content(self):
    super().add_content()
