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
#   Driver for planner creation.
#
#   NOTES
#   All dimensions in planner are in inches.
#_______________________________________________________________________

import argparse

from classes.page_layouts.half_letter_layout import HalfLetterSize
from classes.page_layouts.day_layout import DayLayout
from classes.planner_parser import PlannerCreationParser
from classes.entries.daily_schedule import DailySchedule

#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

if __name__ == '__main__':
  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  PlannerCreationParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  layout_landscpe_no_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=False
    , is_dbl_sided=False
    )

  layout_landscpe_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=False
    , is_dbl_sided=True
    )

  layout_portrait_no_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=True
    , is_dbl_sided=False
    )

  layout_portrait_dbl_sided: HalfLetterSize =\
    HalfLetterSize\
    ( is_portrait=True
    , is_dbl_sided=True
    )

  # Generate the SVG file
  #layout_landscpe_no_dbl_sided.create_layout('landscpe.svg')
  #layout_landscpe_dbl_sided.create_layout('landscpe_dbl.svg')
  #layout_portrait_no_dbl_sided.create_layout('portrait.svg')
  #layout_portrait_dbl_sided.create_layout('portrait_dbl.svg')

  layout_test: DayLayout =\
    DayLayout\
    ( is_dbl_sided=False
    )

  layout_test.save_svg()
  print("all done")

