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
#include "include/_copy.h"
#include "include/_check.h"
#include "include/_error.h"

#define MAX_FILE_SIZE 2147483648 //2 GiB (1024 * 1024 * 1024 * 2)

int create_file(char * filename)
{
    FILE * file;
    file = fopen(filename, "wb");

    if (file == NULL) return open_file_output;

    fclose(file);

    return 0;
}

int start_copy(char * filename, char * output, char * stopthread)
{
    FILE * file_input;
    file_input = fopen(filename, "rb");

    if (file_input == NULL) return open_file_input;

    long long size;
    size = size_of_file(filename, file_input);

    if (size == EMPTY) //empty file
    {
        int result;
        result = create_file(output);

        fclose(file_input);
        return result;
    }

    FILE * file_output;
    file_output = fopen(output, "wb");

    if (file_output == NULL)
    {
        fclose(file_input);
        return open_file_output;
    }

    int result;

    if (size >= MAX_FILE_SIZE) result = copy_with_malloc(output, stopthread, file_input, file_output);
    else result = copy_no_malloc(output, stopthread, file_input, file_output);

    fclose(file_input);
    fclose(file_output);

    if (result != 0) //there is an error
    {
        remove(output);
        return result;
    }

    return 0;
}