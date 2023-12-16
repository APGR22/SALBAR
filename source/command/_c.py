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
import subprocess
from paths import filename, filethread, executable
from command import _folders
from command import _c_errors

def _createfile():
    with open(filename, "w") as file:
        file.write("n\npass\npass\ncopy\n")

def startthread():
    if os.path.isfile(filethread):
        os.remove(filethread)

def stopthread():
    with open(filethread, "w"):...

def _writetofile(n: str, s: str, d: str, copy: bool, symlink: bool):
    if symlink:
        s = os.path.realpath(s)
        d = os.path.realpath(d)
    else:
        s = os.path.abspath(s)
        d = os.path.abspath(d)

    with open(filename, "a") as file:
        file.write(f"{n}\n")
        file.write(f"{s}\n")
        file.write(f"{d}\n")
        if copy:
            file.write("copy\n")
        else:
            file.write("move\n")

def _writedirectories(n: str, s: str, d: str, copy: bool, symlink: bool): #took this method from the copycut module
    for file_s, file_d in _folders.make_directories(s, d):
        _writetofile(n, file_s, file_d, copy, symlink)

def writetofile(n: str, s: str, d: str, file_method: bool, copy: bool, symlink: bool = False) -> (str | None):
    "if file then 's' and 'd' must file path"
    try:
        if file_method:
            _writetofile(n, s, d, copy, symlink)
        else:
            _writedirectories(n, s, d, copy, symlink)
    except Exception as error:
        return f"{n}: {error}"

def copymove(list_errors: list[str]):
    get = subprocess.check_output([executable, filename, filethread])

    #get = "{name}:{error}{\n}"

    #[4:] = "n:3\n" #for pass
            #^^^ ^
            #123 4 
    #[:-2] = "\n0" #for debugging
             # ^^
             # 12 

    get = get.replace(b"\r", b"")[4:][:-2]
    _c_errors.identify(get, list_errors)