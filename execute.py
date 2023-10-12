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
        fp = d
        tp = t
        if globals()[f"{n}_var"].get() == 1:
            if fp not in fperintah or tp not in tperintah or n not in snama:
                fperintah.append(fp)
                tperintah.append(tp)
                snama.append(n)
            globals()[f"{n}_cb"]["fg"] = "#000000"
            globals()[f"{n}_cb"]["bg"] = "#ffffff"
        else:
            try:
                fperintah.remove(fp)
                tperintah.remove(tp)
                snama.remove(n)
            except:
                pass
            globals()[f"{n}_cb"]["fg"] = "#ffffff"
            globals()[f"{n}_cb"]["bg"] = "#686e61"

    globals()[f"{n}_var"] = IntVar()

    globals()[f"{n}_cb"] = Checkbutton(pilihan, text=n, bg="#686e61", fg='#ffffff', variable=globals()[f"{n}_var"], onvalue=1, offvalue=0, command=centang, font=("Helvetica", 10), height=2)
    if tambahkan:
        globals()[f"{n}_cb"].grid(sticky='w', pady=1)
    else:
        globals()[f"{n}_cb"].grid(row=r, sticky='w', pady=1)

    globals()[f"{n}_centang"] = centang

    return globals()[f"{n}_var"], globals()[f"{n}_cb"], globals()[f"{n}_centang"]
