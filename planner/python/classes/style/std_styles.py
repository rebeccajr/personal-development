from classes.style.style import PlannerColors as Colors
from classes.style.style import PlannerFontStyle as Font
from classes.constants.dims import PlannerDims as Dims

from classes.style.table_style import LineRowGroupStyle
from classes.style.table_style import TextBoxStyle


#_______________________________________________________________________
class StdTextBoxStyles():

  DRK_BACK_NORMAL_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.FLUX_BLK
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    , font_color=Colors.WHITE
    )

  DRK_BACK_HEADER_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.FLUX_BLK
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    , font_color=Colors.WHITE
    )

  MED_BACK_NORMAL_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.MEDIUM_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    , font_color=Colors.WHITE
    )

  MED_BACK_HEADER_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.MEDIUM_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    , font_color=Colors.WHITE
    )

  LTE_BACK_NORMAL_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.LIGHT_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    )

  LTE_BACK_HEADER_FONT: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color=Colors.LIGHT_GREY
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    )

  WHT_BACK_NORMAL_FONT_W_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=True
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    )

  WHT_BACK_HEADER_FONT_W_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=True
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    )

  WHT_BACK_NORMAL_FONT_NO_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=False
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_NORMAL
    )

  WHT_BACK_HEADER_FONT_NO_OUTLNE: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=False
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    )

  DEF_PAGE_HEADER: TextBoxStyle =\
    TextBoxStyle\
    ( backgnd_color='none'
    , show_outline=True
    , inner_pad_top=True
    , inner_pad_bot=True
    , inner_pad_lft=True
    , inner_pad_rgt=True
    , font_family=Font.FONT_FAMILY_HEADER
    , font_size=Font.DEF_PAGE_HEADER_SIZE
    )

#_______________________________________________________________________
class StdLineRowGroupStyles():

  PRI_LINE_FOR_DESCENDER: LineRowGroupStyle =\
    LineRowGroupStyle(y_offset=Dims.DEF_ROW_HGHT/3)

  SEC_LINE_FOR_DESCENDER: LineRowGroupStyle =\
    LineRowGroupStyle(dash_array='1,5')