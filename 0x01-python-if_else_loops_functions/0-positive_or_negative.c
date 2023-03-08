#include <stdio.h>
int main()
{
    signed number = srand(-10, 10)

    if (number > 0)
        printf("%lu is positive\n");
    else if (number == 0)
        printf("%lu is zero\n");
    else
        printf("%lu is negative\n");
    return 0;
}