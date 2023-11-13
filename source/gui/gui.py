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
from tkinter.filedialog import *
from gui import _options
from gui.styles import *
from gui import config

def bingkai(root: Tk):
    bingkai_utama = Frame(root)
    bingkai_utama.pack(fill=BOTH, expand=True)
    bingkai_kedua = Frame(root)
    bingkai_kedua.pack(fill=BOTH)
    kanvas = Canvas(bingkai_utama, bg=frame_background, highlightthickness=0)
    kanvas.pack(side=LEFT, fill=BOTH, expand=True)

    gulir = ttk.Scrollbar(bingkai_utama,orient=VERTICAL, command=kanvas.yview)
    gulir.pack(side=RIGHT, fill=Y)

    gulirx = ttk.Scrollbar(bingkai_kedua,orient=HORIZONTAL, command=kanvas.xview)
    gulirx.pack(side=TOP, fill=X)

    kanvas.configure(xscrollcommand=gulirx.set, yscrollcommand=gulir.set)
    kanvas.bind('<Configure>', lambda e: kanvas.configure(scrollregion=kanvas.bbox("all")))
    kanvas.bind("<Left>",  lambda event: kanvas.xview_scroll(-1, "units"))
    kanvas.bind("<Right>", lambda event: kanvas.xview_scroll( 1, "units"))
    kanvas.bind("<Up>",    lambda event: kanvas.yview_scroll(-1, "units"))
    kanvas.bind("<Down>",  lambda event: kanvas.yview_scroll( 1, "units"))

    def on_mousewheel(event):
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift:
            kanvas.xview_scroll(scroll, "units")
        else:
            kanvas.yview_scroll(scroll, "units")
    kanvas.bind_all("<MouseWheel>", on_mousewheel)
    kanvas.focus_set()

    bingkai = Frame(kanvas, bg=frame_background)

    kanvas.create_window((0,0), window=bingkai, anchor="nw")

    def perbarui_scrollbar():
        kanvas.configure(scrollregion=kanvas.bbox("all"))
        root.after(100, perbarui_scrollbar)
    
    root.after(1000, perbarui_scrollbar)

    return kanvas, bingkai

def tombol(root: Tk, list_name: list, list_source: list, list_destination: list, nama_edit_timpa: dict):
    confirm_to_overwrite = IntVar()
    confirm_to_skip = IntVar()

    options = _options.options(root, list_name, list_source, list_destination, confirm_to_overwrite, confirm_to_skip, nama_edit_timpa)

    new = Label(root, text="New")
    new.pack(side=LEFT, fill=Y)
    config.button(new, options.menu)
    def new_bind(event):
        options.menu()

    edit = Label(root, text="Edit")
    edit.pack(side=LEFT, fill=Y)
    config.button(edit, options.edit_file)
    def edit_bind(event):
        options.edit_file()

    delete = Label(root, text="Delete")
    delete.pack(side=LEFT, fill=Y)
    config.button(delete, options.delete_file)
    def delete_bind(event):
        options.delete_file()

    copy = Label(root, text="Copy")
    copy.pack(side=RIGHT, fill=Y)
    config.button(copy, options.run_command, True)
    def copy_bind(event):
        options.run_command(True)

    cut = Label(root, text="Move")
    cut.pack(side=RIGHT, fill=Y)
    config.button(cut, options.run_command, False)
    def cut_bind(event):
        options.run_command(False)

    def timpa_dicentang():
        if confirm_to_overwrite.get() == 1:
            timpa.select()
            lewati.deselect()
    def lewati_dicentang():
        if confirm_to_skip.get() == 1:
            timpa.deselect()
            lewati.select()

    timpa = Checkbutton(root, text = "Overwrites all", command = timpa_dicentang) #bg harus sama dengan jendela_utama
    timpa.pack(side=RIGHT, fill=Y)
    config.checkbutton(timpa, confirm_to_overwrite)

    atau = Label(root, text="or")
    atau.pack(side=RIGHT, fill=Y)
    config.label(atau)

    lewati = Checkbutton(root, text = "Skips all", command = lewati_dicentang) #bg harus sama dengan jendela_utama
    lewati.pack(side=RIGHT, fill=Y)
    config.checkbutton(lewati, confirm_to_skip)

    root.bind("<Control-n>", new_bind)
    root.bind("<Control-N>", new_bind)              #(if Caps lock on)
    root.bind("<Alt-d>", edit_bind)                 #based on Chrome
    root.bind("<Alt-D>", edit_bind)                 #based on Chrome (if Caps lock on)
    root.bind("<Control-d>", delete_bind)
    root.bind("<Control-D>", delete_bind)           #(if Caps lock on)
    root.bind("<Delete>", delete_bind)              #based on Ubuntu
    root.bind("<Control-c>", copy_bind)
    root.bind("<Control-C>", copy_bind)             #(if Caps lock on)
    root.bind("<Control-Shift-c>", copy_bind)       #based on Linux terminal
    root.bind("<Control-Shift-C>", copy_bind)       #based on Linux terminal (if Caps lock on)
    root.bind("<Control-x>", cut_bind)
    root.bind("<Control-X>", cut_bind)              #(if Caps lock on)
    root.bind("<Control-Shift-x>", cut_bind)        #based on Linux terminal
    root.bind("<Control-Shift-X>", cut_bind)        #based on Linux terminal (if Caps lock on)