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
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.messagebox import WARNING
import os
from command import command
import paths
import threading
from gui.styles import *
from gui import config
from gui import message_box
from gui import progress
import configurator
from file_handler import maker

class options:
    def __init__(
                    self,
                    root: Tk,
                    list_name: list[str],
                    list_source: list[str],
                    list_destination: list[str],
                    confirm_to_overwrite: IntVar,
                    confirm_to_skip: IntVar,
                    nama_edit_timpa: dict
                ) -> None:

        self.name = StringVar()
        self.source = StringVar()
        self.destination = StringVar()

        self.root = root
        self.list_name = list_name
        self.list_source = list_source
        self.list_destination = list_destination
        self.confirm_to_overwrite = confirm_to_overwrite
        self.confirm_to_skip = confirm_to_skip
        self.nama_edit_timpa = nama_edit_timpa

        self._menu = _menu(self.root, self.name, self.source, self.destination, self.nama_edit_timpa)

    def menu(
                self,
                edit: bool = False
            ):
        if not edit:
            self.name.set("")
            self.source.set("")
            self.destination.set("")

        self._menu.active(edit)


    def edit_file(self):
        if len(self.list_source) == 1 or len(self.list_destination) == 1 or len(self.list_name) == 1:
            self.name.set(self.list_name[0])
            self.source.set(self.list_source[0])
            self.destination.set(self.list_destination[0])
            self.menu(True)
        elif len(self.list_source) == 0 or len(self.list_destination) == 0 or len(self.list_name) == 0:
            showerror(
                title="Error",
                message="You not selected anything"
            )
        else:
            showerror(
                title="Error",
                message="You cannot select more than one file!"
            )

    def delete_file(self):
        if self.list_name: #Jika ada
            ask = askokcancel(
                title="Warning",
                message="Are you sure you want to delete it?\n(Deleted file/files can't be restored)",
                icon=WARNING
            )
            if ask: #Jika "Ok"
                for f in self.list_name:
                    os.remove(paths.PATH+f+".slbr")

                self.list_name.clear()
                self.list_source.clear()
                self.list_destination.clear()
        else:
            showerror(
                title="Error",
                message="You not selected anything"
        )

    #actually only specifically for threading
    def _run_command(self, command_info: progress.progress_bar, copy: bool, thread: dict[str, bool]):
        """(not active) command_info = ["title", "source", "destination"]"""
        hasil = command.perintah(command_info, self.list_name, self.list_source, self.list_destination, copy, self.confirm_to_overwrite, self.confirm_to_skip, thread)
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

    def run_command(self, copy: bool):
        """if copy == False: cut"""
        if self.list_name and self.list_source and self.list_destination:

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
                thread = {"active": True}
                command_info = progress.progress_bar(["title", "source", "destination"], thread)
                threading.Thread(target=self._run_command, args=(command_info, copy, thread)).start()
        else:
            showerror(
                title = "Error",
                message = "You not selected anything"
            )



class _menu:
    def __init__(self, root: Tk, name: StringVar, source: StringVar, destination: StringVar, nama_edit_timpa: dict) -> None:

        self.name = name
        self.source = source
        self.destination = destination
        self.nama_edit_timpa = nama_edit_timpa
        self.root = root
        self.old_name = ""

        self.menu_window = Toplevel()
        self.menu_window.title("Configuration")
        self.menu_window.resizable(0,0)
        self.menu_window.configure(bg=background)
        self.disable()
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
                    d1 = askopenfilenames(parent=self.menu_window, title="Directory")
                    # print(d1)
                    if d1:
                        d1 = '" "'.join(str(x) for x in d1)
                        d1 = '"'+d1+'"'
                        d1 = paths.replace_path_symbol(d1)
                    config_entry(self.source, entry_direktori, d1)
                else:
                    d0 = askdirectory(parent=self.menu_window, title="Directory")
                    if d0:
                        d0 = paths.replace_path_symbol(d0)
                        d0 = '"'+d0+'"'
                    config_entry(self.source, entry_direktori, d0)
            elif dr_or_tj == "tj":
                if (t_f_or_f.get() == 1):
                    t1 = askopenfilenames(parent=self.menu_window, title="Directory")
                    if t1:
                        t1 = '" "'.join(str(x) for x in t1)
                        t1 = '"'+t1+'"'
                        t1 = paths.replace_path_symbol(t1)
                    config_entry(self.destination, entry_tujuan, t1)
                else:
                    t0 = askdirectory(parent=self.menu_window, title="Directory")
                    if t0:
                        t0 = paths.replace_path_symbol(t0)
                        t0 = '"'+t0+'"'
                    config_entry(self.destination, entry_tujuan, t0)

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

        f_label_nama = Frame(self.menu_window)
        pack_frame(f_label_nama)
        label_nama_title = Label(f_label_nama, text="Name:", bg=background, fg=TEXT_COLOR)
        pack_label_1(label_nama_title)

        f_entry_nama = Frame(self.menu_window, height=BUTTON_HEIGHT)
        pack_frame(f_entry_nama)
        self.entry_nama = Entry(f_entry_nama)
        pack_entry(self.entry_nama)

        label_nama = Label(f_entry_nama, text="")
        pack_label_2(label_nama)

        config.entry(self.entry_nama, self.name, True, label_name = label_nama)

        config.button(label_nama, d_file_folder, "n", my_width=0) #Hasilnya 14

        #
        raw_title = ["Source path:", "Destination path:"]
        raw_stringvar = [self.source, self.destination]
        raw_local = ["entry_source", "entry_destination"]
        raw_text = ["Select (File)", "Become (File)"]
        raw_intvar = [d_f_or_f, t_f_or_f]
        raw_arg = ["dr", "tj"]

        for title, stringvar, local, text, intvar, arg in zip(raw_title, raw_stringvar, raw_local, raw_text, raw_intvar, raw_arg):
            f_label = Frame(self.menu_window)
            pack_frame(f_label)
            label_title = Label(f_label, text=title, bg=background, fg=TEXT_COLOR)
            pack_label_1(label_title)

            f_entry = Frame(self.menu_window)
            pack_frame(f_entry)
            entry = Entry(f_entry)
            pack_entry(entry)
            locals()[local] = entry
            config.entry(entry, stringvar)
            centang = Checkbutton(f_entry, text=text)
            pack_checkbutton(centang)
            config.checkbutton(centang, intvar)
            label = Label(f_entry, text="...")
            pack_label_2(label)
            config.button(label, d_file_folder, arg, my_width=ADD_PATH_BUTTON_WIDTH)
            label_plus = Label(f_entry, text="+...")
            pack_label_2(label_plus)
            config.button(label_plus, d_file_folder, arg, "tambahkan", my_width=ADD_PATH_BUTTON_WIDTH)

        entry_direktori = locals()[raw_local[0]]
        entry_tujuan = locals()[raw_local[1]]

        self.entry_nama.bind("<Up>", lambda e:entry_tujuan.focus_set())
        entry_direktori.bind("<Up>", lambda e:self.entry_nama.focus_set())
        entry_tujuan.bind("<Up>", lambda e:entry_direktori.focus_set())

        self.entry_nama.bind("<Down>", lambda e:entry_direktori.focus_set())
        entry_direktori.bind("<Down>", lambda e:entry_tujuan.focus_set())
        entry_tujuan.bind("<Down>", lambda e:self.entry_nama.focus_set())

        frame_buat = Frame(self.menu_window)
        pack_frame(frame_buat)
        self.label_buat = Label(frame_buat, text="Add")
        self.label_buat.pack(fill="x")

        def return_cmd(event):
            maker.buat(self.menu_window, self.disable, self.name, self.source, self.destination, self.old_name, self.nama_edit_timpa)

        self.menu_window.bind("<Return>", return_cmd)

        def disable_window(*event):
            self.disable()

        self.menu_window.bind("<Escape>", disable_window)
        self.menu_window.protocol("WM_DELETE_WINDOW", disable_window)

    def active(self, edit: bool):
        self.menu_window.deiconify()
        self.menu_window.grab_set()
        self.menu_window.focus_set()

        if edit:
            self.old_name = self.name.get()
        else:
            self.old_name = ""

        self.entry_nama.focus_set()

        #to be able to accept changes at any time
        config.button(self.label_buat, maker.buat, self.menu_window, self.disable, self.name, self.source, self.destination, self.old_name, self.nama_edit_timpa)

        #config
        lebar_layar = self.root.winfo_screenwidth()
        tinggi_layar = self.root.winfo_screenheight()
        wt = self.root.winfo_width() - 22 #Hasilnya 380
        ht = self.root.winfo_height() - 110 #Hasilnya 220

        xt = (lebar_layar/2) - (wt/2)
        yt = (tinggi_layar/2) - (ht/2)

        self.menu_window.geometry('%dx%d+%d+%d' % (wt, ht, xt, yt))
    
    def disable(self):
        self.menu_window.grab_release()
        self.menu_window.withdraw()