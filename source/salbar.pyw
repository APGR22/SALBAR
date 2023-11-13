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
from gui import progress
from tkinter.messagebox import *
from gui import gui
from gui.styles import *
from gui import image
from file_handler import extension
from file_handler import execute
import threading

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

list_source = []
list_destination = []
list_name = []
nama_edit_timpa = {} #as communication between this program and the "maker" module

kanvas_bingkai = gui.bingkai(jendela_utama)
kanvas = kanvas_bingkai[0]
bingkai = kanvas_bingkai[1]

gui.tombol(jendela_utama, list_name, list_source, list_destination, nama_edit_timpa)

program_list = [] #daftar program yang untuk dijalankan
excluded_program_list = [] #daftar program yang dilarang untuk dijalankan

def refresh_program_list():
    program_list.clear()
    program_list.extend(os.listdir("Paths"))
    program_time_list = {}
    for program in program_list:
        if program.endswith(".slbr"):
            name = program[:-5]
            if name in excluded_program_list:
                program_list.remove(program)
            else:
                try:
                    extension.ekstensi.check_read(name)
                    date = extension.ekstensi.read_time(name)
                    #harus memasukkan isi kamus dengan tipe list
                    try:
                        program_time_list[date].append(name) #jika sudah ada date yang sama
                    except KeyError:
                        program_time_list[date] = [name]
                except Exception as error:
                    showerror(
                        title="Error",
                        message=f"{name}: {error}"
                    )
                    excluded_program_list.append(name)
    results = []
    for i in sorted(program_time_list): #sorted in date
        for program in sorted(program_time_list[i]): #sorted in name, maybe?
            if not program in excluded_program_list: #cek jika termasuk program yang dikecualikan
                results.append(program)
    program_list.clear()
    program_list.extend(results)

f_pilihan = Frame(bingkai, bg=frame_background)
f_pilihan.grid()

def baca(nama: str, r: int | None = None, tambahkan: bool = False):
    dapat = extension.ekstensi.read(nama)
    direktori = dapat[0]
    tujuan = dapat[1]
    #untuk didefinisi ulang di utama
    if tambahkan:
        hasil = execute.eksekusi(f_pilihan, r, nama, direktori, tujuan, list_source, list_destination, list_name, tambahkan)
    else:
        hasil = execute.eksekusi(f_pilihan, r, nama, direktori, tujuan, list_source, list_destination, list_name)
    globals()[f"{nama}_var"] = hasil[0]
    globals()[f"{nama}_cb"] = hasil[1]
    globals()[f"{nama}_centang"] = hasil[2]
    globals()[f"{nama}_label"] = hasil[3]

def remove_non_slbr(daftar: list[str]):
    daftar_cache = set(daftar) - set([name+".slbr" for name in excluded_program_list])
    daftar.clear()
    daftar.extend(daftar_cache)
    for path in daftar:
        if path[:-5] in excluded_program_list:
            daftar.remove(path)
        elif path.endswith(".slbr"):
            try:
                extension.ekstensi.check_read(path[:-5])
            except Exception as error:
                showerror(
                    title="Error",
                    message=f"{path[:-5]}: {error}"
                )
                excluded_program_list.append(path[:-5])
                daftar.remove(path)
        else:
            daftar.remove(path)

daftar_pembaruan = os.listdir("Paths")
remove_non_slbr(daftar_pembaruan)

if len(daftar_pembaruan) > 744:
    showwarning(
        title="Warning",
        message="Check button exceeds 744.\nPossible rendering will be broken at the very bottom"
    )

def perbarui():
    global daftar_pembaruan, program_list
    daftar_pembaruan_2 = os.listdir("Paths")
    remove_non_slbr(daftar_pembaruan_2)

    if len(nama_edit_timpa) == 2: #edit
        cache_row = globals()[f"{nama_edit_timpa['nama_lama']}_cb"].grid_info()["row"]
        del globals()[f"{nama_edit_timpa['nama_lama']}_var"], globals()[f"{nama_edit_timpa['nama_lama']}_centang"]
        globals()[f"{nama_edit_timpa['nama_lama']}_cb"].destroy()
        globals()[f"{nama_edit_timpa['nama_lama']}_label"].destroy()
        baca(nama_edit_timpa["nama"], cache_row)
        nama_edit_timpa.clear()
        list_source.clear()
        list_destination.clear()
        list_name.clear()

    elif len(nama_edit_timpa) == 1: #timpa
        try:
            del globals()[f"{nama_edit_timpa['nama_timpa']}_var"], globals()[f"{nama_edit_timpa['nama_timpa']}_centang"]
            globals()[f"{nama_edit_timpa['nama_timpa']}_cb"].destroy()
            globals()[f"{nama_edit_timpa['nama_timpa']}_label"].destroy()
        except:
            try:
                excluded_program_list.remove(nama_edit_timpa["nama_timpa"])
            except:
                pass
        baca(nama_edit_timpa["nama_timpa"], tambahkan = True)
        refresh_program_list()
        for r, i in enumerate(program_list):
            globals()[f"{i}_cb"].grid(row=r) #reconfig
            globals()[f"{i}_label"].grid(row=r) #reconfig
        nama_edit_timpa.clear()
        list_source.clear()
        list_destination.clear()
        list_name.clear()
        daftar_pembaruan_2 = os.listdir("Paths") #reconfig
        remove_non_slbr(daftar_pembaruan_2)

    elif daftar_pembaruan != daftar_pembaruan_2:
        if len(daftar_pembaruan_2) > len(daftar_pembaruan): #tambah
            jumlah = set(daftar_pembaruan_2) - set(daftar_pembaruan)
            for i in jumlah:
                baca(i[:-5], tambahkan=True)
        else: #kurang
            jumlah = set(daftar_pembaruan) - set(daftar_pembaruan_2)

            for i in jumlah:
                globals()[f"{i[:-5]}_cb"].deselect() #pastikan untuk membatalkan centangnya
                globals()[f"{i[:-5]}_centang"]() #pastikan fungsinya berjalan tanpa checkbutton
                del globals()[f"{i[:-5]}_var"], globals()[f"{i[:-5]}_centang"]
                globals()[f"{i[:-5]}_cb"].destroy()
                globals()[f"{i[:-5]}_label"].destroy()

            refresh_program_list()
            for r, i in enumerate(program_list):
                #reconfig
                try:
                    globals()[f"{i}_cb"].grid(row=r)
                    globals()[f"{i}_label"].grid(row=r)
                except: #seandainya kesalahannya berasal dari tindakan pengguna yang rename file .slbr secara manual
                    baca(i)
                    globals()[f"{i}_cb"].grid(row=r)
                    globals()[f"{i}_label"].grid(row=r)

    daftar_pembaruan = daftar_pembaruan_2
    refresh_program_list()

    jendela_utama.after(100, perbarui)

perbarui()

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
    refresh_program_list() #start
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

def pilih(event):
    for i in program_list: #kalau kosong maka for loop-nya tidak berjalan dan dikira selesai
        globals()[f"{i}_cb"].select()
        globals()[f"{i}_centang"]()

def tidak_pilih(event):
    for i in program_list:
        globals()[f"{i}_cb"].deselect()
        globals()[f"{i}_centang"]()

#doesn't catch the exception even if the user disables the progress bar window
kanvas.bind("<Control-a>",  pilih)
kanvas.bind("<Control-A>",  pilih)
kanvas.bind("<Control-Shift-a>",  tidak_pilih)
kanvas.bind("<Control-Shift-A>",  tidak_pilih)

jendela_utama.mainloop()
