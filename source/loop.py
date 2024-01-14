# Copyright © 2024 APGR22

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def loop(list):
    cache_len = len(list)
    h = 0
    #
    #It will update itself if there are any changes
    #
    #Items in the list may decrease while it is being iterated resulting in changes to the index.
    #This is better handled with a while loop rather than a for loop
    while h < len(list):
        item = list[h]

        yield item

        if cache_len > len(list):
            #stay in this index
            h -= 1
            cache_len = len(list)

        h += 1

class _loop_variable:

    def loop(self, list):
        self.list = list
        cache_len = len(self.list)
        h = 0
        while h < len(self.list):
            item = self.list[h]

            yield item

            if cache_len > len(self.list):
                #stay in this index
                h -= 1
                cache_len = len(self.list)

            h += 1

loop_variable = _loop_variable()