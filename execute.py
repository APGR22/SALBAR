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
from gui.styles import FONT
import salbar_path

CHECKBUTTON_SELECTED_FOREGROUND = "#000000"
CHECKBUTTON_SELECTED_BACKGROUND = "#ffffff"
CHECKBUTTON_DESELECTED_FOREGROUND = "#ffffff"
CHECKBUTTON_DESELECTED_BACKGROUND = "#686e61"

def eksekusi(
        pilihan: Frame,
        r: int | None,
        n: str,
        d: str,
        t: str,
        fperintah: list,
        tperintah: list,
        snama: list,
        tambahkan: bool = False
):
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
    def centang():
        if globals()[f"{n}_var"].get() == 1:
            if d not in fperintah or t not in tperintah or n not in snama:
                fperintah.append(d)
                tperintah.append(t)
                snama.append(n)
            globals()[f"{n}_cb"]["fg"] = CHECKBUTTON_SELECTED_FOREGROUND
            globals()[f"{n}_cb"]["bg"] = CHECKBUTTON_SELECTED_BACKGROUND
        else:
            try:
                fperintah.remove(d)
                tperintah.remove(t)
                snama.remove(n)
            except:
                pass
            globals()[f"{n}_cb"]["fg"] = CHECKBUTTON_DESELECTED_FOREGROUND
            globals()[f"{n}_cb"]["bg"] = CHECKBUTTON_DESELECTED_BACKGROUND

    globals()[f"{n}_var"] = IntVar()

    globals()[f"{n}_cb"] = Checkbutton(
                                       pilihan,
                                       text=n,
                                       bg=CHECKBUTTON_DESELECTED_BACKGROUND,
                                       fg=CHECKBUTTON_DESELECTED_FOREGROUND,
                                       variable=globals()[f"{n}_var"],
                                       onvalue=1, offvalue=0,
                                       command=centang,
                                       font=FONT,
                                       height=2,
                                       highlightthickness=0
                                       )
    if tambahkan:
        globals()[f"{n}_cb"].grid(sticky='w', pady=1)
    else:
        globals()[f"{n}_cb"].grid(row=r, sticky='w', pady=1)

    if salbar_path.is_abs_path(d) or salbar_path.is_abs_path(t):
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

    globals()[f"{n}_centang"] = centang

    return globals()[f"{n}_var"], globals()[f"{n}_cb"], globals()[f"{n}_centang"], globals()[f"{n}_label"]