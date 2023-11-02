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

from tkinter import *
from tkinter import ttk
from gui.styles import *
from gui import image
import paths
import os

message = f'''Usage: SALBAR [help | main | directory=[directory]]

current/specified directory: {os.getcwd()}

[-help | -h | --help | --h]:
\tdisplays all commands just by running the 'Help' window without running 'SALBAR' window

[-main | --main]:
\tset directory to the directory where SALBAR.exe is located ("{paths.get_current_path()}")
\tdefault: follows the current directory based on the specified directory

[--directory=[directory]]:
\tset directory to [directory]
\texample: SALBAR directory="{os.path.join("SALBAR", "build", "example")}"
\tdefault: follows the current directory based on the specified directory'''

root = Tk()
root.grab_set()
root.title("Help")
root.configure(bg=HELP_BACKGROUND)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
default_w = 900
default_h = 200

w = default_w
h = default_h

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

image.set_icon(root)

content = Text(root, bg=HELP_BACKGROUND, fg=TEXT_COLOR, font=FONT) #Later I want to use a font that is similar to the Windows Terminal font if possible or you can help me with the condition that you make it yourself or download it from a trusted source.
content.pack(side=LEFT, fill=BOTH, expand=True)
content.insert('end', message)
content.config(state='disabled') #read-only

#reference: https://askubuntu.com/questions/17299/what-do-the-different-colors-mean-in-ls
content.tag_configure("path", foreground="#0000ff")
content.tag_add("path", "3.29", "3.end")
content.tag_add("path", "9.62", f"9.{62+len(paths.get_current_path())}")

scrollbar = ttk.Scrollbar(root, orient='vertical', command=content.yview)
scrollbar.pack(side=RIGHT, fill=Y)

content['yscrollcommand'] = scrollbar.set

root.mainloop()