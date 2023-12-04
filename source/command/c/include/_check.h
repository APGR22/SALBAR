#include <stdio.h>

//check if the file exists
int file_exists(char * file);

//just a check with a slight drop in performance
int check_threading(char * stopthread, FILE * file, FILE * file_output, char * output, int removefile);