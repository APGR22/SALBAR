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
from file_handler import sorter

def main(root: Tk | Toplevel, default_from_sort_text: str, sort_key: dict[str, str], key: str):
    dict_texts = {
        "Name (A-Z)⯀": sorter.SORTED_NAME,
        "Name (Z-A)⯀": sorter.SORTED_NAME_REVERSED,
        "Date created (OLD-NEW)⯀": sorter.SORTED_TIME,
        "Date created (NEW-OLD)⯀": sorter.SORTED_TIME_REVERSED
    }

    def sort_button(
                    widget: Label | Button,
                    texts: list[str],
                    another_widgets: list[Label] | list[Button],
                    dict_texts: dict[str, str],
                    sort_key: dict[str, str],
                    key: str,
                    use_current_text: bool = False
                    ):
        current_text = widget["text"]

        if use_current_text and current_text.replace("⯀", "") not in texts:
            texts.insert(0, current_text.replace("⯀", ""))
            index = 0
        else:
            index = texts.index(current_text.replace("⯀", ""))

        length = len(texts)

        if current_text.count("⯀"):
            if index+1 == length:
                widget["text"] = texts[0] + "⯀"
            else:
                widget["text"] = texts[index+1] + "⯀"
        else:
            widget["text"] = current_text + "⯀"

        for another_widget in another_widgets:
            another_widget["text"] = another_widget["text"].replace("⯀", "")

        sort_key[key] = dict_texts[widget["text"]]
    
    def set_default(widget: Label | Button, another_text: list[str] = None):
        if dict_texts[widget["text"] + "⯀"] == default_from_sort_text:
            widget["text"] = widget["text"] + "⯀"
        elif another_text is not None:
            for text in another_text:
                if dict_texts[text + "⯀"] == default_from_sort_text:
                    widget["text"] = text + "⯀"

    Name = Label(root, text="Name (A-Z)")
    Name.grid(row=0, column=0)
    set_default(Name, ["Name (Z-A)"])

    State = Label(root, text="State", width=10, height=BUTTON_HEIGHT)
    State.grid(row=0, column=1, padx=1)
    config.label(State)

    Date = Label(root, text="Date created (OLD-NEW)")
    Date.grid(row=0, column=2)
    set_default(Date, ["Date created (NEW-OLD)"])

    config.button(Name, sort_button, Name, ["Name (Z-A)"], [Date], dict_texts, sort_key, key, True, my_width=12)
    config.button(Date, sort_button, Date, ["Date created (NEW-OLD)"], [Name], dict_texts, sort_key, key, True, my_width=22)

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
    confirm_to_not_shutil = IntVar()

    options_class = _options.options(root, list_name, list_source, list_destination, confirm_to_overwrite, confirm_to_skip, confirm_to_not_shutil, nama_edit_timpa)

    start = _options.options_menu(confirm_to_overwrite, confirm_to_skip, confirm_to_not_shutil)

    new = Label(root, text="New")
    new.pack(side=LEFT, fill=Y)
    config.button(new, options_class.menu)
    def new_bind(event):
        options_class.menu()

    edit = Label(root, text="Edit")
    edit.pack(side=LEFT, fill=Y)
    config.button(edit, options_class.edit_file)
    def edit_bind(event):
        options_class.edit_file()

    delete = Label(root, text="Delete")
    delete.pack(side=LEFT, fill=Y)
    config.button(delete, options_class.delete_file)
    def delete_bind(event):
        options_class.delete_file()

    copy = Label(root, text="Copy")
    copy.pack(side=RIGHT, fill=Y)
    config.button(copy, options_class.run_command, True)
    def copy_bind(event):
        options_class.run_command(True)

    cut = Label(root, text="Move")
    cut.pack(side=RIGHT, fill=Y)
    config.button(cut, options_class.run_command, False)
    def cut_bind(event):
        options_class.run_command(False)

    menu = Label(root, text="Menu")
    menu.pack(side=RIGHT, fill=Y)
    config.button(menu, start.active)
    def menu_bind(event):
        start.active()
    
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
    root.bind("<F2>", menu_bind)