#include <stdio.h>
#include "include/run.h"
#include "include/_error.h"

int main(int argc, char * argv[])
{
    if (argc < 3)
    {
        printf("args: %d", argc);
        return argc_less;
    }

    int result = start(argv[1], argv[2]);

    printf("%d\n", result);

    return 0;
}