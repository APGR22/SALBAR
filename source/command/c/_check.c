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

int check_threading(char * stopthread, FILE * file, FILE * file_output, char * output, int removefile)
{
    if (file_exists(stopthread) != 0) return 1;

    fclose(file);
    fclose(file_output);

    if (removefile != 0)
    {
        if (remove(output) != 0) return rm_file_while_stop_threading;
    }

    return 0;
}