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
#include <sys/stat.h>
#include "include/_check.h"
#include "include/_error.h"

#define EMPTY 0

const size_t b_buffer = 1024 * 512; //512 KB for safety because of better than 2 MB

typedef unsigned char BYTE;

void create_file(char * filename)
{
    FILE * file;
    file = fopen(filename, "wb");

    if (file != NULL) fclose(file);
}

int start_copy(char * filename, char * output, char * stopthread)
{
    // printf("%s | %s | %s\n", filename, output, stopthread);

    FILE * file_input;
    file_input = fopen(filename, "rb");

    if (file_input == NULL)
    {
        return open_file_input;
    }

    struct stat my_stat;

    int s = stat(filename, &my_stat);

    if (s == 0 && my_stat.st_size == 0) //empty file
    {
        create_file(output);
        fclose(file_input);
        return 0;
    }

    // BYTE buffer[b_buffer];
    BYTE * buffer;
    buffer = malloc(b_buffer);

    if (buffer == NULL) return memory_error;

    //check if the file previously existed
    int cache_output_file_exists = file_exists(output);

    remove(output);

    FILE * file_output;
    file_output = fopen(output, "wb");

    if (file_output == NULL)
    {
        fclose(file_input);
        return open_file_output;
    }

    int error;
    size_t size;

    // https://stackoverflow.com/questions/6160319/how-to-read-unsigned-character-array-using-gets
    // https://stackoverflow.com/questions/18255384/read-an-empty-file-with-fread

    while ( (size = fread(buffer, 1, b_buffer, file_input)) > EMPTY )
    {
        error = check_threading(stopthread, file_input, file_output, output, cache_output_file_exists);
        if (error == 0) return stop_threading;
        else if (error == rm_file_while_stop_threading) return rm_file_while_stop_threading;

        // printf("%lld\n", size);

        fwrite(buffer, 1, size, file_output);

        free(buffer);
        buffer = malloc(b_buffer);
    }

    free(buffer);
    fclose(file_input);
    fclose(file_output);

    return 0;
}