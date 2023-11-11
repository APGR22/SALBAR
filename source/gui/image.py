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

from tkinter import *
import os
from PIL import Image, ImageTk
from io import BytesIO

path_icon = "SALBAR.png"

def set_icon(root: Tk):
    if os.path.isfile(path_icon):
        root.wm_iconphoto(True, ImageTk.PhotoImage(Image.open(path_icon)))
    else:
        kode_icon = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01\x00\x00\x00\x01\x00\x08\x06\x00\x00\x00\\r\xa8f\x00\x00\x00\tpHYs\x00\x00.#\x00\x00.#\x01x\xa5?v\x00\x00\x04\xa0IDATx\xda\xed\xdcAn\x1b9\x10@QQ\xd0":\xa6u0\xf9\x98\xca\x8e6\x0c\x1b\x10\x0cG!\xad&\x9bd\xbd\x07\x0cf\x13\x04\x13\xb5\xfaw\xb1\xda\x99\xc3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa8\x93V\xf9\x83\xe4\xdb5\xbb\x9c<}C\x9c/I\x00\xdc\xf8\x08A\x12\x80\xb1o\xfc\x8f\x7f\xf9\xaa"\x04\x02\x00\xcd\xef\x93\xf7\x18,\xf7\x07;\xce<\xfd\xfb^B\xdc\x00\x80\x87\x8d\x00@\xd7c\xa7\x00\x80)@\x00@\x04&7\xf3[\x00K@v\xbdoVx+pr-?\xfdy\xf1\x19D\xf7\xf7\xb5f\x12X\xe2\xe7\x03\x04\xe0+\xe9)\xf9\x10\xf8\x9a.\x8b\x7f\xdd\xecS\x80\x00\xdc_tS\x00\xe5\xd3\xc0\x12S\x80\x00|\xbb\xe8+\xfe\xb4\x17\xbfx \xe4\x1c"\x02\x96\x80\xf6\x01<\xbf\x17\x98v)(\x00\xff\xfa`L\x02\xd4\xed\x04\xa6\x8c\x80#\x80\x9d\x00\x81w\x02\x02\xf0(\xe9\xde\x0cP?\t\x08\x80)\x80\xa0\x93\xc0tS\x80\x1d@\t\x11\xa0\xfc(0\xd5>\xc0\x04\xe0(@\xe0\xa3\x80\t\xc0\x14@\xe0)\xc0\x04Pq\xd1\xbd\x1a\xa4b\x12\x98b\x1f \x005\x17<\xfb\x0b\x88TO\x02C\xf3\xff\x03\x08v\xc1\xe9z,\x1c\xfe\x89a\x07\xf0\x9b\x0f\xcdQ\x80\xf2\xa3\xc0\xd0\xfb\x00\x01hW\x7fL\x86\xc3G\xc0\x11\xc0q\x80>\x0f\x83!\x8f\x03\x96\x80OF\xc0q\x80\x8a\xa3\xc0po\x06\x04\xe0\xd9\x8b\xee\xcd\x00\x13O\x86v\x00[|\x88\xa6\x00\xea&\x81a\xf6\x01\x02\xd0\xf7\x1c\x88I`\xa8\x08X\x02\x06\x1d\xfd\xd8\xff\x19f\x07\xb0\x18\x7fi\x88\xca\xa3\x80\x00,w\xc1\x1d\x05(\x9f\nw\x7f+`\x07`\x1f\xc0\xfeG\xc3\xdd\xf6\x01&\x00G\x01\x02\x1f\x05L\x00\xa6\x00\xc6\x98\x04v\x99\x02L\x00\r/\xb8\x9f\x0f\xa0b\x12\xd8e\x1f \x00\xad/\xb8I\x80\xf2)\xa0{\x04\x1c\x01z|\xc8&\x01\xeav\x02\xdd\x8e\x03&\x00\x93\x00\x81\'\x01?\t\x08\xbd\x15>\x0cz\xbc=0\x01t\xac\xbe\xa3\x00\x157x\x97)@\x00\xc6:\xfbA\xd7\x088\x02\xc0\xd8\x0f\x8d\xdc\xf2\xc1!\x00\x10\x98\x00\xc0\x1cG\x01\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x80\xceN>\x02\xa2K\xe7\xcb&\xbfO\xbe]M\x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\x80\x00\x00\x02\x00\x08\x00 \x00\xc0P\xd2\xac\xff\xe1\xf9v\xcd.\xdf\xc0_\xac\xf3\xc5\x870\xc1\xbdo\x02\x00G\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\x00\x10\x00@\x00\x00\x01\x00\x04\xa0\x97\xe4\xf2\x81\x9b\xc8\xdf\x0c\x1c\xf1\x8b\xe5o\x03Nq\xef\x1f\x17\xb8\xf9]J\x08\xbe\x03p\x1c\x80\x88\x01\xb8\x1b5E\x00\xa2?9\xed\x03\xb8\xfbn\x17}\x17\xb6\xdaW\xb4<\x8e\xbe\xff76\xb9W\x8f\x8b^x\xf0 \x08\x1a\x00\x11\x80\xa8\x01\xf0\xfa\tL\x00\xa6\x00(pZ\xf2\xce\xbf{3`)\x081\'\x00\x93\x00\x08\x80\x08@\xd8\x00\xf8A!0\x01\x00?8E\xf8CZ\n\x82\t\x00\x10\x00\xbb\x00\x88>\x01\x88\x00D\x0c\x80\xb7\x02`\x02\x00\x0eA\xde\x02<\x9a\x02\xbc\x15\xc0\x04\x10\x9b\xa3\x00\x02 \x02 \x00\xa1\x8f\x03\xbe\x0e\xd8\x01\xd8\t\xd8\t`\x02\x00\x04\xc0>\x00\x04@\x04@\x00b\xed\x03@\x00L\x01\xb0.o\x01\x1eO\x01\xde\n`\x020\t\x80\x00\x00\x02`\n\x00\x01\x08\xb8\x0f\xf0i\xb0\x1aK\xc0\xca\x08X\nb\x02p\x1c\x00\x01\x10\x01\x10\x80\xa8\xc7\x01\x10\x00S\x004\x7f\xe8$\x01\x18l\n\xf8\xfcG\x04h.\xdf\xae\xcd~oo\x01\xb6\x99\x04\xbc\x19`\xba\xa7\xbf\x00l\x7f\x1c\xc8\xff\xfb5v\x08c>d{\xdd\xac\xdf\x9e\xe6\xb9\xe0;\xe5\x1c\x0b3\x04`\xc6\xfb\xc9\x0e\x00\x02\x13\x00\x10\x00\x00\x00\x00\x00`Uo\xb5\r\x13~\xb2S\x92\xfa\x00\x00\x00\x00IEND\xaeB`\x82'
        root.wm_iconphoto(True, ImageTk.PhotoImage(Image.open(BytesIO(kode_icon))))

def get_image(path: str, pixel: tuple[int, int] = None):
    if pixel:
        return ImageTk.PhotoImage(Image.open(path).resize(pixel))
    else:
        return ImageTk.PhotoImage(Image.open(path))