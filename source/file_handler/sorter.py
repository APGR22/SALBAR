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

from tkinter.messagebox import *
from file_handler import extension
import info

SORTED_NAME = "A-Z"
SORTED_NAME_REVERSED = "Z-A"
SORTED_TIME = "OLD-NEW"
SORTED_TIME_REVERSED = "NEW-OLD"

list_sorted = [
    SORTED_NAME,
    SORTED_NAME_REVERSED,
    SORTED_TIME,
    SORTED_TIME_REVERSED
]

class sort:
    def __init__(self, info: info._info) -> None:
        self.info = info

    def _get_program(self):
        h = 0

        #Items in the list may decrease while it is being iterated resulting in changes to the index.
        #This is better handled with a while loop rather than a for loop
        while h < len(self.info.program_list):
            program = self.info.program_list[h]
            if program.endswith(".slbr"):
                name = program[:-5]
                if name in self.info.excluded_program_list:
                    self.info.program_list.remove(program)
                else:
                    yield name

                    h += 1

    def _reversed_dict(self, input: dict[str, str]) -> dict[str, str]:
        return dict(reversed(input.items()))

    def name(self, reverse: bool = False) -> dict[str, str]:
        output = {}
        i = 0
        for name in sorted(self._get_program()):
            output[i] = name
            i += 1
        
        if reverse:
            return self._reversed_dict(output)
        
        return output

    def time(self, reverse: bool = False) -> dict[str, str]:
        output = {}
        for name in self._get_program():
            try:
                extension.ekstensi.check_read(name)
                date = extension.ekstensi.read_time(name)
                #harus memasukkan isi kamus dengan tipe list
                try:
                    output[date].append(name) #jika sudah ada date yang sama
                except KeyError:
                    output[date] = [name]
            except Exception as error:
                showerror(
                    title="Error - (time)",
                    message=f"{name}: {error}"
                )
                self.info.excluded_program_list.append(name)

        new_output = {}
        h = 0
        for i in sorted(output): #sorted in date
            for program in sorted(output[i]): #sorted in name, maybe?
                new_output[h] = program
                h += 1

        output = new_output

        if reverse:
            return self._reversed_dict(output)

        return output