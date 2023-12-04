#include <stdio.h>
#include <string.h>
#include "include/my_copy.h"
#include "include/my_move.h"
#include "include/_error.h"

const int safe_length = 4096; //1024 * 4

int start(char * filename, char * stopthread)
{
    char file_source[safe_length];
    char file_destination[safe_length];
    char file_mode[safe_length];

    FILE * file;
    file = fopen(filename, "r");

    if (file == NULL)
    {
        return file_argv;
    }

    int count = 0;
    int c;
    int switch_to = 0;
    int skip_newline = 0; //to avoid 2 newline characters

    int result;
    while ( (c = fgetc(file)) != EOF )
    {
        // printf("%c\n", c);

        if (c == '\n' || c == '\r')
        {
            // printf("%d\n", c);

            if (switch_to == 0 && skip_newline == 0)
            {
                switch_to = 1;
                count = 0;
                skip_newline = 1;

                // printf("0>1\n");
            }
            else if (switch_to == 1 && skip_newline == 0)
            {
                switch_to = 2;
                count = 0;
                skip_newline = 1;

                // printf("1>2\n");
            }
            else if (switch_to == 2 && skip_newline == 0)
            {
                switch_to = 0;
                count = 0;
                skip_newline = 1;

                // printf("2>0\n");

                if (strcmp(file_mode, "copy") == 0) result = start_copy(file_source, file_destination, stopthread);
                else result = start_move(file_source, file_destination, stopthread);

                printf("%d\n", result);

                //reset
                memset(file_source, 0, safe_length);
                memset(file_destination, 0, safe_length);
                memset(file_mode, 0, safe_length);
            }

            continue;
        }

        if (switch_to == 0)
        {
            file_source[count] = (char) c;
        }
        else if (switch_to == 1)
        {
            file_destination[count] = (char) c;
        }
        else
        {
            file_mode[count] = (char) c;
        }

        // printf("%s | %s | %s | %d | %d | %d\n", file_source, file_destination, file_mode, switch_to, count, c);

        if (skip_newline > 0) skip_newline = 0;
        count++;
    }

    fclose(file);

    return 0;
}