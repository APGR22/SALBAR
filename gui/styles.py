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
import paths
import platform

BACKGROUND = "#737373"
HELP_BACKGROUND = "#000000"
FRAME_BACKGROUND = "#3c4038"
CHECKBUTTON_BOX_BACKGROUND = "#686868"
CHECKBUTTON_ACTIVE_BACKGROUND = "#ffffff"
ENTRY_BACKGROUND = "#565656"
if platform.system() == "Windows":
    MESSAGEBOX_BACKGROUND = "#ffffff"
    MESSAGEBOX_BUTTON_FRAME_BACKGROUND = "SystemButtonFace" #I know the true color is '#f0f0f0' from "https://stackoverflow.com/questions/36093839/how-to-reset-background-color-of-a-python-tkinter-button/68903355#68903355"
    MESSAGEBOX_ICON = os.path.join(paths.get_current_path(), "icons", "Warning.png")
else:
    MESSAGEBOX_BACKGROUND = "#d9d9d9"
    MESSAGEBOX_BUTTON_FRAME_BACKGROUND = "#d9d9d9"
    MESSAGEBOX_ICON = os.path.join(paths.get_current_path(), "icons", "Warning (ubuntu).png")

BUTTON_WIDTH = 8
BUTTON_HEIGHT = 2
ADD_PATH_BUTTON_WIDTH = 2

TEXT_COLOR = "#ffffff"
FONT_SIZE = 10

def add_font(font_filename: str) -> tuple:
    font = TTFont(os.path.join(paths.get_current_path(), "fonts", font_filename)) #https://stackoverflow.com/questions/63468751/adding-ttf-fonts-with-fonttools-in-to-tkinter
    return (font, FONT_SIZE)

FONT = add_font("arial.ttf") #copied from windows font #default
JUST_FONT = FONT[0]