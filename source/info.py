# Copyright © 2024 APGR22

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tkinter import *

def baca(nama: str, r: int | None = None, tambahkan: bool = False):...

class _info:
    def __init__(self):
        self.root: Tk
        self.kanvas: Canvas
        self.bingkai: Frame

        self.program_list: list[str]
        self.excluded_program_list: list[str]
        self.list_name: list[str]
        self.list_source: list[str]
        self.list_destination: list[str]
        self.nama_edit_timpa: dict[str, str]
        self.dict_program_list: dict[str, IntVar | Checkbutton | object | Label | Label]
        self.sort_key: str
        self.baca = baca

        self.selected: str
        self.confirm_to_overwrite: IntVar
        self.confirm_to_skip: IntVar
        self.confirm_to_use_c: IntVar

info = _info()