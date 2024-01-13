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
from tkinter.messagebox import *
from file_handler import extension
from file_handler import sorter
import info

class refresh:
    def __init__(
                self,
                info: info._info
                ) -> None:
        "auto run"

        #variable
        self.info = info
        self.current_sort_key = info.sort_key

        #class
        self.sorter = sorter.sort(info)

        #
        self.daftar_pembaruan = os.listdir("Paths")
        self.remove_non_slbr(self.daftar_pembaruan)

        if len(self.daftar_pembaruan) > 744:
            showwarning(
                title="Warning",
                message="Check button exceeds 744.\nPossible rendering will be broken at the very bottom"
            )

        self.perbarui()

    def refresh_program_list(self):
        self.info.program_list.clear()
        self.info.program_list.extend(os.listdir("Paths"))

        if self.info.sort_key == sorter.SORTED_NAME:
            program_sort_list = self.sorter.name()
        elif self.info.sort_key == sorter.SORTED_NAME_REVERSED:
            program_sort_list = self.sorter.name(True)
        elif self.info.sort_key == sorter.SORTED_TIME:
            program_sort_list = self.sorter.time()
        elif self.info.sort_key == sorter.SORTED_TIME_REVERSED:
            program_sort_list = self.sorter.time(True)
        else:
            raise KeyError("key is no valid")

        results = []
        for program in program_sort_list.values():
            if not program in self.info.excluded_program_list: #cek jika termasuk program yang dikecualikan
                results.append(program)
        self.info.program_list.clear()
        self.info.program_list.extend(results)

    def remove_non_slbr(self, daftar: list[str]):
        daftar_cache = set(daftar) - set([name+".slbr" for name in self.info.excluded_program_list])
        daftar.clear()
        daftar.extend(daftar_cache)
        for path in daftar:
            if path[:-5] in self.info.excluded_program_list:
                daftar.remove(path)
            elif path.endswith(".slbr"):
                try:
                    extension.ekstensi.check_read(path[:-5])
                except Exception as error:
                    showerror(
                        title="Error - (remove non slbr)",
                        message=f"{path[:-5]}: {error}"
                    )
                    self.info.excluded_program_list.append(path[:-5])
                    daftar.remove(path)
            else:
                daftar.remove(path)
    
    def reset_list(self):
        self.info.nama_edit_timpa.clear()
        self.info.list_source.clear()
        self.info.list_destination.clear()
        self.info.list_name.clear()

    def reconfig(self):
        self.refresh_program_list()
        for r, i in enumerate(self.info.program_list):
            #reconfig
            try:
                self.info.dict_program_list[f"{i}_cb"].grid(row=r+1)
                self.info.dict_program_list[f"{i}_label"].grid(row=r+1)
                self.info.dict_program_list[f"{i}_date"].grid(row=r+1)
            except: #seandainya kesalahannya berasal dari tindakan pengguna yang rename file .slbr secara manual
                self.info.baca(i)
                self.info.dict_program_list[f"{i}_cb"].grid(row=r+1)
                self.info.dict_program_list[f"{i}_label"].grid(row=r+1)
                self.info.dict_program_list[f"{i}_date"].grid(row=r+1)

    def destroy(self, name: str):
        del self.info.dict_program_list[f"{name}_var"], self.info.dict_program_list[f"{name}_centang"]
        self.info.dict_program_list[f"{name}_cb"].destroy()
        self.info.dict_program_list[f"{name}_label"].destroy()
        self.info.dict_program_list[f"{name}_date"].destroy()

    def perbarui(self):
        daftar_pembaruan_2 = os.listdir("Paths")
        self.remove_non_slbr(daftar_pembaruan_2)

        if len(self.info.nama_edit_timpa) == 2: #edit
            cache_row = self.info.dict_program_list[f"{self.info.nama_edit_timpa['nama_lama']}_cb"].grid_info()["row"]
            self.destroy(self.info.nama_edit_timpa['nama_lama'])
            self.info.baca(self.info.nama_edit_timpa["nama"], cache_row)
            self.reset_list()
            self.reconfig()

        elif len(self.info.nama_edit_timpa) == 1: #timpa
            try:
                self.destroy(self.info.nama_edit_timpa['nama_timpa'])
            except:
                try:
                    self.info.excluded_program_list.remove(self.info.nama_edit_timpa["nama_timpa"])
                except:
                    pass
            self.info.baca(self.info.nama_edit_timpa["nama_timpa"], tambahkan = True)
            self.reconfig()
            self.reset_list()
            daftar_pembaruan_2 = os.listdir("Paths") #reconfig
            self.remove_non_slbr(daftar_pembaruan_2)

        elif self.daftar_pembaruan != daftar_pembaruan_2:
            if len(daftar_pembaruan_2) > len(self.daftar_pembaruan): #tambah
                jumlah = set(daftar_pembaruan_2) - set(self.daftar_pembaruan)
                for i in jumlah:
                    self.info.baca(i[:-5], tambahkan=True)

                self.reconfig()
            else: #kurang
                jumlah = set(self.daftar_pembaruan) - set(daftar_pembaruan_2)

                for i in jumlah:
                    self.info.dict_program_list[f"{i[:-5]}_cb"].deselect() #pastikan untuk membatalkan centangnya
                    self.info.dict_program_list[f"{i[:-5]}_centang"]() #pastikan fungsinya berjalan tanpa checkbutton
                    self.destroy(i[:-5])

                self.reconfig()
        
        elif self.info.sort_key != self.current_sort_key:
            self.reconfig()
            self.current_sort_key = self.info.sort_key

        self.daftar_pembaruan = daftar_pembaruan_2
        self.refresh_program_list()

        self.info.root.after(100, self.perbarui)