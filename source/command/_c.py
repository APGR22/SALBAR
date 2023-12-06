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
import shutil
from paths import filename, filethread, executable
from command import _folders
from command import _c_errors

def _writetofile(s: str, d: str, copy: bool, symlink: bool):
    if symlink:
        s = os.path.realpath(s)
        d = os.path.realpath(d)
    else:
        s = os.path.abspath(s)
        d = os.path.abspath(d)

    with open(filename, "a") as file:
        file.write(f"{s}\n")
        file.write(f"{d}\n")
        if copy:
            file.write("copy\n")
        else:
            file.write("move\n")

def copymove_file(s: str, d: str, copy: bool, symlink: bool = False) -> str:
    _writetofile(s, d, copy, symlink)

    get = subprocess.check_output([executable, filename, filethread])

    return _c_errors.identify(get[2:])


def copymove_folder(s: str, d: str, copy: bool, symlink: bool = False) -> str: #took this method from the copycut module
    path_sd = _folders.make_directories(s, d)
    path_s = path_sd[0]
    path_d = path_sd[1]

    for file_s, file_d in zip(path_s, path_d):
        # results.append(copymove_file(file_s, file_d, copy, symlink))
        _writetofile(file_s, file_d, copy, symlink)

    get = subprocess.check_output([executable, filename, filethread])

    if not copy:
        try:
            shutil.rmtree(s)
        except FileNotFoundError: #firasat saya tidak enak kalau tidak ada pengecualian
            pass

    return _c_errors.identify(get[2:])