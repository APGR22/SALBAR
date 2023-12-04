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

class undo_redo:
    def __init__(self, entry: Entry):
        self.entry = entry
        self.entry.bind("<Key>", self.add)
        self.entry.bind("<Control-Z>", self.undo)
        self.entry.bind("<Control-z>", self.undo)
        self.entry.bind("<Control-Y>", self.redo)
        self.entry.bind("<Control-y>", self.redo)
        self.changed = {0: self.entry.get()} #0 = default. 0 ini tidak dapat diubah
        self.position = {0: self.entry.index(INSERT)}
        self.current = 0 #ditambah berarti redo atau add. tidak mungkin akan 0 seandainya ditambah

    def add(self, *event):
        if self.entry.get() != self.changed[self.current]: #if changed
            total = len(self.changed)-1
            for count_redo in range(total - self.current): #get total redo
                self.changed.pop(total - count_redo)
                self.position.pop(total - count_redo)

            #add a new change
            self.current += 1
            self.changed[self.current] = self.entry.get()
            self.position[self.current] = self.entry.index(INSERT)

    def update(self):
        text = self.changed[self.current]
        self.entry.delete(0, END)
        self.entry.insert(0, text)

        self.entry.icursor(self.position[self.current])

        total = len(self.entry.get())
        if total > 0:
            self.entry.xview_moveto(self.position[self.current]/total - (50/total))

    def undo(self, *event):
        if self.current > 0: #jika tidak di awal
            self.current -= 1
            self.update()

    def redo(self, *event):
        if self.current < len(self.changed)-1: #jika tidak di akhir
            self.current += 1
            self.update()

def label(obj: Label):
    obj.config(bg=background, fg=TEXT_COLOR, font=default_font)

def button(obj: Label, callable: object | bool, *args: tuple, **option):
    """jika sudah berada di *args, maka bebas menambahkan apa saja, kecuali **pilihan"""

    DEFAULT_FOREGROUND = '#ffffff'
    DEFAULT_BACKGROUND = '#4b4b4b'
    EVENT_CLICK_FOREGROUND = '#ffffff'
    EVENT_CLICK_BACKGROUND = '#1f1f1f'

    global clicked
    clicked = False

    obj.config(fg=DEFAULT_FOREGROUND, bg=DEFAULT_BACKGROUND, highlightthickness=0, highlightbackground=background, height=BUTTON_HEIGHT, font=default_font)
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
    obj.pack(padx=1)

def checkbutton(obj: Checkbutton, var: IntVar):
    obj.config(variable=var, onvalue=1, offvalue=0, bg=background, activebackground=CHECKBUTTON_ACTIVE_BACKGROUND, fg=TEXT_COLOR, font=default_font, selectcolor=CHECKBUTTON_BOX_BACKGROUND, highlightthickness=0)

def radiobutton(obj: Radiobutton, var: IntVar | StringVar, value: int | str, tristatevalue: int | str = None):
    "if tristate is none, then set it to value"
    if tristatevalue is None:
        tristatevalue = value
    obj.config(variable=var, value=value, tristatevalue=tristatevalue, bg=background, activebackground=CHECKBUTTON_ACTIVE_BACKGROUND, fg=TEXT_COLOR, font=default_font, selectcolor=CHECKBUTTON_BOX_BACKGROUND, highlightthickness=0)

def entry(obj: Entry, var: StringVar, nama: bool = False, **more_obj):
    obj.config(textvariable=var, bg=ENTRY_BACKGROUND, fg=TEXT_COLOR, font=default_font, highlightthickness=0)

    if nama:
        #"https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names"
        if platform.system() == "Windows":
            karakter = '\\/:*?"<>|'

            def tandai():
                if obj.get().startswith(" "):
                    more_obj["label_name"].config(bg="#ff0000")
                else:
                    more_obj["label_name"].config(bg="#4b4b4b")
                obj.master.after(10, tandai)
            
            tandai()

        elif platform.system() == "Linux":
            karakter = "/"
        else: #Darwin
            karakter = ":" #only for filename
        def pilihan_karakter(S):
            if len(S) == 1:
                if S in karakter: #kalau mengetikkan karakter yang dilarang
                    obj.master.bell()
                    return False
            else:
                for i in karakter:
                    if i in S: #kalau menempel teks yang terdapat karakter yang dilarang
                        obj.master.bell()
                        return False
            return True
        batas_karakter = (obj.master.register(pilihan_karakter), '%S')
        obj.config(validate="key", validatecommand=batas_karakter)

    scrollbar_entry = Scrollbar(obj.master, orient=HORIZONTAL, command=obj.xview, width=8, relief=FLAT, highlightthickness=0)
    obj.configure(xscrollcommand=scrollbar_entry.set)

    def selected(event):
        obj.selection_range(0, END)

        scrollbar_entry.pack(side=BOTTOM, fill=X, in_=obj)

    def deselected(event):
        scrollbar_entry.pack_forget()

    obj.bind("<FocusIn>", selected)
    obj.bind("<FocusOut>", deselected)

    undo_redo(obj)