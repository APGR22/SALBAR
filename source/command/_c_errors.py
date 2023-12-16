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

SUCCESS = b"0"

errors = {
    1: "Too few arguments",
    2: "Cannot open file from arguments",
    3: "Cannot open source file",
    4: "Cannot create destination file",
    5: "The process is stopped",
    6: "Cannot delete unfinished file",
    7: "Cannot delete source file",
    8: "Unable to allocate required memory"
}

def identify(results: bytes, list_errors: list[str]):
    list_results = results.splitlines()

    while True:
        try:
            list_results.remove(b"")
        except:
            break

    # for i in range(len(errors)):
    #     if i+1 in s:
    #         return errors[i+1]

    for result in list_results:
        name_result_int = result.split(b":")
        name = name_result_int[0]
        result_int = name_result_int[1]

        if result_int != SUCCESS:
            list_errors.append(f"{name.decode()}: {errors[int(result_int)]}")