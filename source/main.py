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

#utama
#icon
#yang mengerjakan
#"buat" dan "hapus" hanya sekali eksekusi
#"edit" dan "timpa" perlu komunikasi dengan dibawahnya

import sys
import os
import paths

if __name__ != "__main__":
    sys.exit()

pending_error_message = ""

if len(sys.argv) > 1: #jika ada argumen lainnya tidak peduli dengan argumen lainnya setelah kedua
    if sys.argv[1] in ["-main", "--main"]: #jika itu adalah perintah
        os.chdir(paths.get_current_path()) #configuration for all to apply
    elif sys.argv[1].startswith("--directory="): #jika itu adalah perintah
        try:
            os.chdir(sys.argv[1][len("--directory="):])
        except Exception as error:
            pending_error_message = error #if it calls showerror() too early then the icon implementation won't work
    elif sys.argv[1] in ["-help", "-h", "--help", "--h"]:
        import gui.salbar_help
        sys.exit()

from tkinter import *
from tkinter.messagebox import *
import configurator
from gui import progress
from gui import gui
from gui.styles import *
from gui import image
from gui import selector
from file_handler import extension
from file_handler import execute
from file_handler import refresh
from file_handler import sorter
import datetime
import threading
import info

config = configurator.config("user.yaml")

jendela_utama = Tk()
jendela_utama.title("SALBAR")
jendela_utama.minsize(width=532, height=440)
jendela_utama.configure(bg=background)
width_screen = jendela_utama.winfo_screenwidth()
height_screen = jendela_utama.winfo_screenheight()
default_w = 752
default_h = 480

w = default_w
h = default_h

x = (width_screen/2) - (w/2)
y = (height_screen/2) - (h/2)

jendela_utama.geometry('%dx%d+%d+%d' % (w, h, x, y))

image.set_icon(jendela_utama)

if not os.path.isdir("Paths"):
    os.makedirs("Paths")

list_name = []
list_source = []
list_destination = []
nama_edit_timpa = {} #as communication between this program and the "maker" module

#insert to info
info.info.root = jendela_utama
info.info.list_name = list_name
info.info.list_source = list_source
info.info.list_destination = list_destination
info.info.nama_edit_timpa = nama_edit_timpa

kanvas, bingkai = gui.bingkai(jendela_utama)

gui.tombol(info.info)

dict_program_list = {}
program_list = [] #daftar program yang untuk dijalankan
excluded_program_list = [] #daftar program yang dilarang untuk dijalankan
key = "sort"
if config.find("sorted_by") and config.get_value("sorted_by") in sorter.list_sorted:
    default_sort_text = config.get_value("sorted_by")
    sort_key = config.get_value("sorted_by")
else:
    default_sort_text = sorter.SORTED_NAME
    sort_key = sorter.SORTED_NAME

f_pilihan = Frame(bingkai, bg=frame_background)
f_pilihan.grid()

#insert to info
info.info.selected = ""
info.info.kanvas = kanvas
info.info.bingkai = bingkai
info.info.dict_program_list = dict_program_list
info.info.program_list = program_list
info.info.excluded_program_list = excluded_program_list
info.info.sort_key = sort_key

gui.main(f_pilihan, default_sort_text, info.info)

def baca(nama: str, r: int | None = None, tambahkan: bool = False):
    direktori, tujuan = extension.ekstensi.read(nama)
    date = datetime.datetime.fromtimestamp(float(extension.ekstensi.read_time(nama)))
    #untuk didefinisi ulang di utama
    if tambahkan:
        hasil = execute.eksekusi(f_pilihan, r, nama, direktori, tujuan, date, info.info, tambahkan)
    else:
        hasil = execute.eksekusi(f_pilihan, r+1, nama, direktori, tujuan, date, info.info)
    dict_program_list[f"{nama}_var"] = hasil[0]
    dict_program_list[f"{nama}_cb"] = hasil[1]
    dict_program_list[f"{nama}_centang"] = hasil[2]
    dict_program_list[f"{nama}_label"] = hasil[3]
    dict_program_list[f"{nama}_date"] = hasil[4]

#insert to info
info.info.baca = baca

refresh_class = refresh.refresh(info.info)

done = [False]

#tidak bisa untuk threading semua kode
def start():
    progress_window = progress.simple_progress_bar()
    nama_kesalahan = []
    kesalahan = []
    if len(program_list) > 64:
        progress_window.active()
        total = len(program_list) - 1
    else:
        total = 100 #must not zero
    refresh_class.refresh_program_list() #start
    for r, i in enumerate(program_list):
        persent = r / total * 100
        progress_window.set(persent)
        try:
            baca(i, r)
        except Exception as error:
            nama_kesalahan.append(i)
            kesalahan.append(error)
            excluded_program_list.append(i)
    if nama_kesalahan:
        for i, j in zip(nama_kesalahan, kesalahan):
            showerror(
                title="Error",
                message=f"{i}: {j}"
            )
    progress_window.destroy()
    kanvas.focus_set()

    done[0] = True

if len(sys.argv) > 2:
    showinfo(
        title="Info",
        message="Requires only one argument"
    )
if pending_error_message:
    showerror(
        title="Error",
        message=f'Failed to set path: {pending_error_message}\nSo set the path to: "{os.getcwd()}"'
        )

def _check_successful():
    if done[0]:
        cache_list = os.listdir("Paths")

        #remove non-slbr
        for f in cache_list:
            f = os.path.join("Paths", f)
            if os.path.isfile(f):
                if not f.endswith(".slbr"):
                    cache_list.remove(f)
            else:
                cache_list.remove(f)

        if len(program_list) != len(cache_list):
            showerror(
                title="salbar",
                message="threading has failed, salbar will be reopening"
            )
            jendela_utama.destroy()

            #https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself
            try: os.execv(os.path.join(paths.get_current_path(), "salbar.exe"), sys.argv) #after compile
            except: pass #before compile

        globals().pop("done") #same as (global done; del done)
    else:
        jendela_utama.after(100, _check_successful)

_check_successful()

def check_deletion():
    if not os.path.isdir("Paths"):
        showwarning(
            title="Warning!!!",
            message='The “Paths” folder has been deleted, SALBAR will be close'
        )
        sys.exit()
    jendela_utama.after(100, check_deletion)

check_deletion()

threading.Thread(target = start).start()

selector.simple_select(info.info)

if config.get_value("shift") == True:
    selector_class = selector.main(info.info)

    kanvas.bind("<Shift-Up>", selector_class.up)
    kanvas.bind("<Shift-Down>", selector_class.down)

jendela_utama.mainloop()
