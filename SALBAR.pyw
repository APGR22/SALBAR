"""Copyright © 2023 APGR22

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

#only for developer
# from timeit import timeit
# print(f"Load Time (__start__): {(start_time := timeit())}")
from time import time, sleep
# print(f"Load Time (starttime): {(start_time_time := time())}")
from tkinter import *
from tkinter.ttk import Progressbar
import os
from pathlib import *
#import subprocess
from tkinter.messagebox import *
from tkinter.messagebox import WARNING
from tkinter.filedialog import *
from PIL import Image, ImageTk
from cm import *
try:
    from Worker import *
    ada_pekerja = True
except Exception:
    ada_pekerja = False
from threading import Thread

if not os.path.isdir("Paths"):
    os.makedirs("Paths")

#Alat
class alat():
    class bunyikan_belnya(Frame):
        def on(self):
            self.bell()
alat = alat()

#Start
#kemungkinan #e5e5e5 adalah default warna
latar_belakang = "#737373"
latar_belakang_bingkai = "#3c4038"
latar_belakang_bingkai_options = "#606060"
latar_belakang_bingkai_tombol_options = "#444444"
warna_teks = "#ffffff"
warna_teks_tidak_aktif = "#aaaaaa"
latar_belakang_centang = "#686868"
latar_belakang_kotak_centang_aktif = "#ffffff"
latar_belakang_entry = "#565656"
label_slbr = "#25dafd"
label_slbre = "#ffea3c"
latar_belakang_checkbutton = "#686e61"
latar_belakang_checkbutton_aktif = "#ffffff"
teks_checkbutton = "#ffffff"
teks_checkbutton_aktif = "#000000"

def make_file_icon():
    #bytes python from png file
    #didn't use the encoder because I thought it would slow down the performance even though it wasn't noticeable
    #base64=2KB, bytes=4KB
    kode_icon = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x06\x00\x00\x00\\r\xa8f\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x04\xa0IDATx\xda\xed\xdcAn\x1b9\x10@QQ\xd0":\xa6u0\xf9\x98\xca\x8e6\x0c\x1b\x10\x0cG!\xad&\x9bd\xbd\x07\x0cf\x13\x04\x13\xb5\xfaw\xb1\xda\x99\xc3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa8\x93V\xf9\x83\xe4\xdb5\xbb\x9c<}C\x9c/I\x00\xdc\xf8\x08A\x12\x80\xb1o\xfc\x8f\x7f\xf9\xaa"\x04\x02\x00\xcd\xef\x93\xf7\x18,\xf7\x07;\xce<\xfd\xfb^B\xdc\x00\x80\x87\x8d\x00@\xd7c\xa7\x00\x80)@\x00@\x04&7\xf3[\x00K@v\xbdoVx+pr-?\xfdy\xf1\x19D\xf7\xf7\xb5f\x12X\xe2\xe7\x03\x04\xe0+\xe9)\xf9\x10\xf8\x9a.\x8b\x7f\xdd\xecS\x80\x00\xdc_tS\x00\xe5\xd3\xc0\x12S\x80\x00|\xbb\xe8+\xfe\xb4\x17\xbfx \xe4\x1c"\x02\x96\x80\xf6\x01<\xbf\x17\x98v)(\x00\xff\xfa`L\x02\xd4\xed\x04\xa6\x8c\x80#\x80\x9d\x00\x81w\x02\x02\xf0(\xe9\xde\x0cP?\t\x08\x80)\x80\xa0\x93\xc0tS\x80\x1d@\t\x11\xa0\xfc(0\xd5>\xc0\x04\xe0(@\xe0\xa3\x80\t\xc0\x14@\xe0)\xc0\x04Pq\xd1\xbd\x1a\xa4b\x12\x98b\x1f \x005\x17<\xfb\x0b\x88TO\x02C\xf3\xff\x03\x08v\xc1\xe9z,\x1c\xfe\x89a\x07\xf0\x9b\x0f\xcdQ\x80\xf2\xa3\xc0\xd0\xfb\x00\x01hW\x7fL\x86\xc3G\xc0\x11\xc0q\x80>\x0f\x83!\x8f\x03\x96\x80OF\xc0q\x80\x8a\xa3\xc0po\x06\x04\xe0\xd9\x8b\xee\xcd\x00\x13O\x86v\x00[|\x88\xa6\x00\xea&\x81a\xf6\x01\x02\xd0\xf7\x1c\x88I`\xa8\x08X\x02\x06\x1d\xfd\xd8\xff\x19f\x07\xb0\x18\x7fi\x88\xca\xa3\x80\x00,w\xc1\x1d\x05(\x9f\nw\x7f+`\x07`\x1f\xc0\xfeG\xc3\xdd\xf6\x01&\x00G\x01\x02\x1f\x05L\x00\xa6\x00\xc6\x98\x04v\x99\x02L\x00\r/\xb8\x9f\x0f\xa0b\x12\xd8e\x1f \x00\xad/\xb8I\x80\xf2)\xa0{\x04\x1c\x01z|\xc8&\x01\xeav\x02\xdd\x8e\x03&\x00\x93\x00\x81\'\x01?\t\x08\xbd\x15>\x0cz\xbc=0\x01t\xac\xbe\xa3\x00\x157x\x97)@\x00\xc6:\xfbA\xd7\x088\x02\xc0\xd8\x0f\x8d\xdc\xf2\xc1!\x00\x10\x98\x00\xc0\x1cG\x01\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x80\xceN>\x02\xa2K\xe7\xcb&\xbfO\xbe]M\x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\xc0P\xd2\xac\xff\xe1\xf9v\xcd.\xdf\xc0_\xac\xf3\xc5\x870\xc1\xbdo\x02\x00G\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\xa0\x97\xe4\xf2\x81\x9b\xc8\xdf\x0c\x1c\xf1\x8b\xe5o\x03Nq\xef\x1f\x17\xb8\xf9]J\x08\xbe\x03p\x1c\x80\x88\x01\xb8\x1b5E\x00\xa2?9\xed\x03\xb8\xfbn\x17}\x17\xb6\xdaW\xb4<\x8e\xbe\xff76\xb9W\x8f\x8b^x\xf0 \x08\x1a\x00\x11\x80\xa8\x01\xf0\xfa\tL\x00\xa6\x00(pZ\xf2\xce\xbf{3`)\x081\'\x00\x93\x00\x08\x80\x08@\xd8\x00\xf8A!0\x01\x00?8E\xf8CZ\n\x82\t\x00\x10\x00\xbb\x00\x88>\x01\x88\x00D\x0c\x80\xb7\x02`\x02\x00\x0eA\xde\x02<\x9a\x02\xbc\x15\xc0\x04\x10\x9b\xa3\x00\x02 \x02 \x00\xa1\x8f\x03\xbe\x0e\xd8\x01\xd8\t\xd8\t`\x02\x00\x04\xc0>\x00\x04@\x04@\x00b\xed\x03@\x00L\x01\xb0.o\x01\x1eO\x01\xde\n`\x020\t\x80\x00\x00\x02`\n\x00\x01\x08\xb8\x0f\xf0i\xb0\x1aK\xc0\xca\x08X\nb\x02p\x1c\x00\x01\x10\x01\x10\x80\xa8\xc7\x01\x10\x00S\x004\x7f\xe8$\x01\x18l\n\xf8\xfcG\x04h.\xdf\xae\xcd~oo\x01\xb6\x99\x04\xbc\x19`\xba\xa7\xbf\x00l\x7f\x1c\xc8\xff\xfb5v\x08c>d{\xdd\xac\xdf\x9e\xe6\xb9\xe0;\xe5\x1c\x0b3\x04`\xc6\xfb\xc9\x0e\x00\x02\x13\x00\x10\x00\x00\x00\x00\x00`Uo\xb5\r\x13~\xb2S\x92\xfa\x00\x00\x00\x00IEND\xaeB`\x82'
    #get help from 'https://stackoverflow.com/questions/9929479/embed-icon-in-python-script' and 'https://stackoverflow.com/questions/3715493/encoding-an-image-file-with-base64'

    buat_icon = open(path_icon_temp, "wb")
    buat_icon.write(kode_icon)
    buat_icon.close()

path_icon = "SALBAR.png"
path_icon_temp = "data_icon_temp.png"

jendela_utama = Tk()

if not os.path.isfile(path_icon):
    make_file_icon()
try:
    jendela_utama.wm_iconphoto(True, ImageTk.PhotoImage(Image.open(path_icon)))
except:
    try:
        jendela_utama.wm_iconphoto(True, ImageTk.PhotoImage(Image.open(path_icon_temp)))
    except:
        pass #berarti menggunakan default tkinter
if os.path.isfile(path_icon_temp):
    os.remove(path_icon_temp)

jendela_utama.title("SALBAR")
jendela_utama.resizable(1,1)
jendela_utama.minsize(width=532, height=440)
jendela_utama.configure(bg=latar_belakang)

#GUI
lebar_layar = jendela_utama.winfo_screenwidth()
tinggi_layar = jendela_utama.winfo_screenheight()
default_w = 752 #Minimal 552
default_h = 480 #Minimal 480
def if_results_is_else():
    global w, h
    w = default_w
    h = default_h
if not os.path.exists("resize.ignore"):
    if os.path.exists("window resize.pyi"):
        try:
            exec(compile(open("window resize.pyi", "rb").read(), "", "exec"))
        except:
            if_results_is_else()
    else:
        if_results_is_else()
else:
    if_results_is_else()

x = (lebar_layar/2) - (w/2)
y = (tinggi_layar/2) - (h/2)

jendela_utama.geometry('%dx%d+%d+%d' % (w, h, x, y))

lebar_tombol = 8
tinggi_tombol = 2

lebar_tombol_select_f = 14
lebar_tombol_titik = 2

lebar_centang = False #Untuk daftar perintah
tinggi_centang = 2 #Untuk daftar perintah

ukuran_teks = 10 #hasilnya 9
font_teks = ("Helvetica", ukuran_teks)

#progress
jalankan_progress = True
jendela_progress = Toplevel()
jendela_progress.resizable(0, 0)
jendela_progress.grab_set()
jendela_progress.focus_set()
progress = Progressbar(jendela_progress, orient=HORIZONTAL, mode='determinate')
progress.pack(fill=BOTH)
wp = 250
hp = 24
xp = (lebar_layar/2) - (wp/2)
yp = (tinggi_layar/2) - (hp/2)

jendela_progress.geometry('%dx%d+%d+%d' % (wp, hp, xp, yp))

def kemajuan(n, total_daftar):
    jendela_progress.deiconify()
    jendela_progress.grab_set()
    hitung = (n+1)/total_daftar*100
    progress["value"] = hitung
    jendela_progress.update_idletasks()
    if hitung == 100:
        global jalankan_progress
        sleep(0.100)
        jalankan_progress = False
        jendela_progress.grab_release()
        jendela_progress.withdraw()


def gaya_tombol(obj, callable, callobj, **pilihan):
    default_fg = '#ffffff'
    default_bg = '#4b4b4b'
    klik_fg = '#ffffff'
    klik_bg = '#1f1f1f'
    lepas_fg = default_fg
    lepas_bg = default_bg
    border = 1
    border_bg = "#929292"
    global f
    f = False
    try:
       pilihan["s_lebar_tombol"]
    except:
        hasil = "tidak ada" 
    else:
        hasil = "ada" 
    obj.config(fg=default_fg, bg=default_bg, highlightthickness=border, highlightbackground=border_bg, height=tinggi_tombol, font=font_teks)
    if hasil == "ada":
        obj.config(width=pilihan["s_lebar_tombol"])
    else:
        obj.config(width=lebar_tombol)
    def klik(event):
        obj.config(fg=klik_fg, bg=klik_bg)
    def lepas(event):
        try:
            pilihan["more_callobj"]
        except:
            hasil = "tidak ada" 
        else:
            hasil = "ada" 
        obj.config(fg=lepas_fg, bg=lepas_bg)
        if f:
            if callable != "tidak perlu":
                if callobj == "tidak perlu":
                    callable()
                elif hasil == "ada":
                    callable(callobj, pilihan["more_callobj"])
                else:
                    callable(callobj)
    def kursor(event):
        global f
        f = True
    def tinggal(event):
        global f
        f = False
    obj.bind("<Enter>", kursor) #kursor mengenainya
    obj.bind("<Leave>", tinggal) #kursor meninggalkannya
    obj.bind("<ButtonPress-1>", klik) #Button-1==tombol berubah tapi ketika kursor meninggalkannya
    obj.bind("<ButtonRelease-1>", lepas) #ButtonRelease-1==tombol semula setelah ditekan

#gaya tkinter
def gaya_tombol_cek(obj, var, **pilihan):
    obj.config(variable=var, onvalue=1, offvalue=0, bg=latar_belakang, activebackground=latar_belakang_kotak_centang_aktif, fg=warna_teks, disabledforeground=warna_teks_tidak_aktif, selectcolor=latar_belakang_centang)
    try:
        obj.config(bg=pilihan["latar_belakang"])
    except:
        pass

def gaya_entry(obj, var, jendela, *pilihan): #edit == True
    global key
    key = False
    def get_key_backspace(event):
        global key
        key = True
    global pertama_kali
    try:
        pilihan[1] #if True (== edit)
        pertama_kali = True
    except:
        pertama_kali = False
    daftar_karakter = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    daftar_angka = "0123456789"
    if pilihan:
        if pilihan[0] == "path":
            daftar_karakter += """/\\:()~.-+!# "'"""
    #get help from "https://stackoverflow.com/questions/49484637/how-to-set-only-certain-characters-to-be-inputted-into-an-entry-widget"
    def pilihan_karakter(S):
        global pertama_kali, key
        # print(S)
        # print(S in list(daftar_karakter))
        if obj.index(INSERT) == 0 and pilihan[0] == "name":
            if S in list(daftar_karakter.replace(daftar_angka, "")) and len(S) == 1: #get help from "https://stackoverflow.com/questions/31023744/getting-cursor-position-in-tkinter-entry-widget"
                return True
            elif pertama_kali:
                pertama_kali = False
                return True
            elif len(S) > 1: #fungsinya untuk jika pilih karakter satu atau lebih #harus lebih dari satu agar ketahuan kalau itu dipilih
                ada = 0
                for c in S:
                    if not c in list(daftar_karakter): #jika ketemu karakter yang tidak terdaftar
                        ada = 1
                        break #hentikan proses
                h = 0
                for hi, angka in enumerate(S): #jika ketemu karakter angka
                    if not angka in daftar_angka: #ketika sudah ketemu non-angka, maka hasil yang akan menentukan. Apakah hasilnya 0 (True) atau tidak 0 (False)
                        h = hi
                        break
                if not ada and not h:
                    return True
                else:
                    alat.bunyikan_belnya().on()
                    return False
            # print(f"Pertama: {S in list(daftar_karakter)}")
        else:
            # print(f"Kedua: {S in list(daftar_karakter)}")
            # print(len(S))
            if pilihan[0] == "path" and obj.index(INSERT) == 0 and len(S) == 1: #jika kursor di awal (dan panjangnya harus satu (setiap ketikan meski ada yang di copy-paste))
                if S in daftar_karakter.replace("'", ""):
                    return True
            elif pilihan[0] == "path" and obj.index(INSERT) == len(obj.get()) and len(S) == 1: #jika kursor di awal (dan panjangnya harus satu (setiap ketikan meski ada yang di copy-paste))
                if S in daftar_karakter.replace("'", ""):
                    key = False
                    return True
                elif key:
                    key = False
                    return True
            elif S in list(daftar_karakter):
                return True
            elif pertama_kali:
                pertama_kali = False
                return True
            elif len(S) > 1: #fungsinya untuk jika pilih karakter satu atau lebih #harus lebih dari satu agar ketahuan kalau itu dipilih
                ada = 0
                for c in S:
                    if not c in list(daftar_karakter): #jika ketemu karakter yang tidak terdaftar
                        ada = 1
                        break
                if not ada:
                    return True
                else:
                    alat.bunyikan_belnya().on()
                    return False
        alat.bunyikan_belnya().on()
        key = False
        return False
    if pilihan[0] == "password":
        obj.config(textvariable=var, bg=latar_belakang_entry, fg=warna_teks, font=font_teks)
    else:
        batas_karakter = (jendela.register(pilihan_karakter), '%S')
        obj.config(textvariable=var, bg=latar_belakang_entry, fg=warna_teks, font=font_teks, validate="key", validatecommand=batas_karakter)
        obj.bind("<BackSpace>", get_key_backspace)
#

#Get helped from "https://www.youtube.com/watch?v=0WafQCaok6g"

#Bikin bingkai utama
bingkai_utama = Frame(jendela_utama, bg=latar_belakang_bingkai)
bingkai_utama.pack(fill=BOTH, expand=1)

bingkai_kedua = Frame(jendela_utama)
bingkai_kedua.pack(fill=BOTH)

bingkai_opsi = Frame(jendela_utama, bg=latar_belakang_bingkai_options)
bingkai_opsi.pack(fill=BOTH)

def bikin_bingkai():
    global kanvas, gulir, gulirx, bingkai
    #Bikin kanvas
    kanvas = Canvas(bingkai_utama, bg=latar_belakang_bingkai, highlightthickness=0)
    kanvas.pack(side=LEFT, fill=BOTH, expand=1)

    #Bikin scrollbar
    gulir = Scrollbar(bingkai_utama,orient=VERTICAL, command=kanvas.yview)
    gulir.pack(side=RIGHT, fill=Y)
    
    gulirx = Scrollbar(bingkai_kedua,orient=HORIZONTAL, command=kanvas.xview)
    gulirx.pack(side=TOP, fill=X)

    #Konfigurasi kanvas
    kanvas.configure(xscrollcommand=gulirx.set, yscrollcommand=gulir.set)
    kanvas.bind('<Configure>', lambda e: kanvas.configure(scrollregion=kanvas.bbox("all"))) #e == Event
    
    #Gulir dengan tombol, get helped from "https://stackoverflow.com/questions/33665542/tkinter-how-to-scroll-an-entire-canvas-using-arrow-keys"
    kanvas.bind("<Left>",  lambda event: kanvas.xview_scroll(-1, "units"))
    kanvas.bind("<Right>", lambda event: kanvas.xview_scroll( 1, "units"))
    kanvas.bind("<Up>",    lambda event: kanvas.yview_scroll(-1, "units"))
    kanvas.bind("<Down>",  lambda event: kanvas.yview_scroll( 1, "units"))
    #Get helped from "https://stackoverflow.com/questions/42830690/trouble-with-mousewheel-scrollbars-in-tkinter"
    def on_mousewheel(event):
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift:
            kanvas.xview_scroll(scroll, "units")
        else:
            kanvas.yview_scroll(scroll, "units")
    kanvas.bind_all("<MouseWheel>", on_mousewheel)
    kanvas.focus_set()

    #Bikin bingkai kedua (digunakan)
    bingkai = Frame(kanvas, bg=latar_belakang_bingkai) #warna bg harus sama dengan kanvas agar tidak terlihat perbatasan antara kanvas dan bingkai

    #BIkin bingkai menjadi jendela kanvas
    kanvas.create_window((0,0), window=bingkai, anchor="nw")

def hancur_semua_bingkai():
    global kanvas, gulir, gulirx, bingkai
    kanvas.destroy()
    gulir.destroy()
    gulirx.destroy()
    bingkai.destroy()

#Main

fperintah = [] #list
tperintah = [] #list
snama = [] #list
ntipe = []
pperintah = "" #string
nama = StringVar()
direktori = StringVar()
tujuan = StringVar()
tipe = StringVar()
password = StringVar()
d_f_or_f = IntVar()
t_f_or_f = IntVar()
konfirmasi_timpa = IntVar()
konfirmasi_aman = IntVar()

#reset
def reset_var():
    r = ""
    #var
    nama.set(r)
    direktori.set(r)
    tujuan.set(r)
    tipe.set(r)
    #list
    snama.clear()
    fperintah.clear()
    tperintah.clear()
    ntipe.clear()

def buat(edit, *argumen_lainnya):
    global jendela_tanya, fl, tnama
    n = f"{nama.get()}"
    d = f"{direktori.get()}"
    t = f"{tujuan.get()}"
    tp = f"{tipe.get()}"
    if not n == "" and not d == "" and not t == "":
        if not len(n) > 251:
            if edit == "edit":
                e = tp
            else:
                if ada_pekerja and konfirmasi_aman.get() == 1:
                    e = ".slbre"
                else:
                    e = ".slbr"
            et = e.replace(".", "")
            teks = f"""
global calling, nama_{n}_{et}
def nama_{n}_{et}():
    global fl, cb_{n}_{et}, var{n}_{et}
    def centang():
        fp = r'''{d}'''
        tp = r'''{t}'''
        if var{n}_{et}.get() == 1:
            fperintah.append(fp)
            tperintah.append(tp)
            snama.append('{n}')
            ntipe.append('{e}')
            cb_{n}_{et}["fg"] = teks_checkbutton_aktif
            cb_{n}_{et}["bg"] = latar_belakang_checkbutton_aktif
        else:
            try:
                fperintah.remove(fp)
                tperintah.remove(tp)
                snama.remove('{n}')
                ntipe.remove('{e}')
            except:
                pass
            cb_{n}_{et}["fg"] = teks_checkbutton
            cb_{n}_{et}["bg"] = latar_belakang_checkbutton

    var{n}_{et} = IntVar()

    cb_{n}_{et} = Checkbutton(fl, text='{n}', bg=latar_belakang_checkbutton, fg='#ffffff', variable=var{n}_{et}, onvalue=1, offvalue=0, command=centang, font=font_teks, width=lebar_centang, height=tinggi_centang)
    global r
    cb_{n}_{et}.grid(row=r, sticky='w', pady=1)

calling = nama_{n}_{et}""" #must not to add new line #must 31 lines or contact me if you want to add or remove rows
            global op, fl, l
            if edit == "edit":
                op = fr"Paths\{n}{tp}"
                op_lama = fr"Paths\{argumen_lainnya[0]}{tp}"
            else:
                if ada_pekerja and konfirmasi_aman.get() == 1:
                    op = fr"Paths\{n}.slbre"
                else:
                    op = fr"Paths\{n}.slbr"
                op_lama = None
            def buat_or_timpa():
                # for n, i in enumerate(teks):
                #     print(n, i)
                if edit == "edit":
                    if tp == ".slbre":
                        teks_compile = my_compile(my_format(teks))
                    else: #apapun akan dianggap .slbr
                        teks_compile = my_format(teks)
                else:
                    if ada_pekerja and konfirmasi_aman.get() == 1:
                        teks_compile = my_compile(my_format(teks)) #must in str
                    else:
                        teks_compile = my_format(teks)
                #for debug
                    # teks_decompile = my_decompile(teks_compile)

                    #repr help to found difference between teks and teks_decompile
                    # for n, i, j in zip(enumerate(repr(teks)), repr(teks), repr(teks_decompile)):
                    #     if i != j:
                    #         letak_kesalahan = n[0]
                    #         kesalahan_string1 = i
                    #         kesalahan_string2 = j
                    #         print(f"Kesalahan: {letak_kesalahan} \"{kesalahan_string1}\" \"{kesalahan_string2}\"")
                    # print(teks.lstrip() == teks_decompile.lstrip())
                    # hi = 0
                    # for i, j in zip(repr(teks), repr(teks_decompile)): #enumerate() make repr() to not to maks of repr()
                    #     try:
                    #         print(f"{hi} {i} , {hi} {j}")
                    #     except:
                    #         break
                    #     else:
                    #         hi +=1
                if edit != "edit":
                    if os.path.exists(op):
                        os.remove(op)
                else:
                    try:
                        os.rename(op_lama, op)
                        # print(argumen_lainnya)
                    except Exception as error:
                        # print(argumen_lainnya)
                        print(error)
                        pass
                new = open(op, "wb")
                # print(tp)
                new.write(teks_compile.encode("utf-8"))
                new.close()
                reset_var()
                jendela_tanya.destroy()
                if edit == "edit":
                    perbarui("edit", n, et, argumen_lainnya[0])
            if edit != "edit":
                if not os.path.exists(op):
                    buat_or_timpa()
                else:
                    ask = askokcancel(
                        title="Warning",
                        message='We found the filename is the same as your entry name.\nClick "Ok" to overwrite (old file will be deleted)',
                        icon=WARNING,
                        parent=jendela_tanya
                    )
                    if ask: #True
                        buat_or_timpa()
                        perbarui("cmd")
            elif op == op_lama:
                buat_or_timpa()
            elif os.path.exists(op):
                showinfo(
                    title = "Info",
                    message = "We found the filename is the same as your entry name. Try again",
                    parent=jendela_tanya
                )
            else:
                buat_or_timpa()
        else:
            showwarning(
                title="Warning",
                message="Sorry, you can't insert over 251 words!",
                parent=jendela_tanya
            )
    else:
        showerror(
            title="Error",
            message="You can't fill empty!",
            parent=jendela_tanya
        )

def sbuat(edit): #n == 0, d == 1, t == 2
    global jendela_tanya
    if edit != "edit":
        nama.set("")
        direktori.set("")
        tujuan.set("")
    if edit == "edit":
        true_false = True
    else:
        true_false = False
    jendela_tanya = Toplevel()
    jendela_tanya.grab_set()
    jendela_tanya.title("Configuration")
    jendela_tanya.resizable(0,0)
    jendela_tanya.configure(bg=latar_belakang)
    jendela_tanya.focus_set()
    #GUI
    wt = jendela_utama.winfo_width() - 22 #Hasilnya 380
    ht = jendela_utama.winfo_height() - 110 #Hasilnya 220

    xt = (lebar_layar/2) - (wt/2)
    yt = (tinggi_layar/2) - (ht/2)

    jendela_tanya.geometry('%dx%d+%d+%d' % (wt, ht, xt, yt))
    #
    def d_file_folder(dr_or_tj, *pilihan): #checkbox variables
        def config_entry(stringvar, entry, askopen):
            def same_acts_in_else():
                stringvar.set(askopen)
            def same_acts():
                entry.icursor(len(entry.get()))
                entry.xview_moveto(1)
            if pilihan:
                if pilihan[0] == "tambahkan":
                    if askopen:
                        if stringvar.get():
                            askopen = " "+askopen
                    stringvar.set(stringvar.get()+askopen) #meski kosong akan tetap diisi dengan hampa
                    entry.focus_set()
                    same_acts()
                else: #kondisi yang sama secara berulang
                    same_acts_in_else()
                    same_acts()
            else: #kondisi yang sama secara berulang
                same_acts_in_else()
                same_acts()

        #0 = folder
        #1 = file
        if dr_or_tj == "dr":
            if (d_f_or_f.get() == 1):
                d1 = askopenfilenames(parent=jendela_tanya, title="Directory")
                # print(d1)
                if d1:
                    d1 = '" "'.join(str(x) for x in d1)
                    d1 = '"'+d1+'"'
                    d1 = d1.replace("/", "\\")
                config_entry(direktori, tdirektori, d1)
            else:
                d0 = askdirectory(parent=jendela_tanya, title="Directory")
                if d0:
                    d0 = d0.replace("/", "\\")
                    d0 = '"'+d0+'"'
                config_entry(direktori, tdirektori, d0)
        elif dr_or_tj == "tj":
            if (t_f_or_f.get() == 1):
                t1 = askopenfilenames(parent=jendela_tanya, title="Directory")
                if t1:
                    t1 = '" "'.join(str(x) for x in t1)
                    t1 = '"'+t1+'"'
                    t1 = t1.replace("/", "\\")
                config_entry(tujuan, ttujuan, t1)
            else:
                t0 = askdirectory(parent=jendela_tanya, title="Directory")
                if t0:
                    t0 = t0.replace("/", "\\")
                    t0 = '"'+t0+'"'
                config_entry(tujuan, ttujuan, t0)

    blnama = Frame(jendela_tanya, bg=latar_belakang)
    blnama.pack(padx=10, fill='x', expand=True)
    tlnama = Label(blnama, text="Name:", bg=latar_belakang, fg=warna_teks)
    tlnama.pack(fill="x", side="left")

    benama = Frame(jendela_tanya, bg=latar_belakang, height=tinggi_tombol)
    benama.pack(padx=10, fill='x', expand=True)
    tnama = Entry(benama)
    tnama.pack(side="left", fill="both", expand=True)
    tnama.focus_set()
    gaya_entry(tnama, nama, jendela_tanya, "name", true_false)
    bnama = Label(benama, text="")
    bnama.pack(side="right", fill="y")
    gaya_tombol(bnama, d_file_folder, "n", s_lebar_tombol=0) #Hasilnya 14

    if edit == "edit":
        nama_lama = tnama.get()
    #
    bldirektori = Frame(jendela_tanya, bg=latar_belakang)
    bldirektori.pack(padx=10, fill='x', expand=True)
    tldirektori = Label(bldirektori, text="Source path:", bg=latar_belakang, fg=warna_teks)
    tldirektori.pack(fill="x", side="left")

    bedirektori = Frame(jendela_tanya, bg=latar_belakang)
    bedirektori.pack(padx=10, fill='x', expand=True)
    tdirektori = Entry(bedirektori)
    tdirektori.pack(side="left", fill="both", expand=True)
    gaya_entry(tdirektori, direktori, jendela_tanya, "path", true_false)
    bdcentang = Checkbutton(bedirektori, text="Select (File)")
    bdcentang.pack(side="right")
    gaya_tombol_cek(bdcentang, d_f_or_f)
    bdirektori = Label(bedirektori, text="...")
    bdirektori.pack(side="right", fill="y")
    gaya_tombol(bdirektori, d_file_folder, "dr", s_lebar_tombol=lebar_tombol_titik)
    b2direktori = Label(bedirektori, text="+...")
    b2direktori.pack(side="right", fill="y")
    gaya_tombol(b2direktori, d_file_folder, "dr", s_lebar_tombol=lebar_tombol_titik, more_callobj="tambahkan")
    #
    bltujuan = Frame(jendela_tanya, bg=latar_belakang)
    bltujuan.pack(padx=10, fill='x', expand=True)
    tltujuan = Label(bltujuan, text="Destination path:", bg=latar_belakang, fg=warna_teks)
    tltujuan.pack(fill="x", side="left")

    betujuan = Frame(jendela_tanya, bg=latar_belakang)
    betujuan.pack(padx=10, fill='x', expand=True)
    ttujuan = Entry(betujuan)
    ttujuan.pack(side="left", fill="both", expand=True)
    gaya_entry(ttujuan, tujuan, jendela_tanya, "path", true_false)
    btcentang = Checkbutton(betujuan, text="Become (File)")
    btcentang.pack(side="right")
    gaya_tombol_cek(btcentang, t_f_or_f)
    btujuan = Label(betujuan, text="...")
    btujuan.pack(side="right", fill="y")
    gaya_tombol(btujuan, d_file_folder, "tj", s_lebar_tombol=lebar_tombol_titik)
    b2tujuan = Label(betujuan, text="+...")
    b2tujuan.pack(side="right", fill="y")
    gaya_tombol(b2tujuan, d_file_folder, "tj", s_lebar_tombol=lebar_tombol_titik, more_callobj="tambahkan")
    #
    if edit == "edit":
        bbbuat = Frame(jendela_tanya)
        bbbuat.pack(padx=10, fill='x', expand=True)
        mbuat = Label(bbbuat, text="Add")
        mbuat.pack(fill="x")
        gaya_tombol(mbuat, buat, edit, more_callobj=nama_lama)
    else:
        bbbuat = Frame(jendela_tanya)
        bbbuat.pack(padx=10, fill='x', expand=True)
        mbuat = Label(bbbuat, text="Add")
        mbuat.pack(fill="x")
        gaya_tombol(mbuat, buat, "")
    #
    if edit == "edit":
        def return_cmd(event):
            buat(edit, nama_lama)
    else:
        def return_cmd(event):
            buat("")
    jendela_tanya.bind("<Return>", return_cmd)

    tnama.bind("<Up>", lambda e:ttujuan.focus_set())
    tdirektori.bind("<Up>", lambda e:tnama.focus_set())
    ttujuan.bind("<Up>", lambda e:tdirektori.focus_set())

    tnama.bind("<Down>", lambda e:tdirektori.focus_set())
    tdirektori.bind("<Down>", lambda e:ttujuan.focus_set())
    ttujuan.bind("<Down>", lambda e:tnama.focus_set())
    #
    def cek_entry():
        teks_entry = tdirektori.get()
        cek_di_entry = teks_entry.count('"')
        if cek_di_entry > 2:
            btcentang.deselect()
            btcentang["state"] = "disabled"
        else:
            btcentang["state"] = "normal"
        jendela_tanya.after(200, cek_entry)
    cek_entry()

def sunting_file():
    global jendela_tanya
    if len(fperintah) == 1 or len(tperintah) == 1 or len(snama) == 1:
        nama.set(snama[0])
        direktori.set(fperintah[0])
        tujuan.set(tperintah[0])
        tipe.set(ntipe[0])
        sbuat("edit")
    elif len(fperintah) == 0 or len(tperintah) == 0 or len(snama) == 0:
        showerror(
            title="Error",
            message="You not selected anything"
        )
    else:
        showerror(
            title="Error",
            message="You cannot select more than one file!"
        )

def hapus_file():
    if snama: #Jika ada
        ask = askokcancel(
            title="Warning",
            message="Are you sure you want to delete it?\n(Deleted file/files can't be restored)",
            icon=WARNING
        )
        if ask: #Jika "Ok"
            for f, t in zip(snama, ntipe):
                if t == ".slbre":
                    os.remove("Paths\\"+f+".slbre")
                else: #apapun itu akan dianggap .slbr
                    os.remove("Paths\\"+f+".slbr")

            snama.clear()
            fperintah.clear()
            tperintah.clear()
            ntipe.clear()
    else:
        showerror(
            title="Error",
            message="You not selected anything"
        )

def jalankan_perintah(copy_cut):
    if snama and fperintah and tperintah:
        hasil = perintah(snama, fperintah, tperintah, copy_cut, konfirmasi_timpa.get())
        if hasil.count("SUCCESSFULLY"):
            showinfo(
                title = "Info",
                message = hasil
            )
        elif hasil == "CANCELED":
            showinfo(
                title = "Info",
                message = "CANCELED BY USER"
            )
        else:
            showerror(
                title = "Error",
                message = hasil
            )
    else:
        showerror(
            title = "Error",
            message = "You not selected anything"
        )

def masukkan_password():
    jendela_password = Toplevel()
    jendela_password.grab_set()
    jendela_password.title("Insert Password")
    jendela_password.resizable(0,0)
    jendela_password.configure(bg=latar_belakang)
    jendela_password.focus_set()
    #GUI
    wt = jendela_utama.winfo_width() - 300
    ht = jendela_utama.winfo_height() - 420

    xt = (lebar_layar/2) - (wt/2)
    yt = (tinggi_layar/2) - (ht/2)

    jendela_password.geometry('%dx%d+%d+%d' % (wt, ht, xt, yt))

    blpw = Frame(jendela_password, bg=latar_belakang)
    blpw.pack(padx=10, fill='x', expand=True)
    tlpw = Label(blpw, text="Password:", bg=latar_belakang, fg=warna_teks)
    tlpw.pack(fill="x", side="left")

    bepw = Frame(jendela_password, bg=latar_belakang, height=tinggi_tombol)
    bepw.pack(padx=10, fill='x', expand=True)
    tpw = Entry(bepw)
    tpw.pack(side="left", fill="both", expand=True)
    tpw.focus_set()
    gaya_entry(tpw, password, jendela_password, "password")

daftar_program = []

def utama(*perbarui: bool):
    global r, c, fl, l, folder_jalur, bingkai, kesalahan, dijalankan, daftar_program
    if perbarui:
        dijalankan = 1
        jendela_utama.after(500, perbarui_GUI)
    else:
        bikin_bingkai()
        r = 0
        c = 0
        kesalahan = []
        # kesalahan_modifikasi = []
        folder_jalur = r'Paths'
        p = sorted(Path(folder_jalur).iterdir(), key=os.path.getctime)
        l = [] #daftar program yang untuk dijalankan
        for x in p:
            p_cache = "".join(str(x))
            p_cache = p_cache.replace(folder_jalur + "\\", "")
            l.append(p_cache)
        fl = Frame(bingkai, bg="#3c4038") #Warna bg harus sama dengan canvas dan bingkai
        fl.grid()
        if l != daftar_program:
            daftar_program.clear()
            daftar_program = l #perbarui

def perbarui_GUI():
    global r, c, fl, l, folder_jalur, bingkai, kesalahan, dijalankan, daftar_program, jalankan_progress
    kesalahan = []
    p = sorted(Path(folder_jalur).iterdir(), key=os.path.getctime)
    l = [] #daftar program yang untuk dijalankan
    for x in p:
        p_cache = "".join(str(x))
        p_cache = p_cache.replace(folder_jalur + "\\", "")
        l.append(p_cache)
    kurangi = False #set as default
    if dijalankan:
        daftar_baru = l
    elif set(daftar_program) > set(l): #perbarui
        daftar_baru = list(set(daftar_program)-set(l)) #program dikurangi
        kurangi = True
    elif set(daftar_program) < set(l): #perbarui
        daftar_baru = list(set(l)-set(daftar_program)) #program tambahan yang belum dieksekusi
    else:
        daftar_baru = []
    total_daftar = len(daftar_baru)
    # awal_eksekusi = time()
    for n, p in enumerate(daftar_baru):
        global calling
        calling = "" #reset to not callable
        cache_name = os.path.splitext(p)[0]
        cache_ext = os.path.splitext(p)[1].replace(".", "")
        if kurangi: #same as bool()
            # globals()[f"nama_{}"]
            # globals()[f"cb_{}"]
            # globals()[f"var{}"]
            # globals()[f"Label_{}"]
            globals()[f"cb_{cache_name}_{cache_ext}"].destroy()
            globals()[f"Label_{cache_name}_{cache_ext}"].destroy()
            del globals()[f"nama_{cache_name}_{cache_ext}"], globals()[f"cb_{cache_name}_{cache_ext}"], globals()[f"var{cache_name}_{cache_ext}"], globals()[f"Label_{cache_name}_{cache_ext}"]
        else:
            if os.path.isfile(os.path.join(folder_jalur, p)) and ".slbr" in os.path.splitext(p): #.slbr mean SALBAR file
                try:
                    raw = open(folder_jalur+"\\"+p, "rb").read().decode("utf-8")
                    deformat = my_deformat(raw)
                    exec(compile(deformat, "", "exec")) #lebih mudah untuk berbagi object dibandingkan dengan impor modul
                    calling()
                    globals()[f"Label_{cache_name}_{cache_ext}"] = Label(fl, text='         SLBR', font=font_teks, bg=latar_belakang_bingkai, fg=label_slbr)
                    globals()[f"Label_{cache_name}_{cache_ext}"].grid(column=1,row=r, sticky='nsw', pady=1)
                    r+=1
                except Exception as error:
                    print(error)
                    kesalahan.append(p)
            elif os.path.isfile(os.path.join(folder_jalur, p)) and ".slbre" in os.path.splitext(p) and ada_pekerja: #.slbre mean SALBAR file with encrypt
                try:
                    raw = open(folder_jalur+"\\"+p, "r").read()
                    decompile = my_decompile(raw) #must in str
                    deformat = my_deformat(decompile)
                    exec(compile(deformat, "", "exec")) #lebih mudah untuk berbagi object dibandingkan dengan impor modul
                    calling()
                    globals()[f"Label_{cache_name}_{cache_ext}"] = Label(fl, text='         SLBRE', font=font_teks, bg=latar_belakang_bingkai, fg=label_slbre)
                    globals()[f"Label_{cache_name}_{cache_ext}"].grid(column=1,row=r, sticky='nsw', pady=1)
                    r+=1
                except Exception as error:
                    kesalahan.append(p)
                    print(error)
            # if int(time()-awal_eksekusi) > 1:
            if jalankan_progress:
                Thread(target=kemajuan, args=(n, total_daftar)).start()
    if not total_daftar:
        jendela_progress.grab_release()
        jendela_progress.withdraw()
        jalankan_progress = False
    if kurangi: #must update row
        for n, i in enumerate(l):
            cache_name = os.path.splitext(i)[0]
            cache_ext = os.path.splitext(p)[1].replace(".", "")
            globals()[f"cb_{cache_name}_{cache_ext}"].grid(row=n)
            globals()[f"Label_{cache_name}_{cache_ext}"].grid(row=n)
        r = len(l)
    if kesalahan:
        kslhn = ""
        for f in kesalahan:
            fs = '"'+f+'"'
            if kslhn:
                kslhn += ", "+fs
            else:
                kslhn = fs
        # print("Error:"+kslhn)
        if kslhn.find(",") == -1:
            word = "that"
            adalah = " is "
            more_than_one = " "
        else:
            word = "which"
            adalah = " are "
            more_than_one = "s "
        showerror(
            title="Error",
            message="We found the error file"+more_than_one+ word +adalah+ kslhn
        )
    if l != daftar_program:
        daftar_program.clear()
        daftar_program = l
    dijalankan = 0

def perbarui_pilihan(obj: list):
    row_cache = globals()[f"cb_{obj[2]}_{obj[1]}"].grid_info()["row"] #get help from "https://stackoverflow.com/questions/37731654/how-to-retrieve-the-row-and-column-information-of-a-button-and-use-this-to-alter"
    globals()[f"cb_{obj[2]}_{obj[1]}"].destroy() #hapus yang lama (berupa nama lama)
    globals()[f"Label_{obj[2]}_{obj[1]}"].destroy() #hapus yang lama (berupa nama lama)
    del globals()[f"cb_{obj[2]}_{obj[1]}"], globals()[f"Label_{obj[2]}_{obj[1]}"] #menghapus yang lama (berguna jika dalam mode edit dan tidak berguna jika sebaliknya)
    kesalahan = []
    p = f"{obj[0]}.{obj[1]}" #buat yang baru (berupa nama baru yang diedit)
    if obj[1] == "slbr": #.slbr mean SALBAR file
        try:
            raw = open(folder_jalur+f"\\"+p, "rb").read().decode("utf-8")
            deformat = my_deformat(raw)
            exec(compile(deformat, "", "exec")) #lebih mudah untuk berbagi object dibandingkan dengan impor modul
            calling()
            globals()[f"Label_{obj[0]}_{obj[1]}"] = Label(fl, text='         SLBR', font=font_teks, bg=latar_belakang_bingkai, fg=label_slbr)
            globals()[f"Label_{obj[0]}_{obj[1]}"].grid(column=1,row=row_cache, sticky='nsw', pady=1)
        except Exception as error:
            print(error)
            kesalahan.append(p)
    elif obj[1] == "slbre": #.slbre mean SALBAR file with encrypt
        try:
            raw = open(folder_jalur+f"\\"+p, "r").read()
            decompile = my_decompile(raw) #must in str
            deformat = my_deformat(decompile)
            exec(compile(deformat, "", "exec")) #lebih mudah untuk berbagi object dibandingkan dengan impor modul
            calling()
            globals()[f"Label_{obj[0]}_{obj[1]}"] = Label(fl, text='         SLBRE', font=font_teks, bg=latar_belakang_bingkai, fg=label_slbre)
            globals()[f"Label_{obj[0]}_{obj[1]}"].grid(column=1,row=row_cache, sticky='nsw', pady=1)
        except Exception as error:
            kesalahan.append(p)
            print(error)
    p = sorted(Path(folder_jalur).iterdir(), key=os.path.getctime)
    l = [] #daftar program yang untuk dijalankan
    for x in p:
        p_cache = "".join(str(x))
        p_cache = p_cache.replace(folder_jalur + "\\", "")
        l.append(p_cache)
    for n, i in enumerate(l): #perbarui baris setiap pilihan untuk seluruh pilihan
        p = os.path.basename(i)
        cache_name = os.path.splitext(p)[0]
        cache_ext = os.path.splitext(p)[1].replace(".", "")
        globals()[f"cb_{cache_name}_{cache_ext}"].grid(row=n)
        globals()[f"Label_{cache_name}_{cache_ext}"].grid(row=n)
    if kesalahan:
        kslhn = ""
        for f in kesalahan:
            fs = '"'+f+'"'
            if kslhn:
                kslhn += ", "+fs
            else:
                kslhn = fs
        # print("Error:"+kslhn)
        if kslhn.find(",") == -1:
            word = "that"
            adalah = " is "
            more_than_one = " "
        else:
            word = "which"
            adalah = " are "
            more_than_one = "s "
        showerror(
            title="Error",
            message="We found the error file"+more_than_one+ word +adalah+ kslhn
        )

utama()

option_secure = Checkbutton(bingkai_opsi, text = "New with .slbre (Encrypt) (Too heavy!)")
option_secure.pack(side=LEFT)
gaya_tombol_cek(option_secure, konfirmasi_aman, latar_belakang=latar_belakang_bingkai_tombol_options)
if not ada_pekerja:
    option_secure["state"] = "disabled"

baru = Label(jendela_utama, text = "New", relief="flat")
baru.pack(side=LEFT, fill=Y)
gaya_tombol(baru, sbuat, "")
sunting = Label(jendela_utama, text = "Edit")
sunting.pack(side=LEFT, fill=Y)
gaya_tombol(sunting, sunting_file, "tidak perlu")
hapus = Label(jendela_utama, text = "Delete")
hapus.pack(side=LEFT, fill=Y)
gaya_tombol(hapus, hapus_file, "tidak perlu")

#Jika SIDE-nya RIGHT, harus didaftarkan secara terbalik
option_password = Label(jendela_utama, text = "Unlock")
option_password.pack(side=RIGHT, fill=Y)
gaya_tombol(option_password, masukkan_password, "tidak perlu")
salin = Label(jendela_utama, text = "Copy")
salin.pack(side=RIGHT, fill=Y)
gaya_tombol(salin, jalankan_perintah, "salin")
potong = Label(jendela_utama, text = "Cut")
potong.pack(side=RIGHT, fill=Y)
gaya_tombol(potong, jalankan_perintah, "potong")
timpa = Checkbutton(jendela_utama, text = "Overwrites all") #bg harus sama dengan jendela_utama
timpa.pack(side=RIGHT, fill=Y)
gaya_tombol_cek(timpa, konfirmasi_timpa)

p = os.getcwd()+"\\Paths"
global o
o = os.listdir(p)
for i in o:
    if i.endswith(".slbr"):
        pass
    elif i.endswith(".slbre"):
        pass
    else:
        o.remove(i)
def perbarui(edit, *obj):
    global o
    o_cache = os.listdir(p)
    for i in o_cache:
        # print((not i.endswith(".slbr") or not i.endswith(".slbre")), i) #I don't know why this print() returned True if i ends with ".slbr" or ".slbre"
        if i.endswith(".slbr"): # (not i.endswith(".slbr") or not i.endswith(".slbre")) doesn't work as I expected
            pass
        elif i.endswith(".slbre"):
            pass
        else:
            o_cache.remove(i)
    # print(o, o_cache)
    def perbaruikan(*user):
        global o, dijalankan, kanvas, jalankan_progress
        o = o_cache
        status=jendela_utama.state()
        if status != "zoomed":
            wpr = jendela_utama.winfo_width()
            hpr = jendela_utama.winfo_height()
            jendela_utama.geometry('%dx%d' % (wpr, hpr))
        if user:
            dijalankan = True
            jalankan_progress = True
            hancur_semua_bingkai()
            utama()
            reset_var()
            perbarui_GUI()
        else:
            perbarui_GUI()
        jendela_utama.state(status)
    if o != o_cache or edit == "edit" or edit == "user" or edit == "cmd":
        if len(o_cache) != len(o): #ditambah atau dikurangi
            perbaruikan()
        elif edit == "user":
            Thread(target=perbaruikan, args=(True,)).start()
        elif edit == "edit":
            perbarui_pilihan([obj[0], obj[1], obj[2]])
        elif edit == "cmd":
            perbaruikan()
        elif not snama and not fperintah and not tperintah:
            #Jika tidak ada yang terpilih
            perbaruikan()
        #Punya 3. Masing-masing membandingkan yang lain yaitu hanya 2, jadi 3x2=6
        elif len(snama) == len(fperintah) and len(snama) == len(tperintah) and len(fperintah) == len(snama) and len(fperintah) == len(tperintah) and len(tperintah) == len(snama) and len(tperintah) == len(fperintah):
            #Jika semua sama dengan lainnya meski tidak ada (mustahil tidak ada karena akan trigger if-else pertama tentang ketiadaan)
            ask = askokcancel(
                title="Warning",
                message="Your selected will be deselect. Click Ok to continue",
                icon=WARNING
            )
            if ask:
                perbaruikan()
        elif len(snama) != len(fperintah) and len(snama) != len(tperintah) and len(fperintah) != len(snama) and len(fperintah) != len(tperintah) and len(tperintah) != len(snama) and len(tperintah) != len(fperintah):
            #Impossible to happen
            showwarning(
                title="Warning",
                message="We found a bug that list of selected [name] and/or [source directory] (in [name]) and/or [destination directory] (in [name]) not same as each other. Please send creator a message about this bug!"
            )
            perbaruikan()
        else:
            #Impossible to happen
            showwarning(
                title="Warning",
                message="We found a mysterious bug. Please send creator a message about this bug!"
            )
            perbaruikan()
    jendela_utama.after(1000, lambda:perbarui(""))

perbarui("")

def perbarui_scrollbar():
    global kanvas
    #get help from "https://stackoverflow.com/questions/70266334/update-scrollbar-in-tkinter"
    if kanvas.winfo_exists(): #get help from "https://stackoverflow.com/questions/15311698/how-to-see-if-a-widget-exists-in-tkinter"
        kanvas.configure(scrollregion=kanvas.bbox("all")) #not work if used event <configure>
    jendela_utama.after(100, perbarui_scrollbar)

perbarui_scrollbar()

diperbarui = Label(jendela_utama, text = "Refresh")
diperbarui.pack(side=TOP, fill=Y)
gaya_tombol(diperbarui, perbarui, "user")

def save_current_resize():
    if not os.path.exists("resize.ignore"):
        wcr = jendela_utama.winfo_width()
        hcr = jendela_utama.winfo_height()
        status_win = jendela_utama.state()
        teks_tambahan=""
        if status_win == "zoomed":
            teks_tambahan+="\njendela_utama.state('zoomed')"
        if wcr > lebar_layar*85/100 or hcr > tinggi_layar*85/100:
            wcr-=round(wcr*20/100)
            hcr-=round(hcr*20/100)
        teks=f"""global w, h
w={wcr}
h={hcr}{teks_tambahan}"""
        cr = open("window resize.pyi", "w")
        cr.write(teks)
        cr.close()
    else:
        try:
            os.remove("window resize.pyi")
        except:
            pass
    jendela_utama.destroy()

def save_from_delete():
    print("No, you shouldn't do that!")

jendela_progress.protocol("WM_DELETE_WINDOW", save_from_delete)

global dijalankan
dijalankan = 1
jendela_utama.after(1000, Thread(target=perbarui_GUI).start) #must Thread in order to show progress at the same time

jendela_utama.protocol("WM_DELETE_WINDOW", save_current_resize)
#only for developer
# print(f"Load Time (___end___): {(end_time := timeit())}")
# print(f"Load Time (end_time_): {(end_time_time := time())}")
# print(f"\nLoad Time (totaltime): {end_time_time-start_time_time}")
# print(f"Load Time (end-start): {end_time-start_time}")
# print(f"Load Time (start-end): {start_time-end_time}")
# print(f"Load Time (end+start): {end_time+start_time}")
# print(f"Load Time (start+end): {start_time+end_time}")
jendela_utama.mainloop()
