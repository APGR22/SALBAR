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

import platform
import os

if platform.system() == "Windows":
    PATH_SYMBOL = "\\"
else: #Linux and Darwin
    PATH_SYMBOL = "/"

PATH = "Paths"+PATH_SYMBOL

def replace_path_symbol(path: str) -> str:
    path = path.replace("\\", PATH_SYMBOL)
    path = path.replace("/", PATH_SYMBOL)
        
    return path

def get_current_path() -> str:
    return os.path.dirname(__file__)

def separate_path(path: str) -> list[str]:
    path = path.replace('" "', '"')
    paths = path.split('"')
    while True:
        try:
            paths.remove("")
        except:
            break #buat daftar untuk setiap jalur
    return paths

def is_abs_path(path: str) -> bool:
    abs_path = False
    for path in separate_path(path):
        if os.path.isabs(path):
            abs_path = True #jika sudah ketemu meski cuman 1 maka akan dianggap ada
            break
    return abs_path

path = os.path.join(get_current_path(), "c")
filename = os.path.join(path, "com.txt")
filethread = os.path.join(path, ".stopthread")
if platform.system() == "Windows":
    executable = os.path.join(path, "main.exe")
else: #Linux
    executable = os.path.join(path, "main")