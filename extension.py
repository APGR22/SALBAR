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
# import datetime
import time

def get_time() -> str:
    return str(time.time())

SYNTAX_STRING_1 = "insert string di salbar dengan atas nama dir1 = >>"
SYNTAX_STRING_2 = "insert string di salbar dengan atas nama dir2 = >>"
SYNTAX_TIME = "insert time as string di salbar dengan atas nama time = >>"

class ekstensi:
    def make(nama: str, direktori: str, tujuan: str, nama_lama: str = False):
        d = convert.make(direktori)
        t = convert.make(tujuan)
        if nama_lama:
            make_time = ekstensi.read_time(nama_lama)
        else:
            make_time = get_time()

        teks = f"""{SYNTAX_STRING_1}{d}<<;
{SYNTAX_STRING_2}{t}<<;
{SYNTAX_TIME}{make_time}<<;"""

        if nama_lama:
            if os.path.isfile(paths.PATH+nama_lama+".slbr"):
                os.rename(paths.PATH+nama_lama+".slbr", paths.PATH+nama+".slbr")
        o = open(paths.PATH+nama+".slbr", "w")
        o.write(teks)
        o.close()

    def check_read(name):
        with open(paths.PATH+name+".slbr", "r") as o:
            teks = o.read()

        with open(paths.PATH+name+".slbr", "r") as o:
            baris = o.readlines()

        if not (
            teks.count(SYNTAX_STRING_1) == 1 and
            teks.count(SYNTAX_STRING_2) == 1 and
            teks.count(SYNTAX_TIME) == 1 and

            baris[0].startswith(SYNTAX_STRING_1) and
            baris[1].startswith(SYNTAX_STRING_2) and
            baris[2].startswith(SYNTAX_TIME) and

            baris[0].endswith("<<;\n") and
            baris[1].endswith("<<;\n") and
            baris[2].endswith("<<;") and

            baris[0].count(";") == 1 and
            baris[1].count(";") == 1 and
            baris[2].count(";") == 1 and

            baris[0].count(">>") == 1 and
            baris[1].count(">>") == 1 and
            baris[2].count(">>") == 1 and

            baris[0].count("<<") == 1 and
            baris[1].count("<<") == 1 and
            baris[2].count("<<") == 1 and

            len(baris) == 3
            ):
            raise Exception("there is modification")

    def read(name: str):
        with open(paths.PATH+name+".slbr", "r") as o:
            baris = o.readlines()
        hasil_d = baris[0].split(SYNTAX_STRING_1)[1].split("<<;")[0]
        hasil_t = baris[1].split(SYNTAX_STRING_2)[1].split("<<;")[0]
        hasil_d = convert.read(hasil_d)
        hasil_t = convert.read(hasil_t)
        return hasil_d, hasil_t #untuk mengirim definisi

    def read_time(name: str) -> str:
        with open(paths.PATH+name+".slbr", "r") as o:
            content = o.readlines()
        creation_time = content[2].split(SYNTAX_TIME)[1].split("<<;")[0]
        return creation_time