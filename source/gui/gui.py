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
from tkinter.messagebox import *
from tkinter.messagebox import WARNING
import os
from command import command
from file_handler import maker
import paths
import threading
from gui.styles import *
from gui import config
from gui import message_box
from gui import progress
import configurator

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
        jendela_tanya.configure(bg=background)
        jendela_tanya.focus_set()
        #GUI
        lebar_layar = root.winfo_screenwidth()
        tinggi_layar = root.winfo_screenheight()
        wt = root.winfo_width() - 22 #Hasilnya 380
        ht = root.winfo_height() - 110 #Hasilnya 220

        xt = (lebar_layar/2) - (wt/2)
        yt = (tinggi_layar/2) - (ht/2)

        jendela_tanya.geometry('%dx%d+%d+%d' % (wt, ht, xt, yt))
        #
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
            frame.config(bg=background)
            frame.pack(padx=10, fill='x', expand=True)
        
        def pack_label_1(label: Label):
            label.pack(fill="x", side="left")

        def pack_label_2(label: Label):
            label.pack(side="right", fill="y")
        
        def pack_entry(entry: Entry):
            entry.pack(side="left", fill="both", expand=True)
        
        def pack_checkbutton(checkbutton: Checkbutton):
            checkbutton.pack(side="right")

        f_label_nama = Frame(jendela_tanya)
        pack_frame(f_label_nama)
        label_nama_title = Label(f_label_nama, text="Name:", bg=background, fg=TEXT_COLOR)
        pack_label_1(label_nama_title)

        f_entry_nama = Frame(jendela_tanya, height=BUTTON_HEIGHT)
        pack_frame(f_entry_nama)
        entry_nama = Entry(f_entry_nama)
        pack_entry(entry_nama)
        entry_nama.focus_set()

        label_nama = Label(f_entry_nama, text="")
        pack_label_2(label_nama)

        config.entry(entry_nama, nama, True, label_name = label_nama)

        config.button(label_nama, d_file_folder, "n", my_width=0) #Hasilnya 14

        nama_lama = entry_nama.get()
        #
        f_label_direktori = Frame(jendela_tanya)
        pack_frame(f_label_direktori)
        label_direktori_title = Label(f_label_direktori, text="Source path:", bg=background, fg=TEXT_COLOR)
        pack_label_1(label_direktori_title)

        f_entry_direktori = Frame(jendela_tanya)
        pack_frame(f_entry_direktori)
        entry_direktori = Entry(f_entry_direktori)
        pack_entry(entry_direktori)
        config.entry(entry_direktori, direktori)
        direktori_centang = Checkbutton(f_entry_direktori, text="Select (File)")
        pack_checkbutton(direktori_centang)
        config.checkbutton(direktori_centang, d_f_or_f)
        label_direktori = Label(f_entry_direktori, text="...")
        pack_label_2(label_direktori)
        config.button(label_direktori, d_file_folder, "dr", my_width=ADD_PATH_BUTTON_WIDTH)
        label_plus_direktori = Label(f_entry_direktori, text="+...")
        pack_label_2(label_plus_direktori)
        config.button(label_plus_direktori, d_file_folder, "dr", "tambahkan", my_width=ADD_PATH_BUTTON_WIDTH)
        #
        f_label_tujuan = Frame(jendela_tanya)
        pack_frame(f_label_tujuan)
        label_tujuan_title = Label(f_label_tujuan, text="Destination path:", bg=background, fg=TEXT_COLOR)
        pack_label_1(label_tujuan_title)

        f_entry_tujuan = Frame(jendela_tanya)
        pack_frame(f_entry_tujuan)
        entry_tujuan = Entry(f_entry_tujuan)
        pack_entry(entry_tujuan)
        config.entry(entry_tujuan, tujuan)
        tujuan_centang = Checkbutton(f_entry_tujuan, text="Become (File)")
        pack_checkbutton(tujuan_centang)
        config.checkbutton(tujuan_centang, t_f_or_f)
        label_tujuan = Label(f_entry_tujuan, text="...")
        pack_label_2(label_tujuan)
        config.button(label_tujuan, d_file_folder, "tj", my_width=ADD_PATH_BUTTON_WIDTH)
        label_plus_tujuan = Label(f_entry_tujuan, text="+...")
        pack_label_2(label_plus_tujuan)
        config.button(label_plus_tujuan, d_file_folder, "tj", "tambahkan", my_width=ADD_PATH_BUTTON_WIDTH)

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
            config.button(label_buat, maker.buat, jendela_tanya, nama, direktori, tujuan, nama_edit_timpa, nama_lama)
            def return_cmd(event):
                maker.buat(jendela_tanya, nama, direktori, tujuan, nama_edit_timpa, nama_lama)
        else:
            config.button(label_buat, maker.buat, jendela_tanya, nama, direktori, tujuan, nama_edit_timpa)
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

    def _run_command(command_info, copy: bool, snama: list, fperintah: list, tperintah: list):
        """(not active) command_info = ["title", "source", "destination"]"""
        hasil = command.perintah(command_info, snama, fperintah, tperintah, copy, konfirmasi_timpa, konfirmasi_lewati)
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

    def jalankan_perintah(copy: bool, snama: list, fperintah: list, tperintah: list):
        """if copy == False: cut"""
        if snama and fperintah and tperintah:

            if configurator.config("user.yaml").get_value("warning0") != False:
                answer = message_box.create(
                                        title="Command-Warning",
                                        message="Copy/move action cannot be stopped while it is in progress, continue?",
                                        options=["Yes", "Always Yes", "No"],
                                        icon_path=messagebox_icon,
                                        button_padx=15,
                                        window_height=110,
                                        bell=True
                                        )[0]
                if answer == "Always Yes":
                        if configurator.config("user.yaml").find("warning0"):
                            configurator.config("user.yaml").change("warning0", False)
                        else:
                            configurator.config("user.yaml").add("warning0: false")

                        showinfo(
                            title="Command-Warning-Info",
                            message='''You can change this configuration in "user.yaml" file CAREFULLY if you change your mind.\nAll you have to do is remove 'warning0: false'!''' #"I know you can also change the value or delete the file"
                        )
            else:
                answer = "Yes"

            if answer in ["Yes", "Always Yes"]:
                command_info = progress.progress_bar(["title", "source", "destination"])
                threading.Thread(target=options._run_command, args=(command_info, copy, snama, fperintah, tperintah)).start()
        else:
            showerror(
                title = "Error",
                message = "You not selected anything"
            )

def tombol(root: Tk, snama: list, fperintah: list, tperintah: list, nama_edit_timpa: dict):
    global nama, direktori, tujuan, konfirmasi_timpa, konfirmasi_lewati
    nama = StringVar()
    direktori = StringVar()
    tujuan = StringVar()
    konfirmasi_timpa = IntVar()
    konfirmasi_lewati = IntVar()

    new = Label(root, text="New")
    new.pack(side=LEFT, fill=Y)
    config.button(new, options.menu, root, nama_edit_timpa, False)
    def new_bind(event):
        options.menu(root, nama_edit_timpa, False)

    edit = Label(root, text="Edit")
    edit.pack(side=LEFT, fill=Y)
    config.button(edit, options.sunting_file, root, snama, fperintah, tperintah, nama_edit_timpa)
    def edit_bind(event):
        options.sunting_file(root, snama, fperintah, tperintah, nama_edit_timpa)

    delete = Label(root, text="Delete")
    delete.pack(side=LEFT, fill=Y)
    config.button(delete, options.hapus_file, snama, fperintah, tperintah)
    def delete_bind(event):
        options.hapus_file(snama, fperintah, tperintah)

    copy = Label(root, text="Copy")
    copy.pack(side=RIGHT, fill=Y)
    config.button(copy, options.jalankan_perintah, True, snama, fperintah, tperintah)
    def copy_bind(event):
        options.jalankan_perintah(True, snama, fperintah, tperintah)

    cut = Label(root, text="Move")
    cut.pack(side=RIGHT, fill=Y)
    config.button(cut, options.jalankan_perintah, False, snama, fperintah, tperintah)
    def cut_bind(event):
        options.jalankan_perintah(False, snama, fperintah, tperintah)

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
    config.checkbutton(timpa, konfirmasi_timpa)

    atau = Label(root, text="or")
    atau.pack(side=RIGHT, fill=Y)
    config.label(atau)

    lewati = Checkbutton(root, text = "Skip", command = lewati_dicentang) #bg harus sama dengan jendela_utama
    lewati.pack(side=RIGHT, fill=Y)
    config.checkbutton(lewati, konfirmasi_lewati)

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