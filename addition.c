#include <cs50.h>
#include <stdio.h>

// A function that adds 2 user inputted integers
int main(void)
{
    int x = get_int("x: "); //ask for a first integer
    int y = get_int("y: "); //ask for a second integer

    printf("%i\n", x+y);
}