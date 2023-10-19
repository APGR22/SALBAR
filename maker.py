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
from tkinter.messagebox import *
from tkinter.messagebox import WARNING
import os
import platform
import extension
import paths

def buat(root: Tk | Toplevel, nama: StringVar, direktori: StringVar, tujuan: StringVar, daftar_nama_edit_timpa: dict = {}, nama_lama: str = ""):
    """jika nama_lama ada, maka akan dianggap edit (daftar_nama_edit diperlukan)"""
    def hapus(stri: str) -> str:
        if platform.system() == "Windows":
            while True: #menghapus jika ia berkali-kali lipat adanya
                if stri.startswith(" "):
                    stri = stri[1:]
                else:
                    break
        return stri
    n = hapus(nama.get())
    d = direktori.get()
    t = tujuan.get()
    if not n or not d or not t:
        return showerror(
            title="Error",
            message="You can't fill empty!",
            parent=root
        )
    if platform.system() == "Windows":
        daftar_filename = "CON, CONIN$, CONOUT$, PRN, AUX, CLOCK$, NUL, COM0, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, LPT0, LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9" #https://en.wikipedia.org/wiki/Filename
        daftar_filename = daftar_filename.split(", ")
        if n in daftar_filename:
            return showinfo(
                title = "Info",
                message = "You entered a prohibited filename. Try again",
                parent=root
            )
    if len(n) > 250:
        return showwarning(
            title="Warning",
            message="Sorry, you can't insert over 250 characters!",
            parent=root
        )
    if nama_lama: #mustahil akan dikirim "" alias kosong
        if os.path.isfile(paths.PATH+n+".slbr") and n != nama_lama:
            return showinfo(
                title = "Info",
                message = "We found the filename is the same as your entry name. Try again",
                parent=root
            )
        try:
            extension.ekstensi.make(n, d, t, nama_lama)
            daftar_nama_edit_timpa["nama"] = n
            daftar_nama_edit_timpa["nama_lama"] = nama_lama
        except Exception as error:
            return showerror(
                title="System error",
                message=error,
                parent=root
            )
        return root.destroy()
    if os.path.isfile(paths.PATH+n+".slbr"):
        ask = askokcancel(
            title="Warning",
            message='We found the filename is the same as your entry name.\nClick "Ok" to overwrite (old file will be deleted)',
            icon=WARNING,
            parent=root
        )
        if ask: #True
            os.remove(paths.PATH+n+".slbr")
            daftar_nama_edit_timpa["nama_timpa"] = n
        else:
            return ""
    try:
        extension.ekstensi.make(n, d, t)
    except Exception as error:
        return showerror(
            title="System error",
            message=error,
            parent=root
        )
    root.destroy()