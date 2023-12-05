#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include "include/_check.h"
#include "include/_error.h"

const int total_buffer = 12288; //1024 * 12
const size_t b_buffer = total_buffer;

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

    BYTE buffer[b_buffer];
    const BYTE empty[b_buffer]; //Please don't change this!!😫

    int file_output_exists = file_exists(output);

    FILE * file_output;
    file_output = fopen(output, "wb");

    if (file_output == NULL)
    {
        fclose(file_input);
        return open_file_output;
    }

    int total = 0;
    int c;

    //https://stackoverflow.com/questions/4823177/reading-a-file-character-by-character-in-c
    while ( (c = fgetc(file_input)) != EOF )
    {
        //append
        buffer[total] = (BYTE) c;
        total++;

        if (total == total_buffer)
        {
            if (check_threading(stopthread, file_input, file_output, output, file_output_exists) == 0) return stop_threading;

            fwrite(buffer, sizeof(buffer), 1, file_output);

            //reset
            memset(buffer, 0, b_buffer);
            total = 0;
        }
    }

    if (check_threading(stopthread, file_input, file_output, output, file_output_exists) == 0) return stop_threading;

    //jika buffer-nya masih ada
    if (memcmp(buffer, empty, b_buffer) != 0) fwrite(buffer, total, 1, file_output);

    // free(buffer);
    fclose(file_input);
    fclose(file_output);

    return 0;
}