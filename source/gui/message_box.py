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
from tkinter import ttk
from gui import image
from gui.styles import *

def create(
            title: str,
            message: str,
            options: list[str],
            icon_path: str,
            button_padx: int = 5,
            window_height: int = 100,
            bell: bool = False,
            use_checkbutton: bool = False,
            checkbutton_text: str = "",
            ) -> tuple[str, str]:
    """return (option, checkbutton_value: default is 0 if not using the checkbutton)"""
    message_window = Toplevel()
    message_window.title(title)
    message_window.resizable(0,0)
    message_window.grab_set()
    message_window.focus_set()

    message_window.bind("<Escape>", lambda e: message_window.destroy())

    w = 500
    h = window_height
    w_screen = message_window.winfo_screenwidth()
    h_screen = message_window.winfo_screenheight()
    x = (w_screen/2) - (w/2)
    y = (h_screen/2) - (h/2)
    message_window.geometry("%dx%d+%d+%d" % (w, h, x, y))

    #Up-Start

    main_frame = Frame(message_window, bg=messagebox_background)
    main_frame.pack(fill=BOTH)

        #Left-Start

    icon_frame = Frame(main_frame, bg=messagebox_background)
    icon_frame.pack(fill=Y, side=LEFT)

    img = image.get_image(icon_path, (64,64)) #must be saved to memory
    icon_image = Label(icon_frame, image=img, bg=messagebox_background)
    icon_image.pack(fill=BOTH, padx=5)

        #Left-End

        #Right-Start

    message_frame = Frame(main_frame, bg=messagebox_background)
    message_frame.pack(fill=Y, side=LEFT)

    message_text = Label(main_frame, text=message, wraplength=80/100*w, bg=messagebox_background, font=(just_font, 9))
    message_text.pack(fill=BOTH, expand=True)

        #Right-End

    #Up-End

    checkbutton_value = StringVar(value=0)

    if use_checkbutton:

        checkbutton_frame = Frame(main_frame, bg=messagebox_background)
        checkbutton_frame.pack()

        checkbutton = Checkbutton(
                                    checkbutton_frame,
                                    text=checkbutton_text,
                                    variable=checkbutton_value,
                                    wraplength=80/100*w,
                                    bg=messagebox_background,
                                    activebackground=messagebox_background,
                                    highlightthickness=0,
                                    font=(just_font, 9)
                                    )
        checkbutton.pack()

    #Down-Start

    option_frame = Frame(message_window, bg=messagebox_button_frame_background)
    option_frame.pack(fill=BOTH, pady=9)

    button_frame = Frame(option_frame, bg=messagebox_button_frame_background)
    button_frame.pack()

    global get_value
    get_value = ""

    def return_option(option: str, *event):
        global get_value
        get_value = option
        message_window.destroy()
    
    button_list = [ttk.Button] #just for Visual Studio Code (pylance extension) annotation
    button_list.clear()

    def switch(event, n: int):
        button_list[n].focus_set()

    if use_checkbutton:
        checkbutton.bind("<FocusIn>", lambda e: button_list[0].focus_set())

    for n, option in enumerate(options):

        if len(options) > 1:
            if n == 0: #first
                before = len(options) - 1 #end
                after = n+1
            elif n == len(options)-1: #last
                before = n-1
                after = 0 #start
            else:
                before = n-1
                after = n+1
        else:
            before = 0
            after = 0

        button = ttk.Button(button_frame, text=option, command=lambda set_option=option:return_option(set_option)) #"https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments"
        button.pack(fill=Y, expand=True, side=LEFT, padx=button_padx)

        button_list.append(button)

        button.bind("<Left>", lambda e, set_before=before: switch(e, set_before))
        button.bind("<Up>", lambda e, set_before=before: switch(e, set_before))
        button.bind("<Right>", lambda e, set_after=after: switch(e, set_after))
        button.bind("<Down>", lambda e, set_after=after: switch(e, set_after))
        button.bind("<Return>", lambda e, set_option=option:return_option(set_option, e))

        if n == 0:
            button.focus_set()

    #Down-End

    if bell:
        message_window.bell()
    message_window.wait_window()

    return get_value, checkbutton_value.get()