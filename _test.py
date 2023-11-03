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