#include <stdio.h>

int copy_no_malloc(char * output, char * stopthread, FILE * file_input, FILE * file_output);

//if malloc fails then copy_no_malloc
int copy_with_malloc(char * output, char * stopthread, FILE * file_input, FILE * file_output);