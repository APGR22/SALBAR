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
#include <stdlib.h>
#include <string.h>
#include "include/my_copy.h"
#include "include/my_move.h"
#include "include/_check.h"
#include "include/_error.h"

const int safe_length = 4096; //1024 * 4
const size_t malloc_length = safe_length + 1;

int start(char * filename, char * stopthread)
{
    char buffer[safe_length];
    char * name; //0
    char * file_source; //1
    char * file_destination; //2
    char * file_mode; //3

    int switch_to = 0;

    int result;

    FILE * file;
    file = fopen(filename, "r");

    if (file == NULL)
    {
        return file_argv;
    }

    while (fgets(buffer, safe_length, file))
    {
        //https://stackoverflow.com/questions/2693776/removing-trailing-newline-character-from-fgets-input
        buffer[strcspn(buffer, "\r\n")] = 0; //remove newline

        //https://stackoverflow.com/questions/9593798/proper-way-to-copy-c-strings

        if (switch_to == 0)
        {
            name = malloc(malloc_length);
            name = strdup(buffer);
            switch_to++;
        }
        else if (switch_to == 1)
        {
            file_source = malloc(malloc_length);
            file_source = strdup(buffer);
            switch_to++;
        }
        else if (switch_to == 2)
        {
            file_destination = malloc(malloc_length);
            file_destination = strdup(buffer);
            switch_to++;
        }
        else
        {
            file_mode = malloc(malloc_length);
            file_mode = strdup(buffer);

            if (strcmp(file_mode, "copy") == 0) result = start_copy(file_source, file_destination, stopthread);
            else result = start_move(file_source, file_destination, stopthread);

            if (result != 0) printf("%s:%d\n", name, result);

            //https://stackoverflow.com/questions/43813188/calling-malloc-multiple-times

            free(name);
            free(file_source);
            free(file_destination);
            free(file_mode);

            switch_to = 0;

            if (file_exists(stopthread) == 0)
            {
                fclose(file);
                return stop_threading;
            }
        }
    }

    fclose(file);

    return 0;
}