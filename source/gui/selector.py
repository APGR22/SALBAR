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

import info
import copy

class main:
    def __init__(
                self,
                info: info._info
                ) -> None:
        self.info = info
        self.cache_program_list = copy.copy(info.program_list)
        self.current = ""
        self.current_index = 0
        self.current_sort_key = info.sort_key
        self.session = False
        self.shift = 0 #n<0 = up, n>0 = down

        #will update if there is a reduction in the list
        def refresh():
            current_index = self.current_index + self.shift
            if (
                len(self.cache_program_list) > len(info.program_list)
                and
                    (
                    current_index == 0 #beginning
                    or
                    current_index == len(info.program_list)-1 #end
                    )
                ):
                if self.shift < 0:
                    self.shift += 1
                elif self.shift > 0:
                    self.shift -= 1

                self.cache_program_list = copy.copy(info.program_list)

            info.kanvas.after(100, refresh)

        refresh()

    def _cancel(self):
        self.session = False

        self.current_sort_key = self.info.sort_key
        self.shift = 0

    def _refresh(self):
        try:
            if self.current_sort_key == self.info.sort_key and len(self.info.selected) != 0:
                self.session = True

                if self.current != self.info.selected:
                    self.shift = 0
                self.current = self.info.selected
                self.current_index = self.info.program_list.index(self.current)
            else:
                self._cancel()
        except:
            self._cancel()

    def _select(self, program_name: str):
        self.info.dict_program_list[f"{program_name}_cb"].select()
        self.info.dict_program_list[f"{program_name}_centang"](False)

    def _deselect(self, program_name: str):
        self.info.dict_program_list[f"{program_name}_cb"].deselect()
        self.info.dict_program_list[f"{program_name}_centang"](False)

    def _config(self, up: bool) -> bool:
        "(select or deselect) and prevent the selection from being outside the program list"
        current_index = self.current_index + self.shift
        if 0 <= current_index < len(self.info.program_list):
            under_index = current_index + 1
            above_index = current_index - 1

            try:
                under_program = self.info.program_list[under_index]
            except:
                under_program = None
            try:
                above_program = self.info.program_list[above_index]
            except:
                above_program = None

            self._select(self.info.program_list[current_index])

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

        return False

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

def simple_select(info: info._info) -> None:

    def pilih(event):
        for i in info.program_list: #kalau kosong maka for loop-nya tidak berjalan dan dikira selesai
            info.dict_program_list[f"{i}_cb"].select()
            info.dict_program_list[f"{i}_centang"]()

    def tidak_pilih(event):
        for i in info.program_list:
            info.dict_program_list[f"{i}_cb"].deselect()
            info.dict_program_list[f"{i}_centang"]()

    #doesn't catch the exception even if the user disables the progress bar window
    info.kanvas.bind("<Control-a>",  pilih)
    info.kanvas.bind("<Control-A>",  pilih)
    info.kanvas.bind("<Control-Shift-a>",  tidak_pilih)
    info.kanvas.bind("<Control-Shift-A>",  tidak_pilih)