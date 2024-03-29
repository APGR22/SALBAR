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
import info

class options:
    def __init__(
                    self,
                    info: info._info
                ) -> None:

        self.name = StringVar()
        self.source = StringVar()
        self.destination = StringVar()

        self.info = info

        self._menu = _menu(info, self.name, self.source, self.destination)

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
        if len(self.info.list_source) == 1 or len(self.info.list_destination) == 1 or len(self.info.list_name) == 1:
            self.name.set(self.info.list_name[0])
            self.source.set(self.info.list_source[0])
            self.destination.set(self.info.list_destination[0])
            self.menu(True)
        elif len(self.info.list_source) == 0 or len(self.info.list_destination) == 0 or len(self.info.list_name) == 0:
            showerror(
                title="Error - (edit file) - 1",
                message="You not selected anything"
            )
        else:
            showerror(
                title="Error - (edit file) - 2",
                message="You cannot select more than one file!"
            )

    def delete_file(self):
        if self.info.list_name: #Jika ada
            ask = askokcancel(
                title="Warning",
                message="Are you sure you want to delete it?\n(Deleted file/files can't be restored)",
                icon=WARNING
            )
            if ask: #Jika "Ok"
                for f in self.info.list_name:
                    os.remove(paths.PATH+f+".slbr")

                self.info.list_name.clear()
                self.info.list_source.clear()
                self.info.list_destination.clear()
        else:
            showerror(
                title="Error - (delete file)",
                message="You not selected anything"
        )

    #actually only specifically for threading
    def _run_command(self, command_info: progress.progress_bar, copy: bool, thread: dict[str, bool]):
        """(not active) command_info = ["title", "source", "destination"]"""
        hasil = command.command(
                                command_info,
                                self.info,
                                copy,
                                thread
                                )
        if hasil.startswith("SUCCESSFULLY"):
            show = showinfo
            title = "Command-Info"
            message = hasil
        elif hasil.startswith("ERROR(S)"):
            show = showerror
            title = "Command-Error"
            message = hasil
        elif hasil == "CANCELED":
            show = showinfo
            title = "Command-Info"
            message = "CANCELED BY USER"
        elif hasil == "SKIP":
            show = showinfo
            title = "Command-Info"
            message = "SKIPPED BY USER"
        else:
            show = showinfo
            title = "Command-:)"
            message = hasil

        show(
            title = title,
            message = message,
            parent=self.info.root
        )

    def run_command(self, copy: bool):
        """if copy == False: cut"""
        if self.info.list_name and self.info.list_source and self.info.list_destination:

            config = configurator.config("user.yaml")
            if config.get_value("warning0") != False:
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
                        if config.find("warning0"):
                            config.change("warning0", False)
                        else:
                            config.add("warning0: false")

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
                title = "Error - (run command)",
                message = "You not selected anything"
            )



class _menu:
    def __init__(self, info: info._info, name: StringVar, source: StringVar, destination: StringVar) -> None:

        self.info = info
        self.name = name
        self.source = source
        self.destination = destination
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
                        if len(askopen) == 0:
                            askopen = ""
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
            if text != "Become (File)":
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
            maker.buat(self.menu_window, self.disable, self.name, self.source, self.destination, self.old_name, self.info.nama_edit_timpa)

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
        config.button(self.label_buat, maker.buat, self.menu_window, self.disable, self.name, self.source, self.destination, self.old_name, self.info.nama_edit_timpa)

        #config
        lebar_layar = self.info.root.winfo_screenwidth()
        tinggi_layar = self.info.root.winfo_screenheight()
        wt = self.info.root.winfo_width() - 22 #Hasilnya 380
        ht = self.info.root.winfo_height() - 110 #Hasilnya 220

        xt = (lebar_layar/2) - (wt/2)
        yt = (tinggi_layar/2) - (ht/2)

        self.menu_window.geometry('%dx%d+%d+%d' % (wt, ht, xt, yt))
    
    def disable(self):
        self.menu_window.grab_release()
        self.menu_window.withdraw()

class options_menu:
    def __init__(self, info: info._info) -> None:
        self.window = Toplevel()
        self.window.title("Configuration")
        self.window.resizable(0,0)
        self.window.configure(bg=background)

        #config
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        w = 420
        h = 50

        x = (screen_width/2) - (w/2)
        y = (screen_height/2) - (h/2)

        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        def disable_window(*event):
            self.disable()

        self.window.bind("<Escape>", disable_window)
        self.window.protocol("WM_DELETE_WINDOW", disable_window)

        self.disable()
        #start

        #bg harus sama dengan jendela

        overwrite_skip = IntVar(value=0)

        def no_overwrite_skip_checked():
            info.confirm_to_overwrite.set(0)
            info.confirm_to_skip.set(0)
        def timpa_dicentang():
            info.confirm_to_skip.set(0)
            info.confirm_to_overwrite.set(1)
        def lewati_dicentang():
            info.confirm_to_overwrite.set(0)
            info.confirm_to_skip.set(1)

        no_overwrite_skip = Radiobutton(self.window, text = "No action", command = no_overwrite_skip_checked)
        no_overwrite_skip.grid(row=1, column=0, sticky=W)
        config.radiobutton(no_overwrite_skip, overwrite_skip, 0)
        no_overwrite_skip.select()

        overwrite = Radiobutton(self.window, text = "Overwrites all", command = timpa_dicentang)
        overwrite.grid(row=1, column=1, sticky=W)
        config.radiobutton(overwrite, overwrite_skip, 1)

        skip = Radiobutton(self.window, text = "Skips all", command = lewati_dicentang)
        skip.grid(row=1, column=2, sticky=W)
        config.radiobutton(skip, overwrite_skip, 2)

        with_slbr_cpmv = Checkbutton(self.window, text = "With SALBAR copymove (slower than shutil and experimental)")
        with_slbr_cpmv.grid(row=2, column=0, columnspan=3, sticky=W)
        config.checkbutton(with_slbr_cpmv, info.confirm_to_use_c)

    def active(self):
        self.window.deiconify()
        self.window.grab_set()
        self.window.focus_set()

    def disable(self):
        self.window.grab_release()
        self.window.withdraw()