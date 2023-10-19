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

import convert #demi mudah dipahami meski performa dikorbankan
import os
import paths
bahasa_1 = "insert string di salbar dengan atas nama dir1 = >>"
bahasa_2 = "insert string di salbar dengan atas nama dir2 = >>"

class ekstensi:
    def make(nama: str, direktori: str, tujuan: str, nama_lama: str = False):
        d = convert.make(direktori)
        t = convert.make(tujuan)
        teks = f"""{bahasa_1}{d}<<;
{bahasa_2}{t}<<;"""
        if nama_lama:
            if os.path.isfile(paths.PATH+nama_lama+".slbr"):
                os.rename(paths.PATH+nama_lama+".slbr", paths.PATH+nama+".slbr")
        o = open(paths.PATH+nama+".slbr", "w")
        o.write(teks)
        o.close()

    def read(nama: str):
        o = open(paths.PATH+nama+".slbr", "r")
        teks = o.read()
        o.close()
        baris = open(paths.PATH+nama+".slbr", "r").readlines()
        if not (
            teks.count(bahasa_1) == 1 and
            teks.count(bahasa_2) == 1 and
            baris[0].startswith(bahasa_1) and
            baris[1].startswith(bahasa_2) and
            baris[0].endswith("<<;\n") and
            baris[1].endswith("<<;") and
            baris[0].count(";") == 1 and
            baris[1].count(";") == 1 and
            baris[0].count(">>") == 1 and
            baris[1].count(">>") == 1 and
            baris[0].count("<<") == 1 and
            baris[1].count("<<") == 1 and
            len(baris) == 2
            ):
            raise Exception("there is modification")
        hasil_d = baris[0].split(bahasa_1)[1]
        hasil_t = baris[1].split(bahasa_2)[1]
        hasil_d = convert.read(hasil_d)
        hasil_t = convert.read(hasil_t)
        return hasil_d, hasil_t #untuk mengirim definisi