#include <stdio.h>
#include <stdlib.h>
#include "include/_check.h"
#include "include/_error.h"

#define BUFFER_SIZE 524288              //512 KiB (1024 * 512) for safety because of better than 2 MiB
#define MAX_BUFFER_SIZE 10485760        //10 MiB (1024 * 1024 * 10)

typedef unsigned char BYTE;

int copy_no_malloc(char * output, char * stopthread, FILE * file_input, FILE * file_output)
{
    BYTE buffer[BUFFER_SIZE];

    size_t size;
    
    // https://stackoverflow.com/questions/6160319/how-to-read-unsigned-character-array-using-gets
    // https://stackoverflow.com/questions/18255384/read-an-empty-file-with-fread
    while ( (size = fread(buffer, 1, BUFFER_SIZE, file_input)) > EMPTY )
    {
        if (check_threading(stopthread, file_input, file_output, output) == stop_threading) return stop_threading;

        fwrite(buffer, 1, size, file_output);
    }

    return 0;
}

int copy_with_malloc(char * output, char * stopthread, FILE * file_input, FILE * file_output)
{
    BYTE * buffer;
    buffer = malloc(MAX_BUFFER_SIZE);

    //alternative way if malloc fails
    if (buffer == NULL) return copy_no_malloc(output, stopthread, file_input, file_output);

    size_t size;

    while ( (size = fread(buffer, 1, MAX_BUFFER_SIZE, file_input)) > EMPTY )
    {
        if (check_threading(stopthread, file_input, file_output, output) == stop_threading)
        {
            //must free memory before ending the process
            free(buffer);

            return stop_threading;
        }

        fwrite(buffer, 1, size, file_output);

        //free the previous allocation and create a new allocation
        free(buffer);
        buffer = malloc(MAX_BUFFER_SIZE);

        //alternative way if malloc fails
        if (buffer == NULL) return copy_no_malloc(output, stopthread, file_input, file_output);
    }

    free(buffer);

    return 0;
}