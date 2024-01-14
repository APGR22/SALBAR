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

from gui import progress
import paths
from command import copycut
from command import _c
from command._for_command import *
import info
import loop

def command(command_info: progress.progress_bar,
            info: info._info,
            copy: bool,
            thread: dict[str, bool]
            ):
    """tanya: Overwrites for all\n
    skip: Skip overwrites\n
    (not active) command_info = ["title", "source", "destination"]"""

    if info.confirm_to_skip.get() == 1:
        skip = True
    else:
        skip = False

    if info.confirm_to_use_c.get() == 1:
        process_message = "Preparing the command to be executed"
        do = _c.writetofile
        c = True
    else:
        process_message = "Process"
        if copy:
            do = copycut.copy
        else:
            do = copycut.move
        c = False

    parent = command_info._get_window()

    total_name = len(info.list_name)

    user = False
    cancel = False
    success = False

    dict_success = {"success": False}

    list_s: list[str]
    list_d: list[str]
    list_s = []
    list_d = []

    list_error: list[str]
    list_error = []

    _c._createfile()
    _c.startthread()

    command_info.active()

    list_error_name: list[str]
    list_error_name = []
    list_path: list[str]
    list_path = []

    #https://stackoverflow.com/questions/16326853/enumerate-two-python-lists-simultaneously
    #https://www.learndatasci.com/solutions/python-valueerror-too-many-values-unpack/
    for count_n, (n, s, d) in enumerate(zip(info.list_name, info.list_source, info.list_destination)):
        if not thread["active"] or cancel:
            break

        command_info.set(
            progress_name = "title",
            value = (count_n+1)/total_name*100,
            title = f"{process_message}: {count_n+1}/{total_name}",
            message = n
        )

        ls = paths.separate_path(s)
        ld = paths.separate_path(d)
        total_source = len(ls)
        total_destination = len(ld)

        list_s.extend(ls)
        list_d.extend(ld)

        count_s = 0

        for s in loop.loop_variable.loop(ls):
            s: str
            count_s += 1

            if not thread["active"] or cancel:
                break

            command_info.set(
                progress_name = "source",
                value = (count_s)/total_source*100,
                title = f"Source: {count_s}/{total_source}",
                message = s
            )

            if s in list_error_name:
                if s in ls: #re-check
                    loop.loop_variable.list = ls = filter_list(ls, s)
                continue

            if os.path.isfile(s):
                file_method = True
            elif os.path.isdir(s):
                file_method = False
            else:
                list_error.append(f"{n}: No source file or folder found: '{s}'")
                list_error_name.append(s)
                count_s += ls.count(s) - 1 #total count - one of them
                loop.loop_variable.list = ls = filter_list(ls, s)
                continue

            for count_d, d in enumerate(ld):
                if not thread["active"] or cancel:
                    break

                command_info.set(
                    progress_name = "destination",
                    value = (count_d+1)/total_destination*100,
                    title = f"Destination: {count_d+1}/{total_destination}",
                    message = d
                )

                if f"{s}-{d}" in list_path:
                    continue

                list_path.append(f"{s}-{d}")

                make_dir(d)
                d = os.path.join(d, os.path.basename(s))

                if info.confirm_to_overwrite.get() == 0:
                    result = if_exists(d, info.confirm_to_skip, parent)

                    if result == "skip": #if exists
                        skip = True
                        continue
                    elif result == False: #No
                        user = True
                        continue
                    elif result == None: #Cancel
                        cancel = True
                        break
                    #elif result == True: Yes

                result = do(n, s, d, file_method, copy)
                if result is not None: #error
                    list_error.append(result)
                else:
                    success = True

    command_info.destroy()

    if copy:
        method = "COPIED"
        message = "copying"
    else:
        method = "MOVED"
        message = "moving"

    if success and c:
        progress_copymove = progress.simple_progress_messagebox(thread)
        progress_copymove.set(f"Start {message}")
        progress_copymove.active()
        progress_copymove.start()

        _c.copymove(list_error)
        if not copy:
            for s, d in zip(list_s, list_d):
                d = os.path.join(d, os.path.basename(s))
                rmtree(s, d)

        progress_copymove.stop()
        progress_copymove.destroy()

    if user or not thread["active"]:
        additional = " AND SOME CANCELLATIONS"
    elif skip:
        additional = " AND SOME SKIP"
    else:
        additional = ""

    if dict_success["success"]:
        success = True

    if len(list_error) > max_error:
        write_error(list_error)
        error = f'(SEE "{os.path.join(os.getcwd(), "errors.txt")}")'
    else:
        error = ",\n".join(list_error) #will empty if list_error empty too

    #success and error
    if success and error:
        text = f"SUCCESSFULLY {method} FILE(S) WITH ERROR(S): " + error + additional
    #success
    elif success and additional:
        text = f"SUCCESSFULLY {method} FILE(S)"+additional
    elif success:
        text = f"SUCCESSFULLY {method} FILE(S)"
    #error
    elif error and additional:
        text = f"ERROR(S): " + error + additional
    elif error:
        text = f"ERROR(S): " + error
    #else
    elif skip:
        text = "SKIP"
    elif cancel or user:
        text = "CANCELED"
    else:
        text = "There are currently no messages available. Go home now"

    return text