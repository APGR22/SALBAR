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
import typing

def make_directories(s: str, d: str) -> typing.Generator[str, str, None]:
#     list_s = []
#     list_d = []
    s = os.path.abspath(s)
    d = os.path.abspath(d)

    len_s = len(s)

    for path, folders, files in os.walk(s): #cari semua jalur file di dalam folder
        if path.startswith(d): #for safety
            continue

        if path[len_s+1:] != "":
            path_d = os.path.join(d, path[len_s+1:])
        else:
            path_d = d

        try: os.makedirs(path_d)
        except FileExistsError: pass

        for file in files:
#             list_s.append(os.path.join(path, file))
#             list_d.append(os.path.join(path_d, file))
            yield os.path.join(path, file), os.path.join(path_d, file)

#     return list_s, list_d