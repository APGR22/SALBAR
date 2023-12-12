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

#include <stdio.h>
#include "include/_error.h"

int file_exists(char * file)
{
    FILE * search_file;

    search_file = fopen(file, "r");

    if (search_file == NULL) return 1;

    fclose(search_file);
    return 0;
}

int check_threading(char * stopthread, FILE * file, FILE * file_output, char * output, int cache_output_file_exists)
{
    if (file_exists(stopthread) != 0) return 1;

    fclose(file);
    fclose(file_output);

    if (cache_output_file_exists != 0)
    {
        if (remove(output) != 0) return rm_file_while_stop_threading;
    }

    return 0;
}