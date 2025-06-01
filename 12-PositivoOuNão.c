#include <stdio.h>
int main (){

float num;

    printf("digite um numero: ");
    scanf("%f", &num);

    if  (num > 0){
        printf("\n\nseu numero e positivo\n\n");
    } else if (num < 0) {
        printf("\n\nseu numero e negativo\n\n");
    } else printf("\n\nseu numero e igual a 0, nao sendo positivo e nem negativo\n\n");

return 0;
}

