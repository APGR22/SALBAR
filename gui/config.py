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
from gui.styles import *
import platform

def gaya_label(obj: Label):
    obj.config(bg=BACKGROUND, fg=TEXT_COLOR, font=FONT)

def gaya_tombol(obj: Label, callable: object | bool, *args: tuple, **option):
    """jika sudah berada di *args, maka bebas menambahkan apa saja, kecuali **pilihan"""

    DEFAULT_FOREGROUND = '#ffffff'
    DEFAULT_BACKGROUND = '#4b4b4b'
    EVENT_CLICK_FOREGROUND = '#ffffff'
    EVENT_CLICK_BACKGROUND = '#1f1f1f'
    HIGHLIGHT_BACKGROUND = "#929292"

    global clicked
    clicked = False

    obj.config(fg=DEFAULT_FOREGROUND, bg=DEFAULT_BACKGROUND, highlightthickness=1, highlightbackground=HIGHLIGHT_BACKGROUND, height=BUTTON_HEIGHT, font=FONT)
    try:
        obj.config(width=option["my_width"])
    except:
        obj.config(width=BUTTON_WIDTH)
    def click(event):
        obj.config(fg=EVENT_CLICK_FOREGROUND, bg=EVENT_CLICK_BACKGROUND)
    def release(event):
        obj.config(fg=DEFAULT_FOREGROUND, bg=DEFAULT_BACKGROUND)
        if clicked:
            try:
                if callable and args:
                    option["thread"](target = callable, args = args).start()
                elif callable:
                    option["thread"](target = callable).start()
            except:
                if callable and args:
                    callable(*args)
                elif callable:
                    callable()
    def cursor_enter(event):
        global clicked
        clicked = True
    def cursor_exit(event):
        global clicked
        clicked = False
    obj.bind("<Enter>", cursor_enter) #kursor mengenainya
    obj.bind("<Leave>", cursor_exit) #kursor meninggalkannya
    obj.bind("<ButtonPress-1>", click) #Button-1==tombol berubah tapi ketika kursor meninggalkannya
    obj.bind("<ButtonRelease-1>", release) #ButtonRelease-1==tombol semula setelah ditekan

def gaya_tombol_cek(obj: Checkbutton, var: IntVar):
    obj.config(variable=var, onvalue=1, offvalue=0, bg=BACKGROUND, activebackground=CHECKBUTTON_ACTIVE_BACKGROUND, fg=TEXT_COLOR, font=FONT, selectcolor=CHECKBUTTON_BOX_BACKGROUND, highlightthickness=0)

def gaya_entry(obj: Entry, var: StringVar, nama: bool = False, jendela: Toplevel = False, **more_obj):
    obj.config(textvariable=var, bg=ENTRY_BACKGROUND, fg=TEXT_COLOR, font=FONT, highlightthickness=0)

    if nama and jendela:
        #"https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names"
        if platform.system() == "Windows":
            karakter = '\\/:*?"<>|'

            def tandai():
                if obj.get().startswith(" "):
                    more_obj["label_name"].config(bg="#ff0000")
                else:
                    more_obj["label_name"].config(bg="#4b4b4b")
                jendela.after(10, tandai)
            
            tandai()

        elif platform.system() == "Linux":
            karakter = "/"
        else: #Darwin
            karakter = ":" #only for filename
        def pilihan_karakter(S):
            if len(S) == 1:
                if S in karakter: #kalau mengetikkan karakter yang dilarang
                    jendela.bell()
                    return False
            else:
                for i in karakter:
                    if i in S: #kalau menempel teks yang terdapat karakter yang dilarang
                        jendela.bell()
                        return False
            return True
        batas_karakter = (jendela.register(pilihan_karakter), '%S')
        obj.config(validate="key", validatecommand=batas_karakter)

    def selected(event):
        obj.selection_range(0, END)
        obj.config(highlightthickness=1)
    
    def deselected(event):
        obj.config(highlightthickness=0)
    
    obj.bind("<FocusIn>", selected)
    obj.bind("<FocusOut>", deselected)