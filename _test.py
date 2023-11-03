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

class test:
    def __init__(self) -> None:
        self.window = Tk()

    def _color(self, color: str) -> bool:
        if color is not None:
            try:
                self.window.configure(bg=color)
                return True
            except:
                return False
            finally:
                self.window.destroy()
        else:
            self.window.destroy()
            return False
    
    def apply_color(self, color: str, except_color: str) -> str:
        if self._color(color):
            return color
        else:
            return except_color