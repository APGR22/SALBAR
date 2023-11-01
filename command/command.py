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

from tkinter import IntVar
#get class "do_progress" from gui/progress
from tkinter.messagebox import *
from tkinter.messagebox import WARNING
import os
import command.copycut as copycut
import paths

def make_dir(d: str):
    try:
        os.makedirs(d)
    except Exception as error: #jika sudah ada. meski ada exist_ok, itu berarti ditimpa sehingga tidak digunakan
        pass

def cek_ada(path, skip: IntVar):
    if os.path.exists(path):
        if skip.get() == 1:
            return "skip"
        ask = askyesnocancel(
            title = "Warning",
            message = f'We found the same file/folder name in "{path}", overwrite it?\nOr "Cancel" to stop the process even though the previous action has already been processed',
            icon = WARNING
        )
        return ask
    return "tidak ada"

def perintah(do_progress: type,
            list_name: list,
            list_source: list,
            list_destination: list,
            copy: bool,
            timpa: IntVar,
            skip: IntVar):
    """tanya: Overwrites for all\n
    skip: Skip overwrites"""
    do_progress.progress_start()

    list_path = [] #0 = name, 1 = list source, 2 = list destination
    berhasil = 0
    kesalahan = []
    operasi_cancel = False
    user = False
    if skip.get() == 1:
        tindakan_skip = True
    else:
        tindakan_skip = False

    for ln, ls, ld in zip(list_name, list_source, list_destination):
        source = paths.separate_path(ls)
        destination = paths.separate_path(ld)
        list_path.append((ln, source, destination))

    total_title = len(list_path)

    try:
        if copy: #sekali dijalankan
            for number_title, p in enumerate(list_path): #perulangan
                total_source = len(p[1])
                total_destination = len(p[2])
                for number_s, s in enumerate(p[1]): #perulangan dalam perulangan
                    if operasi_cancel:
                        break

                    #perulangan dalam perulangan dalam perulangan
                    for number_d, d in enumerate(p[2]):

                        do_progress.progress(
                                            p[0], #title
                                            (number_title+1, total_title), #number_title
                                            (number_s+1, total_source), #number_s
                                            s, #source_path
                                            (number_d+1, total_destination), #number_d
                                            d #destination_path
                                            )

                        if os.path.isfile(s):
                            metode_file = True
                        elif os.path.isdir(s):
                            metode_file = False
                        else:
                            kesalahan.append(f"{p[0]}: No source file or folder found: '{s}'")
                            continue

                        make_dir(d)

                        path = os.path.join(d, os.path.basename(s))

                        if timpa.get() == 0:
                            dicek = cek_ada(path, skip)

                            if dicek == "skip": #jika ada
                                continue
                            if dicek == True: #Yes
                                pass
                            elif dicek == False: #No
                                user = True
                                continue
                            elif dicek == None: #Cancel
                                operasi_cancel = True
                                break

                        hasil = copycut.salin(p[0], s, d, metode_file)

                        if hasil:
                            kesalahan.append(hasil)
                            continue

                        berhasil += 1
        else:
            for p in list_path: #perulangan
                for s in p[1]: #perulangan dalam perulangan
                    if operasi_cancel: #perulangan dalam perulangan dalam perulangan
                        break

                    for d in p[2]:
                        if os.path.isfile(s):
                            metode_file = True
                        elif os.path.isdir(s):
                            metode_file = False
                        else:
                            kesalahan.append(f"{p[0]}: No source file or folder found: '{s}'")
                            continue

                        make_dir(d)

                        path = os.path.join(d, os.path.basename(s))

                        if timpa.get() == 0:
                            dicek = cek_ada(path, skip)

                            if dicek == "skip": #jika ada
                                continue
                            elif dicek == True: #Yes
                                pass
                            elif dicek == False: #No
                                user = True
                                continue
                            elif dicek == None: #Cancel
                                operasi_cancel = True
                                break

                        hasil = copycut.pindah(p[0], s, d, metode_file)

                        if hasil:
                            kesalahan.append(hasil)
                            continue
                        
                        berhasil += 1
    except Exception as error:
        print(error)
        kesalahan.append(str(error))

    do_progress.progress_stop()

    if copy:
        tindakan = "COPIED"
    else:
        tindakan = "MOVED"

    if user:
        tambahan = " AND SOME CANCELLATIONS"
    elif tindakan_skip:
        tambahan = " AND SOME SKIP"
    else:
        tambahan = ""

    salah = ", ".join(kesalahan)
    if len(salah) > 160:
        with open("errors.txt", "w") as o:
            o.write("This file will be deleted and overwritten if a very long error occurs again in the future!\n\n")
            for error in kesalahan:
                o.write(error.replace("\\\\", chr(92))+"\n") #.replace() only applied when in Windows
        salah = f'(SEE "{os.path.join(os.getcwd(), "errors.txt")}")'
    if berhasil and kesalahan:
        teks = f"SUCCESSFULLY {tindakan} FILE(S) WITH ERROR(S): "+salah+tambahan
    elif berhasil and tambahan:
        teks = f"SUCCESSFULLY {tindakan} FILE(S)"+tambahan
    elif berhasil:
        teks = f"SUCCESSFULLY {tindakan} FILE(S)"
    elif tindakan_skip:
        teks = "SKIP"
    elif operasi_cancel or user:
        teks = "CANCELED"
    else:
        teks = "ERROR(S): "+salah
    return teks