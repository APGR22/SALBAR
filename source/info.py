from tkinter import *

def baca(nama: str, r: int | None = None, tambahkan: bool = False):...

class _info:
    def __init__(self):
        self.root: Tk
        self.kanvas: Canvas
        self.bingkai: Frame

        self.program_list: list[str]
        self.excluded_program_list: list[str]
        self.list_name: list[str]
        self.list_source: list[str]
        self.list_destination: list[str]
        self.nama_edit_timpa: dict[str, str]
        self.dict_program_list: dict[str, IntVar | Checkbutton | object | Label | Label]
        self.sort_key: str
        self.baca = baca

        self.selected: str
        self.confirm_to_overwrite: IntVar
        self.confirm_to_skip: IntVar
        self.confirm_to_use_c: IntVar

info = _info()