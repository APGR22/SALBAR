# Copyright © 2023 APGR22

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fontTools.ttLib import TTFont
import os
import salbar_path

BACKGROUND = "#737373"
HELP_BACKGROUND = "#000000"
FRAME_BACKGROUND = "#3c4038"
CHECKBUTTON_BOX_BACKGROUND = "#686868"
CHECKBUTTON_ACTIVE_BACKGROUND = "#ffffff"
ENTRY_BACKGROUND = "#565656"

BUTTON_WIDTH = 8
BUTTON_HEIGHT = 2
ADD_PATH_BUTTON_WIDTH = 2

TEXT_COLOR = "#ffffff"
FONT_SIZE = 10

def add_font(font_name: str, font_filename: str) -> tuple:
    if font_filename:
        TTFont(os.path.join(salbar_path.get_current_path(), "fonts", font_filename)) #https://stackoverflow.com/questions/63468751/adding-ttf-fonts-with-fonttools-in-to-tkinter
    return (font_name, FONT_SIZE)

FONT = add_font("arial", "arial.ttf") #copied from windows font #default