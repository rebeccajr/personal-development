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
#   Entry for a blank page with page header.
#_______________________________________________________________________

import svgwrite.container

from classes.constants.addl_arg_keys import AddlArgKeys as Key
from classes.constants.strings import PlannerStrings as Strings
from classes.elements.row_group import DualLineRowGroup

from classes.page_layouts.half_letter_layout import OnePageHalfLetterLayout
from classes.elements.row_group import TextRowGroup
from classes.style.std_styles import StdTextBoxStyles

class AceStrings:
  """
  Strings used in the ACE Reference page.
  """

  PAGE_HEADER_TXT: str =\
    'Acknowlege ' + Strings.BULLET_PT\
  + ' Connect ' + Strings.BULLET_PT\
  + ' Engage'

  ABOUT_HEADER_TXT: str =\
    'About the ACE Method'

  ABOUT: str = (
    'ACE is a method used in Acceptance and Commitment Therapy as tool '
    'to "unhook" oneself when experiencing unpleasant emotions. These '
    'feelings can trigger one to engage in behaviors and thought '
    'patterns that moves a person away from their ideal self.'
  )

  USING_HEADER_TXT: str =\
    'How it works'

  USING_DESC: str = (
    'When you experience a triggering thought or feeling, pause and '
    'fill out the worksheet as described below.'
  )

  ACKNOWLEDGE_HEADER_TXT: str =\
    'Acknowlege'
  ACKNOWLEGE_DESC: str = (
    'Reference the list of Brene Brown\'s 87 Emotions and Experiences '
    'and identify the terms that most closely represent your current '
    'state.'
  )

  CONNECT_HEADER_TXT: str =\
    'Connect'
  CONNECT_DESC: str = (
    'Connect with your physical body. Engage in one of the exercises '
    'described on the following page.'
  )

  REENGAGE_HEADER_TXT: str =\
    '(Re-)Engage'

  REENGAGE_DESC: str = (
    'After executing the connection exercise, write down what activity '
    'you choose to (re)engage with. This can be what you were doing '
    'before experiencing the trigger, or an intentional act of self '
    'Commonly understood acts of self care include going outside, '
    'physical activity, or journaling. Other acts of self care include '
    'a household chore, creating art, or starting a task you\'ve been '
    'avoiding.'
  )


#_______________________________________________________________________
class AceReference(OnePageHalfLetterLayout):
  """
  Free write layout.
  """

  #_____________________________________________________________________
  def __init__(self
  , total_hght: int = 0
  , total_wdth: int = 0
  , addl_args: dict = {Key.HEADER_TXT: ''}
  ):
    """
    Constructor for class. Assumes landscape orientation.
    """

    self.page_header_txt_: str = addl_args[Key.HEADER_TXT]

    super().__init__\
    ( total_hght=total_hght
    , total_wdth=total_wdth
    , pad_bet_elements=True
    )

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

    self.entries_: list =\
      [ TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
        , text=AceStrings.ABOUT_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.ABOUT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.LTE_BACK_HEADER_FONT
        , text=AceStrings.USING_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.USING_DESC
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
        , text=AceStrings.ACKNOWLEDGE_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.ACKNOWLEGE_DESC
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
        , text=AceStrings.CONNECT_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.CONNECT_DESC
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_W_OUTLNE
        , text=AceStrings.REENGAGE_HEADER_TXT
        )
      , TextRowGroup\
        ( total_wdth=self.content_wdth_
        , style=StdTextBoxStyles.WHT_BACK_NORMAL_FONT_NO_OUTLNE
        , text=AceStrings.REENGAGE_DESC
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

    page_header = super().create_page_header\
      ( header_txt=AceStrings.PAGE_HEADER_TXT
      )

    return page_header
