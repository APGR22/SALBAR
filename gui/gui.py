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
from tkinter.ttk import Progressbar
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.messagebox import WARNING
import os
import command
import maker
import paths
import threading
from gui.styles import *
import gui.config as config

def bingkai(root: Tk):
    bingkai_utama = Frame(root)
    bingkai_utama.pack(fill=BOTH, expand=True)
    bingkai_kedua = Frame(root)
    bingkai_kedua.pack(fill=BOTH)
    kanvas = Canvas(bingkai_utama, bg=FRAME_BACKGROUND, highlightthickness=0)
    kanvas.pack(side=LEFT, fill=BOTH, expand=True)

    gulir = Scrollbar(bingkai_utama,orient=VERTICAL, command=kanvas.yview)
    gulir.pack(side=RIGHT, fill=Y)

    gulirx = Scrollbar(bingkai_kedua,orient=HORIZONTAL, command=kanvas.xview)
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

    bingkai = Frame(kanvas, bg=FRAME_BACKGROUND)

    kanvas.create_window((0,0), window=bingkai, anchor="nw")

    def perbarui_scrollbar():
        kanvas.configure(scrollregion=kanvas.bbox("all"))
        root.after(100, perbarui_scrollbar)
    
    root.after(1000, perbarui_scrollbar)

    return kanvas, bingkai

class options:
    def menu(root: Tk, nama_edit_timpa: dict = {}, edit: bool = False):
        if not edit:
            nama.set("")
            direktori.set("")
            tujuan.set("")
        jendela_tanya = Toplevel()
        jendela_tanya.grab_set()
        jendela_tanya.title("Configuration")
        jendela_tanya.resizable(0,0)
        jendela_tanya.configure(bg=BACKGROUND)
        jendela_tanya.focus_set()
        #GUI
        lebar_layar = root.winfo_screenwidth()
        tinggi_layar = root.winfo_screenheight()
        wt = root.winfo_width() - 22 #Hasilnya 380
        ht = root.winfo_height() - 110 #Hasilnya 220

        xt = (lebar_layar/2) - (wt/2)
        yt = (tinggi_layar/2) - (ht/2)

        jendela_tanya.geometry('%dx%d+%d+%d' % (wt, ht, xt, yt))

        d_f_or_f = IntVar()
        t_f_or_f = IntVar()

        def d_file_folder(dr_or_tj, *pilihan): #checkbox variables
            def config_entry(stringvar: StringVar, entry: Entry, askopen: str):
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
                        d1 = paths.replace_path_symbol(d1)
                    config_entry(direktori, entry_direktori, d1)
                else:
                    d0 = askdirectory(parent=jendela_tanya, title="Directory")
                    if d0:
                        d0 = paths.replace_path_symbol(d0)
                        d0 = '"'+d0+'"'
                    config_entry(direktori, entry_direktori, d0)
            elif dr_or_tj == "tj":
                if (t_f_or_f.get() == 1):
                    t1 = askopenfilenames(parent=jendela_tanya, title="Directory")
                    if t1:
                        t1 = '" "'.join(str(x) for x in t1)
                        t1 = '"'+t1+'"'
                        t1 = paths.replace_path_symbol(t1)
                    config_entry(tujuan, entry_tujuan, t1)
                else:
                    t0 = askdirectory(parent=jendela_tanya, title="Directory")
                    if t0:
                        t0 = paths.replace_path_symbol(t0)
                        t0 = '"'+t0+'"'
                    config_entry(tujuan, entry_tujuan, t0)

        def pack_frame(frame: Frame):
            frame.pack(padx=10, fill='x', expand=True)
        
        def pack_label_1(label: Label):
            label.pack(fill="x", side="left")

        def pack_label_2(label: Label):
            label.pack(side="right", fill="y")
        
        def pack_entry(entry: Entry):
            entry.pack(side="left", fill="both", expand=True)
        
        def pack_checkbutton(checkbutton: Checkbutton):
            checkbutton.pack(side="right")

        f_label_nama = Frame(jendela_tanya, bg=BACKGROUND)
        pack_frame(f_label_nama)
        label_nama_title = Label(f_label_nama, text="Name:", bg=BACKGROUND, fg=TEXT_COLOR)
        pack_label_1(label_nama_title)

        f_entry_nama = Frame(jendela_tanya, bg=BACKGROUND, height=BUTTON_HEIGHT)
        pack_frame(f_entry_nama)
        entry_nama = Entry(f_entry_nama)
        pack_entry(entry_nama)
        entry_nama.focus_set()

        label_nama = Label(f_entry_nama, text="")
        pack_label_2(label_nama)

        config.gaya_entry(entry_nama, nama, True, jendela_tanya, label_name = label_nama)

        config.gaya_tombol(label_nama, d_file_folder, "n", my_width=0) #Hasilnya 14

        nama_lama = entry_nama.get()
        #
        f_label_direktori = Frame(jendela_tanya, bg=BACKGROUND)
        pack_frame(f_label_direktori)
        label_direktori_title = Label(f_label_direktori, text="Source path:", bg=BACKGROUND, fg=TEXT_COLOR)
        pack_label_1(label_direktori_title)

        f_entry_direktori = Frame(jendela_tanya, bg=BACKGROUND)
        pack_frame(f_entry_direktori)
        entry_direktori = Entry(f_entry_direktori)
        pack_entry(entry_direktori)
        config.gaya_entry(entry_direktori, direktori)
        direktori_centang = Checkbutton(f_entry_direktori, text="Select (File)")
        pack_checkbutton(direktori_centang)
        config.gaya_tombol_cek(direktori_centang, d_f_or_f)
        label_direktori = Label(f_entry_direktori, text="...")
        pack_label_2(label_direktori)
        config.gaya_tombol(label_direktori, d_file_folder, "dr", my_width=ADD_PATH_BUTTON_WIDTH)
        label_plus_direktori = Label(f_entry_direktori, text="+...")
        pack_label_2(label_plus_direktori)
        config.gaya_tombol(label_plus_direktori, d_file_folder, "dr", "tambahkan", my_width=ADD_PATH_BUTTON_WIDTH)
        #
        f_label_tujuan = Frame(jendela_tanya, bg=BACKGROUND)
        pack_frame(f_label_tujuan)
        label_tujuan_title = Label(f_label_tujuan, text="Destination path:", bg=BACKGROUND, fg=TEXT_COLOR)
        pack_label_1(label_tujuan_title)

        f_entry_tujuan = Frame(jendela_tanya, bg=BACKGROUND)
        pack_frame(f_entry_tujuan)
        entry_tujuan = Entry(f_entry_tujuan)
        pack_entry(entry_tujuan)
        config.gaya_entry(entry_tujuan, tujuan)
        tujuan_centang = Checkbutton(f_entry_tujuan, text="Become (File)")
        pack_checkbutton(tujuan_centang)
        config.gaya_tombol_cek(tujuan_centang, t_f_or_f)
        label_tujuan = Label(f_entry_tujuan, text="...")
        pack_label_2(label_tujuan)
        config.gaya_tombol(label_tujuan, d_file_folder, "tj", my_width=ADD_PATH_BUTTON_WIDTH)
        label_plus_tujuan = Label(f_entry_tujuan, text="+...")
        pack_label_2(label_plus_tujuan)
        config.gaya_tombol(label_plus_tujuan, d_file_folder, "tj", "tambahkan", my_width=ADD_PATH_BUTTON_WIDTH)

        entry_nama.bind("<Up>", lambda e:entry_tujuan.focus_set())
        entry_direktori.bind("<Up>", lambda e:entry_nama.focus_set())
        entry_tujuan.bind("<Up>", lambda e:entry_direktori.focus_set())

        entry_nama.bind("<Down>", lambda e:entry_direktori.focus_set())
        entry_direktori.bind("<Down>", lambda e:entry_tujuan.focus_set())
        entry_tujuan.bind("<Down>", lambda e:entry_nama.focus_set())

        frame_buat = Frame(jendela_tanya)
        pack_frame(frame_buat)
        label_buat = Label(frame_buat, text="Add")
        label_buat.pack(fill="x")
        if edit:
            config.gaya_tombol(label_buat, maker.buat, jendela_tanya, nama, direktori, tujuan, nama_edit_timpa, nama_lama)
            def return_cmd(event):
                maker.buat(jendela_tanya, nama, direktori, tujuan, nama_edit_timpa, nama_lama)
        else:
            config.gaya_tombol(label_buat, maker.buat, jendela_tanya, nama, direktori, tujuan, nama_edit_timpa)
            def return_cmd(event):
                maker.buat(jendela_tanya, nama, direktori, tujuan, nama_edit_timpa)

        jendela_tanya.bind("<Return>", return_cmd)

        def destroy_jendela(event):
            jendela_tanya.destroy()

        jendela_tanya.bind("<Escape>", destroy_jendela)

    def sunting_file(root: Tk, snama: list, fperintah: list, tperintah: list, nama_edit_timpa: dict):
        if len(fperintah) == 1 or len(tperintah) == 1 or len(snama) == 1:
            nama.set(snama[0])
            direktori.set(fperintah[0])
            tujuan.set(tperintah[0])
            options.menu(root, nama_edit_timpa, True)
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

    def hapus_file(snama: list, fperintah: list, tperintah: list):
        if snama: #Jika ada
            ask = askokcancel(
                title="Warning",
                message="Are you sure you want to delete it?\n(Deleted file/files can't be restored)",
                icon=WARNING
            )
            if ask: #Jika "Ok"
                for f in snama:
                    os.remove(paths.PATH+f+".slbr")

                snama.clear()
                fperintah.clear()
                tperintah.clear()
        else:
            showerror(
                title="Error",
                message="You not selected anything"
        )

    def jalankan_perintah(progress_window: Toplevel, progress: Progressbar, copy: bool, snama: list, fperintah: list, tperintah: list):
        """if copy == False: cut"""
        if snama and fperintah and tperintah:
            hasil = command.perintah(progress_window, progress, snama, fperintah, tperintah, copy, konfirmasi_timpa, konfirmasi_lewati)
            if hasil.count("SUCCESSFULLY"):
                showinfo(
                    title = "Command-Info",
                    message = hasil
                )
            elif hasil == "CANCELED":
                showinfo(
                    title = "Command-Info",
                    message = "CANCELED BY USER"
                )
            elif hasil == "SKIP":
                showinfo(
                    title = "Command-Info",
                    message = "SKIPPED BY USER"
                )
            else:
                showerror(
                    title = "Command-Error",
                    message = hasil
                )
        else:
            showerror(
                title = "Error",
                message = "You not selected anything"
            )

def tombol(root: Tk, snama: list, fperintah: list, tperintah: list, nama_edit_timpa: dict, progress_window: Toplevel, progress: Progressbar):
    global nama, direktori, tujuan, konfirmasi_timpa, konfirmasi_lewati
    nama = StringVar()
    direktori = StringVar()
    tujuan = StringVar()
    konfirmasi_timpa = IntVar()
    konfirmasi_lewati = IntVar()

    new = Label(root, text="New")
    new.pack(side=LEFT, fill=Y)
    config.gaya_tombol(new, options.menu, root, nama_edit_timpa, False)
    def new_bind(event):
        options.menu(root, nama_edit_timpa, False)

    edit = Label(root, text="Edit")
    edit.pack(side=LEFT, fill=Y)
    config.gaya_tombol(edit, options.sunting_file, root, snama, fperintah, tperintah, nama_edit_timpa)
    def edit_bind(event):
        options.sunting_file(root, snama, fperintah, tperintah, nama_edit_timpa)

    delete = Label(root, text="Delete")
    delete.pack(side=LEFT, fill=Y)
    config.gaya_tombol(delete, options.hapus_file, snama, fperintah, tperintah)
    def delete_bind(event):
        options.hapus_file(snama, fperintah, tperintah)

    copy = Label(root, text="Copy")
    copy.pack(side=RIGHT, fill=Y)
    config.gaya_tombol(copy, options.jalankan_perintah, progress_window, progress, True, snama, fperintah, tperintah, thread = threading.Thread)
    def copy_bind(event):
        threading.Thread(target = options.jalankan_perintah, args = (progress_window, progress, True, snama, fperintah, tperintah)).start()

    cut = Label(root, text="Cut")
    cut.pack(side=RIGHT, fill=Y)
    config.gaya_tombol(cut, options.jalankan_perintah, progress_window, progress, False, snama, fperintah, tperintah, thread = threading.Thread)
    def cut_bind(event):
        threading.Thread(target = options.jalankan_perintah, args=(progress_window, progress, False, snama, fperintah, tperintah)).start()

    def timpa_dicentang():
        if konfirmasi_timpa.get() == 1:
            timpa.select()
            lewati.deselect()
    def lewati_dicentang():
        if konfirmasi_lewati.get() == 1:
            timpa.deselect()
            lewati.select()

    timpa = Checkbutton(root, text = "Overwrites all", command = timpa_dicentang) #bg harus sama dengan jendela_utama
    timpa.pack(side=RIGHT, fill=Y)
    config.gaya_tombol_cek(timpa, konfirmasi_timpa)

    atau = Label(root, text="or")
    atau.pack(side=RIGHT, fill=Y)
    config.gaya_label(atau)

    lewati = Checkbutton(root, text = "Skip", command = lewati_dicentang) #bg harus sama dengan jendela_utama
    lewati.pack(side=RIGHT, fill=Y)
    config.gaya_tombol_cek(lewati, konfirmasi_lewati)

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