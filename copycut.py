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

import os
import shutil
import paths

def pindah_folder(s: str, d: str): #If it proves to be very slow and inefficient compared to copytree+rmtree then you can give me criticism as well as a solution if any
    path_s = []
    only_path_s = []
    path_d = []
    only_path_d = []
    for path, folders, files in os.walk(s): #cari semua jalur file di dalam folder
        if folders == [] and files == []: #jika suatu folder kosong (tidak ada file dan folder)
            #daftarkan hanya path (sama saja dengan memindahkan folder)
            only_path_s.append(path)
        else:
            for file in files:
                path_s.append(os.path.join(path, file)) #daftarkan setiap jalur file
                only_path_s.append(path)
    for path in path_s:
        path_d.append(os.path.join(d, path)) #hasil #panjangnya akan sama
    #pisahkan agar ketika kedua panjang list tidak sama maka tidak akan terganggu
    for only_path in only_path_s:
        only_path_d.append(os.path.join(d, only_path)) #hasil #panjangnya akan sama

    for path in only_path_d:
        try:
            os.makedirs(path)
        except FileExistsError:
            pass
    for file_s, file_d in zip(path_s, path_d):
        shutil.move(file_s, file_d)

    try:
        shutil.rmtree(s)
    except FileNotFoundError: #firasat saya tidak enak kalau tidak ada pengecualian
        pass

def salin(n, s: str, d: str, method_file: bool):
    if method_file: #file
        try:
            shutil.copy(paths.ganti_simbol(s),
                        paths.ganti_simbol(d))
        except Exception as error:
            return f"{n}: {error}"
    else: #folder
        try:
            shutil.copytree(paths.ganti_simbol(s),
                            paths.ganti_simbol(os.path.join(d, os.path.basename(s))), #harus pakai penggantian karena membiarkan d dan s masih dalam simbol yang belum diubah
                            dirs_exist_ok = True)
        except Exception as error:
            return f"{n}: {error}"

def pindah(n, s: str, d: str, method_file: bool):
    if method_file: #file
        try:
            shutil.move(paths.ganti_simbol(s),
                        paths.ganti_simbol(d))
        except Exception as error:
            return f"{n}: {error}"
    else: #folder
        try:
            #bertindak seperti move padahal copy
            # salin(n, s, d, method_file)
            # shutil.rmtree(s)
            pindah_folder(paths.ganti_simbol(s),
                        paths.ganti_simbol(d))
        except Exception as error:
            return f"{n}: {error}"