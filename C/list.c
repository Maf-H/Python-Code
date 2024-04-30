#include <stdio.h>
#include <stdlib.h>

int main(void){
    int *a = malloc(3 * sizeof(int));
    //int a[3];
    a[0] = 1;
    a[1] = 2;
    a[2] = 3;
    a[3] = 4;
    for (int i = 0; i < 3; i++){
        printf("%d \n", a[i]);
    }
}