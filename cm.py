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

import shutil
import os
from tkinter.messagebox import *
from tkinter.messagebox import WARNING

def perintah(list_name: list, list_source: list, list_destination: list, perintah: str, tanya: int) -> str: #using annotations so that it is clear to me what needs to be included
    user = False
    operasi = True
    keberhasilan = 0
    kegagalan = 0
    cache = ""
    for ln, ls, ld in zip(list_name, list_source, list_destination): #setiap perintah
        source = ls.replace('" "', '"')
        source = source.split('"')
        while True:
            try:
                source.remove("")
            except:
                break #buat daftar untuk setiap jalur
        destination = ld.replace('" "', '"')
        destination = destination.split('"')
        while True:
            try:
                destination.remove("")
            except:
                break #buat daftar untuk setiap jalur
        if perintah == "salin":
            for s in source: #setiap jalur sumber
                if operasi:
                    for d in destination: #setiap jalur tujuan
                        try:
                            metode = None
                            if os.path.basename(s).count(".") and os.path.exists(s):
                                metode = "file"
                            else:
                                metode = "folder"
                            if os.path.basename(d).count(".") and d.count("\\") and not os.path.isdir(os.path.dirname(d)) and os.path.exists(s): #file in destination
                                os.makedirs(os.path.dirname(d))
                            elif not os.path.isdir(d) and not os.path.basename(d).count(".") and os.path.exists(s): #folder in destination
                                os.makedirs(d)
                            if os.path.exists(fr"{d}\{os.path.basename(s)}") and tanya == 0:
                                cache_path = fr"{d}\{os.path.basename(s)}"
                                ask = askyesnocancel(
                                    title = "Warning",
                                    message = f'We found the same file/folder name in "{cache_path}", overwrite it?\nOr "Cancel" to stop the process even though the previous action has already been processed',
                                    icon = WARNING
                                )
                                if ask == True: #Yes
                                    if metode == "file":
                                        shutil.copy(s, d)
                                    else:
                                        shutil.copytree(s, fr"{d}\{os.path.basename(s)}", dirs_exist_ok = True)
                                elif ask == False: #No
                                    keberhasilan += 1
                                    user = True
                                    continue
                                else: #Cancel
                                    operasi = False
                                    break
                            else:
                                if metode == "file":
                                    shutil.copy(s, d)
                                else:
                                    shutil.copytree(s, fr"{d}\{os.path.basename(s)}", dirs_exist_ok = True)
                            keberhasilan +=1
                        except Exception as error:
                            if cache and not cache.count(f'({ln}: "{error}")'):
                                cache += f', ({ln}: "{error}")'
                            else:
                                cache = f'({ln}: "{error}")'
                            kegagalan +=1
                else:
                    break
        elif perintah == "potong":
            for s in source:
                if operasi:
                    for d in destination:
                        try:
                            metode = None
                            if os.path.basename(s).count("."):
                                metode = "file"
                            else:
                                metode = "folder"
                            if os.path.basename(d).count(".") and d.count("\\") and not os.path.isdir(os.path.dirname(d)) and os.path.exists(s): #file in destination
                                os.makedirs(os.path.dirname(d))
                            elif not os.path.isdir(d) and not os.path.basename(d).count(".") and os.path.exists(s): #folder in destination
                                os.makedirs(d)
                            if os.path.exists(fr"{d}\{os.path.basename(s)}") and tanya == 0:
                                cache_path = fr"{d}\{os.path.basename(s)}"
                                ask = askyesnocancel(
                                    title = "Warning",
                                    message = f'We found the same file/folder name in "{cache_path}", overwrite it?\nOr "Cancel" to stop the process even though the previous action has already been processed',
                                    icon = WARNING
                                )
                                if ask == True: #Yes
                                    if metode == "file":
                                        if os.path.exists(s):
                                            os.remove(fr"{d}\{os.path.basename(s)}")
                                        shutil.move(s, d)
                                    else:
                                        ask2 = askyesno(
                                            title = "Warning 2",
                                            message = "Are you sure you want to overwrite it even if there are files and/or folders in it?\nThis action will delete all files and folders inside! Unless the action of moving the folder states an error",
                                            icon = WARNING
                                        )
                                        if ask2:
                                            if os.path.exists(s):
                                                shutil.rmtree(fr"{d}\{os.path.basename(s)}")
                                            shutil.move(s, d)
                                        else:
                                            keberhasilan += 1
                                            user = True
                                            continue
                                elif ask == False: #No
                                    keberhasilan += 1
                                    user = True
                                    continue
                                else: #Cancel
                                    operasi = False
                                    break
                            else:
                                if os.path.exists(s): #Mengamankan file/folder dari tindakan penghapusan kalau shutil.move() akan memberikan kesalahan
                                    if os.path.exists(fr"{d}\{os.path.basename(s)}"):
                                        if metode == "file":
                                            os.remove(fr"{d}\{os.path.basename(s)}")
                                        else:
                                            shutil.rmtree(fr"{d}\{os.path.basename(s)}")
                                shutil.move(s, d)
                            keberhasilan += 1
                        except Exception as error:
                            if cache:
                                cache += f', ({ln}: "{error}")'
                            else:
                                cache = f'({ln}: "{error}")'
                            kegagalan += 1
                else:
                    break
    if perintah == "salin":
        tindakan = "COPIED"
    elif perintah == "potong":
        tindakan = "MOVED"
    else:
        return "Why you do that?"
    if user:
        tambahan = " AND SOME CANCELLATIONS"
    else:
        tambahan = ""
    if keberhasilan and not kegagalan:
        return f"SUCCESSFULLY {tindakan} FILE(S)"+cache+tambahan
    elif keberhasilan and kegagalan:
        return f"SUCCESSFULLY {tindakan} FILE(S) WITH ERROR(S): "+cache+tambahan
    elif operasi:
        return "ERROR(S): "+cache
    else:
        return "CANCELED"