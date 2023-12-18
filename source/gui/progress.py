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

from tkinter import Toplevel, Frame, HORIZONTAL, X, Y, LEFT
from tkinter.ttk import Progressbar, Label
from gui.styles import *
from command import _c
import threading
import time

class progress_bar():
    def __init__(self, progress_names: list[str], thread: dict[str, bool]) -> None:
        self.progress_window = Toplevel()
        self.progress_window.configure(bg=PROGRESS_BACKGROUND)
        self.progress_window.resizable(0, 0)

        self.progress_list = {} #{str: [Label, Progressbar, Label]}

        for progress_name in progress_names:
            progress_frame = Frame(self.progress_window, bg=PROGRESS_BACKGROUND)
            progress_frame.pack(fill=X, expand=True, pady=5)

            progress_title = Label(progress_frame, font=(just_font, 9), foreground=PROGRESS_FOREGROUND)
            progress_title.pack(fill=X)
            progress_title.configure(background=PROGRESS_BACKGROUND)

            progress = Progressbar(progress_frame, orient=HORIZONTAL, mode='determinate')
            progress.pack(fill=X)

            progress_msg = Label(progress_frame, wraplength=490, font=(just_font, 9), foreground=PROGRESS_FOREGROUND)
            progress_msg.pack(fill=X)
            progress_msg.configure(background=PROGRESS_BACKGROUND)

            self.progress_list[progress_name] = [progress_title, progress, progress_msg]

        w = 500
        h = self.progress_window.winfo_reqheight()
        x = (self.progress_window.winfo_screenwidth()/2) - (w/2)
        y = (self.progress_window.winfo_screenheight()/2) - (h/2)

        self.progress_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.progress_window.withdraw()

        def exit():
            thread["active"] = False
            _c.stopthread()

        self.progress_window.protocol("WM_DELETE_WINDOW", exit)

    def _get_window(self):
        return self.progress_window

    def _auto_config(self):
        w = 500
        h = self.progress_window.winfo_reqheight()

        self.progress_window.geometry('%dx%d' % (w, h))

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

class simple_progress_messagebox:
    def __init__(self, thread: dict[str, bool]):
        self.progress_window = Toplevel()
        self.progress_window.resizable(0, 0)
        self.progress_window.configure(bg=PROGRESS_BACKGROUND)

        wp = 200
        hp = 80
        xp = (self.progress_window.winfo_screenwidth()/2) - (wp/2)
        yp = (self.progress_window.winfo_screenheight()/2) - (hp/2)

        self.progress_window.geometry('%dx%d+%d+%d' % (wp, hp, xp, yp))
        self.progress_window.withdraw()

        self.progress_window.protocol("WM_DELETE_WINDOW", self.disable)

        self.font_size = 13
        self.padx = 15

        self.message = Label(self.progress_window, font=(just_font, self.font_size), background=PROGRESS_BACKGROUND, foreground=PROGRESS_FOREGROUND)
        self.message.pack(side=LEFT, fill=Y, padx=self.padx)

        self.loading = Label(self.progress_window, font=(just_font, self.font_size), background=PROGRESS_BACKGROUND, foreground=PROGRESS_FOREGROUND)
        self.loading.pack(side=LEFT, fill=Y, padx=self.padx)

        self.animation = "|/-\\"
        self.total_animation = len(self.animation)

        self.duration = 0.1 #s

        self.start_loading = False

        self.thread = thread

    def active(self):
        self.progress_window.deiconify()
        self.progress_window.grab_set()
        self.progress_window.focus_set()

    actived = active

    def disable(self):
        self.stop()

        _c.stopthread()
        self.message["text"] = "Cancel"
        self.thread["active"] = False

        #restart
        self.start()

    disabled = disable

    def set(self, message: str):
        self.message["text"] = message

    def _start(self):
        #https://stackoverflow.com/questions/7039114/waiting-animation-in-command-prompt-python
        #https://stackoverflow.com/questions/961344/what-does-the-percentage-sign-mean-in-python

        switch = 0
        while self.start_loading:
            self.loading["text"] = self.animation[switch % self.total_animation]
            switch += 1
            time.sleep(self.duration)

    def start(self):
        self.start_loading = True
        threading.Thread(target = self._start).start()

    def stop(self):
        self.start_loading = False
        self.loading["text"] = self.animation[0]

    def destroy(self):
        self.stop()
        time.sleep(self.duration)
        self.progress_window.destroy()

    delete = deleted = destroyed = destroy