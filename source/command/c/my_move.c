#include <stdio.h>
#include "include/my_copy.h"
#include "include/_check.h"

int start_move(char * filename, char * output, char * stopthread)
{
    int result;
    result = start_copy(filename, output, stopthread);

    if (result != 0) return 1;

    if (file_exists(stopthread) == 0)
    {
        if (remove(filename) != 0) return 1;
    }

    return 0;
}