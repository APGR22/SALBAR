// Copyright © 2023 APGR22

// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at

//     http://www.apache.org/licenses/LICENSE-2.0

// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#define _FILE_OFFSET_BITS 64

#include <stdio.h>
#include "include/run.h"
#include "include/_error.h"

int main(int argc, char * argv[])
{
    if (argc < 3)
    {
        printf("args: %d", argc);
        return argc_less;
    }

    int result = start(argv[1], argv[2]);

    printf("%d\n", result);

    return 0;
}