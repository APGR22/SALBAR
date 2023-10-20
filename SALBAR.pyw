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

if __name__ != "__main__":
    sys.exit()

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.messagebox import *
import gui
from PIL import Image, ImageTk
import os
import extension
import execute
import threading

pesan_error_menanti = ""

if len(sys.argv) > 1: #jika ada argumen lainnya tidak peduli dengan argumen lainnya setelah kedua
    if sys.argv[1] == "main-path": #jika itu adalah perintah
        os.chdir(os.path.dirname(__file__)) #configuration for all to apply
    elif sys.argv[1].startswith("directory="): #jika itu adalah perintah
        try:
            os.chdir(sys.argv[1].replace("directory=", ""))
        except Exception as error:
            pesan_error_menanti = error #if it calls showerror() too early then the icon implementation won't work

jendela_utama = Tk()
jendela_utama.title("SALBAR")
jendela_utama.minsize(width=532, height=440)
jendela_utama.configure(bg=gui.BACKGROUND)
lebar_layar = jendela_utama.winfo_screenwidth()
tinggi_layar = jendela_utama.winfo_screenheight()
default_w = 752
default_h = 480

w = default_w
h = default_h

x = (lebar_layar/2) - (w/2)
y = (tinggi_layar/2) - (h/2)

jendela_utama.geometry('%dx%d+%d+%d' % (w, h, x, y))

path_icon = "SALBAR.png"

def buat_ikon():
    kode_icon = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x06\x00\x00\x00\\r\xa8f\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x04\xa0IDATx\xda\xed\xdcAn\x1b9\x10@QQ\xd0":\xa6u0\xf9\x98\xca\x8e6\x0c\x1b\x10\x0cG!\xad&\x9bd\xbd\x07\x0cf\x13\x04\x13\xb5\xfaw\xb1\xda\x99\xc3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa8\x93V\xf9\x83\xe4\xdb5\xbb\x9c<}C\x9c/I\x00\xdc\xf8\x08A\x12\x80\xb1o\xfc\x8f\x7f\xf9\xaa"\x04\x02\x00\xcd\xef\x93\xf7\x18,\xf7\x07;\xce<\xfd\xfb^B\xdc\x00\x80\x87\x8d\x00@\xd7c\xa7\x00\x80)@\x00@\x04&7\xf3[\x00K@v\xbdoVx+pr-?\xfdy\xf1\x19D\xf7\xf7\xb5f\x12X\xe2\xe7\x03\x04\xe0+\xe9)\xf9\x10\xf8\x9a.\x8b\x7f\xdd\xecS\x80\x00\xdc_tS\x00\xe5\xd3\xc0\x12S\x80\x00|\xbb\xe8+\xfe\xb4\x17\xbfx \xe4\x1c"\x02\x96\x80\xf6\x01<\xbf\x17\x98v)(\x00\xff\xfa`L\x02\xd4\xed\x04\xa6\x8c\x80#\x80\x9d\x00\x81w\x02\x02\xf0(\xe9\xde\x0cP?\t\x08\x80)\x80\xa0\x93\xc0tS\x80\x1d@\t\x11\xa0\xfc(0\xd5>\xc0\x04\xe0(@\xe0\xa3\x80\t\xc0\x14@\xe0)\xc0\x04Pq\xd1\xbd\x1a\xa4b\x12\x98b\x1f \x005\x17<\xfb\x0b\x88TO\x02C\xf3\xff\x03\x08v\xc1\xe9z,\x1c\xfe\x89a\x07\xf0\x9b\x0f\xcdQ\x80\xf2\xa3\xc0\xd0\xfb\x00\x01hW\x7fL\x86\xc3G\xc0\x11\xc0q\x80>\x0f\x83!\x8f\x03\x96\x80OF\xc0q\x80\x8a\xa3\xc0po\x06\x04\xe0\xd9\x8b\xee\xcd\x00\x13O\x86v\x00[|\x88\xa6\x00\xea&\x81a\xf6\x01\x02\xd0\xf7\x1c\x88I`\xa8\x08X\x02\x06\x1d\xfd\xd8\xff\x19f\x07\xb0\x18\x7fi\x88\xca\xa3\x80\x00,w\xc1\x1d\x05(\x9f\nw\x7f+`\x07`\x1f\xc0\xfeG\xc3\xdd\xf6\x01&\x00G\x01\x02\x1f\x05L\x00\xa6\x00\xc6\x98\x04v\x99\x02L\x00\r/\xb8\x9f\x0f\xa0b\x12\xd8e\x1f \x00\xad/\xb8I\x80\xf2)\xa0{\x04\x1c\x01z|\xc8&\x01\xeav\x02\xdd\x8e\x03&\x00\x93\x00\x81\'\x01?\t\x08\xbd\x15>\x0cz\xbc=0\x01t\xac\xbe\xa3\x00\x157x\x97)@\x00\xc6:\xfbA\xd7\x088\x02\xc0\xd8\x0f\x8d\xdc\xf2\xc1!\x00\x10\x98\x00\xc0\x1cG\x01\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x80\xceN>\x02\xa2K\xe7\xcb&\xbfO\xbe]M\x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\xc0P\xd2\xac\xff\xe1\xf9v\xcd.\xdf\xc0_\xac\xf3\xc5\x870\xc1\xbdo\x02\x00G\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\xa0\x97\xe4\xf2\x81\x9b\xc8\xdf\x0c\x1c\xf1\x8b\xe5o\x03Nq\xef\x1f\x17\xb8\xf9]J\x08\xbe\x03p\x1c\x80\x88\x01\xb8\x1b5E\x00\xa2?9\xed\x03\xb8\xfbn\x17}\x17\xb6\xdaW\xb4<\x8e\xbe\xff76\xb9W\x8f\x8b^x\xf0 \x08\x1a\x00\x11\x80\xa8\x01\xf0\xfa\tL\x00\xa6\x00(pZ\xf2\xce\xbf{3`)\x081\'\x00\x93\x00\x08\x80\x08@\xd8\x00\xf8A!0\x01\x00?8E\xf8CZ\n\x82\t\x00\x10\x00\xbb\x00\x88>\x01\x88\x00D\x0c\x80\xb7\x02`\x02\x00\x0eA\xde\x02<\x9a\x02\xbc\x15\xc0\x04\x10\x9b\xa3\x00\x02 \x02 \x00\xa1\x8f\x03\xbe\x0e\xd8\x01\xd8\t\xd8\t`\x02\x00\x04\xc0>\x00\x04@\x04@\x00b\xed\x03@\x00L\x01\xb0.o\x01\x1eO\x01\xde\n`\x020\t\x80\x00\x00\x02`\n\x00\x01\x08\xb8\x0f\xf0i\xb0\x1aK\xc0\xca\x08X\nb\x02p\x1c\x00\x01\x10\x01\x10\x80\xa8\xc7\x01\x10\x00S\x004\x7f\xe8$\x01\x18l\n\xf8\xfcG\x04h.\xdf\xae\xcd~oo\x01\xb6\x99\x04\xbc\x19`\xba\xa7\xbf\x00l\x7f\x1c\xc8\xff\xfb5v\x08c>d{\xdd\xac\xdf\x9e\xe6\xb9\xe0;\xe5\x1c\x0b3\x04`\xc6\xfb\xc9\x0e\x00\x02\x13\x00\x10\x00\x00\x00\x00\x00`Uo\xb5\r\x13~\xb2S\x92\xfa\x00\x00\x00\x00IEND\xaeB`\x82'
    with open(path_icon, "wb") as image:
        image.write(kode_icon)
    jendela_utama.wm_iconphoto(True, ImageTk.PhotoImage(Image.open(path_icon)))
    os.remove(path_icon)

if os.path.isfile(path_icon):
    jendela_utama.wm_iconphoto(True, ImageTk.PhotoImage(Image.open(path_icon)))
else:
    buat_ikon()

if not os.path.isdir("Paths"):
    os.makedirs("Paths")

#Progress Bar
jendela_progress = Toplevel()
jendela_progress.resizable(0, 0)
progress = Progressbar(jendela_progress, orient=HORIZONTAL, mode='indeterminate')
progress.pack(fill=BOTH)
wp = 250
hp = 24
xp = (lebar_layar/2) - (wp/2)
yp = (tinggi_layar/2) - (hp/2)

jendela_progress.geometry('%dx%d+%d+%d' % (wp, hp, xp, yp))
jendela_progress.withdraw()

def cegah_exit():
    pass

jendela_progress.protocol("WM_DELETE_WINDOW", cegah_exit)

fperintah = [] #path
tperintah = [] #path
snama = [] #nama
nama_edit_timpa = {} #sebagai komunikasi antara front-end dan back-end

kanvas_bingkai = gui.bingkai(jendela_utama)
kanvas = kanvas_bingkai[0]
bingkai = kanvas_bingkai[1]

gui.tombol(jendela_utama, snama, fperintah, tperintah, nama_edit_timpa, jendela_progress, progress)

program_list = [] #daftar program yang untuk dijalankan
excluded_program_list = [] #daftar program yang dilarang untuk dijalankan

def refresh_program_list():
    program_list.clear()
    program_list.extend(os.listdir("Paths"))
    program_time_list = {}
    for program in program_list:
        name = os.path.splitext(program)[0]
        date = extension.ekstensi.read_time(name)
        #harus memasukkan isi kamus dengan tipe list
        try:
            program_time_list[date].append(name) #jika sudah ada date yang sama
        except KeyError:
            program_time_list[date] = [name]
    results = []
    for i in sorted(program_time_list): #sorted in date
        for program in sorted(program_time_list[i]): #sorted in name, maybe?
            if not program in excluded_program_list: #cek jika termasuk program yang dikecualikan
                results.append(program)
    program_list.clear()
    program_list.extend(results)

refresh_program_list() #start

f_pilihan = Frame(bingkai, bg="#3c4038")
f_pilihan.grid()

def baca(nama: str, r: int | None = None, tambahkan: bool = False):
    dapat = extension.ekstensi.read(nama)
    direktori = dapat[0]
    tujuan = dapat[1]
    #untuk didefinisi ulang di utama
    if tambahkan:
        hasil = execute.eksekusi(f_pilihan, r, nama, direktori, tujuan, fperintah, tperintah, snama, tambahkan)
    else:
        hasil = execute.eksekusi(f_pilihan, r, nama, direktori, tujuan, fperintah, tperintah, snama)
    globals()[f"{nama}_var"] = hasil[0]
    globals()[f"{nama}_cb"] = hasil[1]
    globals()[f"{nama}_centang"] = hasil[2]
    globals()[f"{nama}_label"] = hasil[3]

def mulai():
    nama_kesalahan = []
    kesalahan = []
    for r, i in enumerate(program_list):
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

daftar_pembaruan = os.listdir("Paths")

if len(daftar_pembaruan) > 744:
    showwarning(
        title="Warning",
        message="Check button exceeds 744.\nPossible rendering will be broken at the very bottom"
    )

def perbarui():
    global daftar_pembaruan, program_list
    daftar_pembaruan_2 = os.listdir("Paths")

    if len(nama_edit_timpa) == 2: #edit
        cache_row = globals()[f"{nama_edit_timpa['nama_lama']}_cb"].grid_info()["row"]
        del globals()[f"{nama_edit_timpa['nama_lama']}_var"], globals()[f"{nama_edit_timpa['nama_lama']}_centang"]
        globals()[f"{nama_edit_timpa['nama_lama']}_cb"].destroy()
        globals()[f"{nama_edit_timpa['nama_lama']}_label"].destroy()
        baca(nama_edit_timpa["nama"], cache_row)
        nama_edit_timpa.clear()
        daftar_pembaruan = os.listdir("Paths")
        fperintah.clear()
        tperintah.clear()
        snama.clear()
        refresh_program_list()

    elif len(nama_edit_timpa) == 1: #timpa
        del globals()[f"{nama_edit_timpa['nama_timpa']}_var"], globals()[f"{nama_edit_timpa['nama_timpa']}_centang"]
        globals()[f"{nama_edit_timpa['nama_timpa']}_cb"].destroy()
        globals()[f"{nama_edit_timpa['nama_timpa']}_label"].destroy()
        baca(nama_edit_timpa["nama_timpa"], tambahkan = True)
        refresh_program_list()
        for r, i in enumerate(program_list):
            globals()[f"{i}_cb"].grid(row=r) #config ulang
            globals()[f"{i}_label"].grid(row=r) #config ulang
        nama_edit_timpa.clear()
        fperintah.clear()
        tperintah.clear()
        snama.clear()

    elif daftar_pembaruan != daftar_pembaruan_2:
        if len(daftar_pembaruan_2) > len(daftar_pembaruan): #tambah
            jumlah = set(daftar_pembaruan_2) - set(daftar_pembaruan)
            for i in jumlah:
                baca(os.path.splitext(i)[0], tambahkan=True)
        else: #kurang
            jumlah = set(daftar_pembaruan) - set(daftar_pembaruan_2)

            for i in jumlah:
                globals()[f"{os.path.splitext(i)[0]}_cb"].deselect() #pastikan untuk membatalkan centangnya
                globals()[f"{os.path.splitext(i)[0]}_centang"]() #pastikan fungsinya berjalan tanpa checkbutton
                del globals()[f"{os.path.splitext(i)[0]}_var"], globals()[f"{os.path.splitext(i)[0]}_centang"]
                globals()[f"{os.path.splitext(i)[0]}_cb"].destroy()
                globals()[f"{os.path.splitext(i)[0]}_label"].destroy()

            refresh_program_list()
            for r, i in enumerate(program_list):
                #config ulang
                try:
                    globals()[f"{i}_cb"].grid(row=r)
                    globals()[f"{i}_label"].grid(row=r)
                except KeyError: #seandainya kesalahannya berasal dari tindakan pengguna yang rename file .slbr secara manual
                    baca(i)
                    globals()[f"{i}_cb"].grid(row=r)
                    globals()[f"{i}_label"].grid(row=r)

        daftar_pembaruan = daftar_pembaruan_2
        refresh_program_list()

    jendela_utama.after(100, perbarui)

perbarui()

#tidak bisa untuk threading semua kode
def thread_mulai():
    threading.Thread(target = mulai).start()
jendela_utama.after(100, thread_mulai) #jangan pakai () agar tidak terpanggil

def pilih(event):
    for i in program_list: #kalau kosong maka for loop-nya tidak berjalan dan dikira selesai
        globals()[f"{i}_cb"].select()
        globals()[f"{i}_centang"]()

def tidak_pilih(event):
    for i in program_list:
        globals()[f"{i}_cb"].deselect()
        globals()[f"{i}_centang"]()

kanvas.bind("<Control-a>",  pilih)
kanvas.bind("<Control-A>",  pilih)
kanvas.bind("<Control-Shift-a>",  tidak_pilih)
kanvas.bind("<Control-Shift-A>",  tidak_pilih)

if len(sys.argv) > 2:
    showinfo(
        title="Info",
        message="Requires only one argument"
    )
if pesan_error_menanti:
    showerror(
        title="Error",
        message=f'Failed to set path: {pesan_error_menanti}\nSo set the path to: "{os.getcwd()}"'
        )


def check_deletion():
    if not os.path.isdir("Paths"):
        showwarning(
            title="Warning!!!",
            message='The “Paths” folder has been deleted, SALBAR will be close'
        )
        sys.exit()
    jendela_utama.after(10, check_deletion)

check_deletion()


jendela_utama.mainloop()