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
import _test
import configurator

def short_func(name: str, except_color: str) -> str:
    return _test.test().apply_color(configurator.config("user.yaml").get_value(name), except_color)

background = short_func("background_window", "#737373")
frame_background = short_func("background", "#3c4038")

if platform.system() == "Windows":
    messagebox_background = "#ffffff"
    messagebox_button_frame_background = "SystemButtonFace" #I know the true color is '#f0f0f0' from "https://stackoverflow.com/questions/36093839/how-to-reset-background-color-of-a-python-tkinter-button/68903355#68903355"
    messagebox_icon = os.path.join(paths.get_current_path(), "icons", "Warning.png")
else:
    messagebox_background = "#d9d9d9"
    messagebox_button_frame_background = "#d9d9d9"
    messagebox_icon = os.path.join(paths.get_current_path(), "icons", "Warning (ubuntu).png")

checkbutton_selected_foreground = short_func("foreground_checkbox_selected", "#000000")
checkbutton_selected_background = short_func("background_checkbox_selected", "#ffffff")
checkbutton_deselected_foreground = short_func("foreground_checkbox_deselected", "#ffffff")
checkbutton_deselected_background = short_func("background_checkbox_deselected", "#686e61")

HELP_BACKGROUND = "#000000"
CHECKBUTTON_BOX_BACKGROUND = "#686868"
CHECKBUTTON_ACTIVE_BACKGROUND = "#ffffff"
ENTRY_BACKGROUND = "#565656"
PROGRESS_BACKGROUND = "#535353"
PROGRESS_FOREGROUND = "#ffffff"

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