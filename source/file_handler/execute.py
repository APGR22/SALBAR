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
import paths
import info

def eksekusi(
        pilihan: Frame,
        r: int | None,
        n: str,
        d: str,
        t: str,
        date: str,
        info: info._info,
        tambahkan: bool = False
) -> tuple[IntVar, Checkbutton, object, Label, Label]:
    """pilihan = tempat checkbutton diletakkan\n
    r = baris\n #jika r = None, maka termasuk tambahakan
    n = nama\n
    d = direktori sumber\n
    t = direktori tujuan\n
    fperintah = daftar jalur direktori sumber\n
    tperintah = daftar jalur direktori tujuan\n
    snama = daftar nama\n
    tambahkan = menambah tanpa bergantung row
    """
    def centang(reset: bool = True):
        if reset and globals()[f"{n}_var"].get() == 1:
            info.selected = n

        if globals()[f"{n}_var"].get() == 1:
            if d not in info.list_source or t not in info.list_destination or n not in info.list_name:
                info.list_source.append(d)
                info.list_destination.append(t)
                info.list_name.append(n)
            globals()[f"{n}_cb"]["fg"] = checkbutton_selected_foreground
            globals()[f"{n}_cb"]["bg"] = checkbutton_selected_background
        else:
            try:
                info.list_source.remove(d)
                info.list_destination.remove(t)
                info.list_name.remove(n)
            except:
                pass
            globals()[f"{n}_cb"]["fg"] = checkbutton_deselected_foreground
            globals()[f"{n}_cb"]["bg"] = checkbutton_deselected_background

    globals()[f"{n}_var"] = IntVar()

    globals()[f"{n}_cb"] = Checkbutton(
                                       pilihan,
                                       text=n,
                                       bg=checkbutton_deselected_background,
                                       fg=checkbutton_deselected_foreground,
                                       variable=globals()[f"{n}_var"],
                                       onvalue=1, offvalue=0,
                                       command=centang,
                                       font=default_font,
                                       height=2,
                                       highlightthickness=0
                                       )
    if tambahkan:
        globals()[f"{n}_cb"].grid(sticky='w', pady=1)
    else:
        globals()[f"{n}_cb"].grid(row=r, sticky='w', pady=1)

    if paths.is_abs_path(d) or paths.is_abs_path(t):
        label_text="     Has absolute path"
        label_fg="#25dafd"
    else:
        label_text="     Has no absolute path"
        label_fg="#ffea3c"
    globals()[f"{n}_label"] = Label(
                                    pilihan,
                                    text=label_text,
                                    bg=pilihan["bg"],
                                    fg=label_fg,
                                    height=2
                                    )
    globals()[f"{n}_label"].grid(
                                    row=globals()[f"{n}_cb"].grid_info()["row"], #bila gunakan r yang kadang-kadang tidak ada, lebih baik dari grid_info dari cb
                                    column=1,
                                    sticky="w",
                                    pady=1
                                )

    globals()[f"{n}_date"] = Label(
                                    pilihan,
                                    text=date,
                                    bg=pilihan["bg"],
                                    fg=TEXT_COLOR,
                                    height=2
                                    )
    globals()[f"{n}_date"].grid(
                                    row=globals()[f"{n}_cb"].grid_info()["row"],
                                    column=2,
                                    sticky="w",
                                    pady=1
                                )

    globals()[f"{n}_centang"] = centang

    return globals()[f"{n}_var"], globals()[f"{n}_cb"], globals()[f"{n}_centang"], globals()[f"{n}_label"], globals()[f"{n}_date"]