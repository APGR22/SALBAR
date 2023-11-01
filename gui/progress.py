from tkinter import Toplevel, Frame, HORIZONTAL, X
from tkinter.ttk import Progressbar, Label
from gui.styles import *

class progress_bar():
    def __init__(self, progress_names: list[str]) -> None:
        self.progress_window = Toplevel()
        self.progress_window.resizable(0, 0)

        self.progress_list = {} #{str: [Label, Progressbar, Label]}

        for progress_name in progress_names:
            progress_frame = Frame(self.progress_window)
            progress_frame.pack(fill=X, expand=True, pady=5)

            progress_title = Label(progress_frame, font=(JUST_FONT, 9))
            progress_title.pack(fill=X)

            progress = Progressbar(progress_frame, orient=HORIZONTAL, mode='determinate')
            progress.pack(fill=X)

            progress_msg = Label(progress_frame, wraplength=490, font=(JUST_FONT, 9))
            progress_msg.pack(fill=X)

            self.progress_list[progress_name] = [progress_title, progress, progress_msg]

        self._auto_config()
        self.progress_window.withdraw()

        def prevent_exit():
            pass

        self.progress_window.protocol("WM_DELETE_WINDOW", prevent_exit)

    def _auto_config(self):
        w = 500
        h = self.progress_window.winfo_reqheight()
        x = (self.progress_window.winfo_screenwidth()/2) - (w/2)
        y = (self.progress_window.winfo_screenheight()/2) - (h/2)

        self.progress_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def active(self):
        "window"
        self.progress_window.deiconify()
        self.progress_window.grab_set()
        self.progress_window.focus_set()
        self._auto_config()
    
    actived = active
    
    def disable(self):
        "window"
        self.progress_window.grab_release()
        self.progress_window.withdraw()
    
    disabled = disable

    def set(self, progress_name: str, value: int, title: str = "", message: str = ""):
        "progress"
        self.progress_list[progress_name][0]["text"] = title
        self.progress_list[progress_name][1]["value"] = value
        self.progress_list[progress_name][2]["text"] = message

        self._auto_config()

    def stop(self, progress_name: str):
        "progress"
        self.progress_list[progress_name][1].stop()

    reset = restart = stop

    def stop_all(self):
        "progress"
        for progress_name in self.progress_list:
            self.progress_list[progress_name][1].stop()
    
    reset_all = restart_all = stop_all
    
    def destroy(self):
        "window"
        self.progress_window.destroy()
    
    delete = deleted = destroyed = destroy

class simple_progress_bar():
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