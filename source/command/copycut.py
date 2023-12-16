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

import shutil
import paths
from command import _folders
from command import _for_command

def move_directory(s: str, d: str): #If it proves to be very slow and inefficient compared to copytree+rmtree then you can give me criticism as well as a solution if any
    for file_s, file_d in _folders.make_directories(s, d):
        shutil.move(file_s, file_d)

    _for_command.rmtree(s, d)

def copy(n: str, s: str, d: str, file_method: bool, *args) -> (str | None):
    try:
        if file_method: #file
            shutil.copy(
                        paths.replace_path_symbol(s),
                        paths.replace_path_symbol(d)
                        )
        else: #folder
            for file_s, file_d in _folders.make_directories(
                                                            paths.replace_path_symbol(s),
                                                            paths.replace_path_symbol(d)
                                                            ):
                shutil.copy(file_s, file_d)
            # shutil.copytree(
            #                 paths.replace_path_symbol(s),
            #                 paths.replace_path_symbol(d),
            #                 dirs_exist_ok = True
            #                 )
    except Exception as error:
        return f"{n}: {error}"

def move(n: str, s: str, d: str, file_method: bool, *args) -> (str | None):
    try:
        if file_method: #file
            shutil.move(
                        paths.replace_path_symbol(s),
                        paths.replace_path_symbol(d)
                        )
        else: #folder
            #bertindak seperti move padahal copy
            # salin(n, s, d, method_file)
            # shutil.rmtree(s)
            move_directory(
                        paths.replace_path_symbol(s),
                        paths.replace_path_symbol(d)
                        )
    except Exception as error:
        return f"{n}: {error}"