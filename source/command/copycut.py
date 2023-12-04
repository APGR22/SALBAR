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
from command import _folders
from command import _c

def pindah_folder(s: str, d: str): #If it proves to be very slow and inefficient compared to copytree+rmtree then you can give me criticism as well as a solution if any
    path_sd = _folders.make_directories(s, d)
    path_s = path_sd[0]
    path_d = path_sd[1]

    for file_s, file_d in zip(path_s, path_d):
        shutil.move(file_s, file_d)

    try:
        shutil.rmtree(s)
    except FileNotFoundError: #firasat saya tidak enak kalau tidak ada pengecualian
        pass

def salin(n: str, s: str, d: str, method_file: bool, c: bool = False):
    if c:
        if method_file:
            result = _c.copymove_file(
                                    paths.replace_path_symbol(s),
                                    paths.replace_path_symbol(os.path.join(d, os.path.basename(s))),
                                    True
                                    )
            if result != "success":
                return f"{n}: {result}"
        else:
            result =  _c.copymove_folder(
                                        paths.replace_path_symbol(s),
                                        paths.replace_path_symbol(os.path.join(d, os.path.basename(s))),
                                        True
                                        )
            if result != "success":
                return f"{n}: {result}"

    else:
        if method_file: #file
            try:
                shutil.copy(paths.replace_path_symbol(s),
                            paths.replace_path_symbol(os.path.join(d, os.path.basename(s))))
            except Exception as error:
                return f"{n}: {error}"
        else: #folder
            try:
                shutil.copytree(paths.replace_path_symbol(s),
                                paths.replace_path_symbol(os.path.join(d, os.path.basename(s))), #harus pakai penggantian karena membiarkan d dan s masih dalam simbol yang belum diubah
                                dirs_exist_ok = True)
            except Exception as error:
                return f"{n}: {error}"

def pindah(n: str, s: str, d: str, method_file: bool, c: bool = False):
    if c:
        if method_file:
            result = _c.copymove_file(
                                    paths.replace_path_symbol(s),
                                    paths.replace_path_symbol(os.path.join(d, os.path.basename(s))),
                                    False
                                    )
            if result != "success":
                return f"{n}: {result}"
        else:
            if not _c.copymove_folder(
                                        paths.replace_path_symbol(s),
                                        paths.replace_path_symbol(d),
                                        False
                                        ):
                return f"{n}: there is an error"
            if result != "success":
                return f"{n}: {result}"

    else:
        if method_file: #file
            try:
                shutil.move(paths.replace_path_symbol(s),
                            paths.replace_path_symbol(os.path.join(d, os.path.basename(s))))
            except Exception as error:
                return f"{n}: {error}"
        else: #folder
            try:
                #bertindak seperti move padahal copy
                # salin(n, s, d, method_file)
                # shutil.rmtree(s)
                pindah_folder(paths.replace_path_symbol(s),
                            paths.replace_path_symbol(d))
            except Exception as error:
                return f"{n}: {error}"