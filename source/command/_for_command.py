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

from tkinter import Toplevel, IntVar
from tkinter.messagebox import *
from tkinter.messagebox import WARNING
import os
import shutil

def make_dir(d: str):
    try: os.makedirs(d)
    except: pass #jika sudah ada. meski ada exist_ok, itu berarti ditimpa sehingga tidak digunakan

def rmtree(s: str, d: str):
    "d and the base name s must be combined first"
    s = os.path.abspath(s)
    d = os.path.abspath(d)

    if d.startswith(s):
        for path, none, none in os.walk(s):
            if path != s and not path.startswith(d):
                try:
                    shutil.rmtree(path)
                except FileNotFoundError:
                    pass
    else:
        try:
            shutil.rmtree(s)
        except FileNotFoundError:
            pass

def if_exists(path: str, skip: IntVar, parent: Toplevel):
    """return "tidak ada" if not exists"""
    if os.path.exists(path):
        if skip.get() == 1:
            return "skip"
        ask = askyesnocancel(
            title = "Warning",
            message = f'We found the same file/folder name in "{path}", overwrite it?\nOr "Cancel" to stop the process even though the previous action has already been processed',
            icon = WARNING,
            parent=parent
        )
        return ask
    return "tidak ada"

def filter_list(source_list: list[str], x: str) -> list[str]:
    return list(filter((x).__ne__, source_list)) #https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list

def write_error(list_error: list[str]):
    with open("errors.txt", "w") as o:
        o.write("This file will be deleted and overwritten if a very long error occurs again in the future!\n\n")
        for error in list_error:
            o.write(error.replace("\\\\", chr(92))+"\n") #.replace() only applied when in Windows

max_error = 3