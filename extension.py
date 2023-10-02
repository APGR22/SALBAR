"""Copyright © 2023 APGR22

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

import private_module.kacaukan as kacaukan
import os
bahasa_1 = "insert string di salbar dengan atas nama dir1 = >>"
bahasa_2 = "insert string di salbar dengan atas nama dir2 = >>"

class ekstensi:
    def make(nama: str, direktori: str, tujuan: str, nama_lama: str = False):
        d = kacaukan.make(direktori)
        t = kacaukan.make(tujuan)
        teks = f"""{bahasa_1}{d}<<;
{bahasa_2}{t}<<;"""
        if nama_lama:
            if os.path.isfile("Paths\\"+nama_lama+".slbr"):
                os.rename("Paths\\"+nama_lama+".slbr", "Paths\\"+nama+".slbr")
        o = open("Paths\\"+nama+".slbr", "w")
        o.write(teks)
        o.close()

    def read(nama: str):
        o = open("Paths\\"+nama+".slbr", "r")
        teks = o.read()
        o.close()
        baris = open("Paths\\"+nama+".slbr", "r").readlines()
        if not (
            teks.count(bahasa_1) == 1 and
            teks.count(";") == 2 and
            baris[0].endswith("<<;\n") and
            baris[1].endswith("<<;") and
            baris[0].count(">>") == 1 and
            baris[1].count(">>") == 1 and
            baris[0].count("<<") == 1 and
            baris[1].count("<<") == 1 and
            teks.count(bahasa_2) == 1 and
            len(baris) == 2
            ):
            raise Exception("ada modifikasi")
        hasil_d = baris[0].split(bahasa_1)[1]
        hasil_t = baris[1].split(bahasa_2)[1]
        hasil_d = kacaukan.read(hasil_d)
        hasil_t = kacaukan.read(hasil_t)
        return hasil_d, hasil_t #untuk mengirim definisi