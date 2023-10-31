from tkinter import Toplevel, Frame, HORIZONTAL, X
from tkinter.ttk import Progressbar, Label
from gui.styles import *


def make_progress(width_screen: int, height_screen: int):
    progress_window = Toplevel()
    progress_window.resizable(0, 0)
    wp = 500
    hp = 96
    xp = (width_screen/2) - (wp/2)
    yp = (height_screen/2) - (hp/2)

    progress_window.geometry('%dx%d+%d+%d' % (wp, hp, xp, yp))
    progress_window.withdraw()

    def config_pack_label(label: Label):
        label.config(font=(JUST_FONT, 9))
        label.pack(fill=X)

    progress_frame_title = Frame(progress_window)
    progress_frame_title.pack(fill=X, expand=True, pady=5)
    progress_title_label = Label(progress_frame_title)
    config_pack_label(progress_title_label)
    progress_title = Progressbar(progress_frame_title, orient=HORIZONTAL, mode='determinate')
    progress_title.pack(fill=X)

    progress_frame_source = Frame(progress_window)
    progress_frame_source.pack(fill=X, expand=True, pady=5)
    progress_label = Label(progress_frame_source)
    config_pack_label(progress_label)
    progress = Progressbar(progress_frame_source, orient=HORIZONTAL, mode='determinate')
    progress.pack(fill=X)
    progress_info = Label(progress_frame_source, wraplength=500)
    config_pack_label(progress_info)

    progress_frame_destination = Frame(progress_window)
    progress_frame_destination.pack(fill=X, expand=True, pady=5)
    sub_progress_label = Label(progress_frame_destination)
    config_pack_label(sub_progress_label)
    sub_progress = Progressbar(progress_frame_destination, orient=HORIZONTAL, mode='determinate')
    sub_progress.pack(fill=X)
    sub_progress_info = Label(progress_frame_destination, wraplength=500)
    config_pack_label(sub_progress_info)

    def cegah_exit():
        pass

    def calculator_percent(count: int|float, total: list) -> (int|float):
        return (count+1)/len(total)*100
    
    def calculator_left(total: int, count: int) -> int:
        return len(total)-1 - count

    class do_progress:
        def progress_start():
            progress_window.grab_set()
            progress_window.focus_set()
            progress_window.deiconify()

        def progress(
                    title: str,
                    number_for_title: tuple[int, list],
                    number_s: tuple[int, list],
                    source_path: str,
                    number_d: tuple[int, list],
                    destination_path: str
                    ):
            progress_title_label["text"] = f"{calculator_left(number_for_title[1], number_for_title[0])} lefts: {title}"
            progress_title["value"] = calculator_percent(number_for_title[0], number_for_title[1])

            progress_label["text"] = f"Source: {calculator_left(number_s[1], number_s[0])} lefts"
            progress["value"] = calculator_percent(number_s[0], number_s[1])
            progress_info["text"] = source_path

            sub_progress_label["text"] = f"Destination: {calculator_left(number_d[1], number_d[0])} lefts"
            sub_progress["value"] = calculator_percent(number_d[0], number_d[1])
            sub_progress_info["text"] = destination_path
            
            new_hp = progress_window.winfo_reqheight()

            xp = (width_screen/2) - (wp/2)
            yp = (height_screen/2) - (new_hp/2)

            progress_window.geometry('%dx%d+%d+%d' % (wp, new_hp, xp, yp))

        def progress_stop():
            progress.stop()
            progress_window.grab_release()
            progress_window.withdraw()

    progress_window.protocol("WM_DELETE_WINDOW", cegah_exit)

    return do_progress

class simple_progress():
    def __init__(self):
        self.progress_window = Toplevel()
        self.progress_window.resizable(0, 0)

        self.progress = Progressbar(self.progress_window, orient=HORIZONTAL, mode='determinate')
        self.progress.pack(fill=X)

        wp = 500
        hp = 18
        xp = (self.progress_window.winfo_screenwidth()/2) - (wp/2)
        yp = (self.progress_window.winfo_screenheight()/2) - (hp/2)

        self.progress_window.geometry('%dx%d+%d+%d' % (wp, hp, xp, yp))
        self.progress_window.withdraw()

        self.progress_window.protocol("WM_DELETE_WINDOW", self.disable)

    def active(self):
        self.progress_window.deiconify()
        self.progress_window.grab_set()
        self.progress_window.focus_set()
    
    actived = active
    
    def disable(self):
        self.progress.stop()
        self.progress_window.grab_release()
        self.progress_window.withdraw()
    
    disabled = disable

    def set(self, value: int):
        self.progress["value"] = value
    
    def destroy(self):
        self.progress_window.destroy()
    
    delete = deleted = destroyed = destroy