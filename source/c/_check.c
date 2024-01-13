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

#ifdef __linux__
    #define __USE_LARGEFILE64
    #define _LARGEFILE64_SOURCE
#endif

#include <stdio.h>
#include <sys/stat.h>
#include "include/_error.h"

int file_exists(char * file)
{
    FILE * search_file;

    search_file = fopen(file, "r");

    if (search_file == NULL) return -1;

    fclose(search_file);
    return 0;
}

int check_threading(char * stopthread, FILE * file, FILE * file_output, char * output)
{
    if (file_exists(stopthread) == -1) return -1;

    fclose(file);
    fclose(file_output);

    remove(output);

    return stop_threading;
}

long long size_of_file(char * filename, FILE * file)
{
    struct stat64 my_stat;

    int s = stat64(filename, &my_stat);

    if (s == 0) return my_stat.st_size;

    //alternative way

    long long size;

    fseeko64(file, 0, SEEK_END); //to end
    size = ftello64(file);
    fseeko64(file, 0, SEEK_SET); //to beginning

    return size;
}