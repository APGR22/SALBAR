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

from tkinter import Tk, Toplevel, Frame
import typing

class main:
    def __init__(
                self,
                root: Tk | Toplevel | Frame,
                program_list: list[str],
                dict_program_list: dict[str, typing.Any],
                selected: list[str],
                sort_key: dict[str, str],
                key: str,
                ) -> None:
        self.program_list = program_list
        self.dict_program_list = dict_program_list
        self.selected = selected
        self.current = ""
        self.sort_key = sort_key
        self.current_sort_key = sort_key[key]
        self.key = key
        self.session = False
        self.shift = 0 #n<0 = up, n>0 = down

        def refresh():
            if self.dict_program_list != dict_program_list:
                if self.shift < 0:
                    self.shift += 1
                elif self.shift > 0:
                    self.shift -= 1

                self.dict_program_list = dict_program_list

            root.after(100, refresh)

    def _refresh(self):
        if self.current_sort_key == self.sort_key[self.key] and len(self.selected) != 0:
            self.session = True

            if self.current != self.selected[0]:
                self.shift = 0
            self.current = self.selected[0]
            self.current_index = self.program_list.index(self.current)
        else:
            self.session = False

            self.current_sort_key = self.sort_key[self.key]
            self.shift = 0

    def _select(self, program_name: str):
        self.dict_program_list[f"{program_name}_cb"].select()
        self.dict_program_list[f"{program_name}_centang"](False)

    def _deselect(self, program_name: str):
        self.dict_program_list[f"{program_name}_cb"].deselect()
        self.dict_program_list[f"{program_name}_centang"](False)

    def _config(self, up: bool) -> bool:
        current_index = self.current_index + self.shift
        if current_index >=0 and current_index < len(self.program_list):
            under_index = current_index + 1
            above_index = current_index - 1

            try:
                under_program = self.program_list[under_index]
            except:
                under_program = None
            try:
                above_program = self.program_list[above_index]
            except:
                above_program = None

            self._select(self.program_list[current_index])

            if self.shift < 0: #up
                if up:...
                else:
                    if above_program is not None:
                        self._deselect(above_program)
            elif self.shift > 0: #down
                if up:
                    if under_program is not None:
                        self._deselect(under_program)
                else:...
            else: #current
                if above_program is not None:
                    self._deselect(above_program)
                if under_program is not None:
                    self._deselect(under_program)

            return True

    def up(self, *args): #-1
        self._refresh()
        if self.session == True:
            self.shift -= 1
            if not self._config(True):
                self.shift += 1

    def down(self, *args): #+1
        self._refresh()
        if self.session == True:
            self.shift += 1
            if not self._config(False):
                self.shift -= 1

def simple_select(root: Tk | Toplevel | Frame, program_list: list[str], dict_program_list: dict[str, typing.Any]) -> None:

    def pilih(event):
        for i in program_list: #kalau kosong maka for loop-nya tidak berjalan dan dikira selesai
            dict_program_list[f"{i}_cb"].select()
            dict_program_list[f"{i}_centang"]()

    def tidak_pilih(event):
        for i in program_list:
            dict_program_list[f"{i}_cb"].deselect()
            dict_program_list[f"{i}_centang"]()

    #doesn't catch the exception even if the user disables the progress bar window
    root.bind("<Control-a>",  pilih)
    root.bind("<Control-A>",  pilih)
    root.bind("<Control-Shift-a>",  tidak_pilih)
    root.bind("<Control-Shift-A>",  tidak_pilih)