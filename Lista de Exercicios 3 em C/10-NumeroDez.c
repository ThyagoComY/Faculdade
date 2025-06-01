#include <stdio.h>
int main    () {
    float numero;

    printf("Digite um numero: ");
    scanf("%f", &numero);

    if (numero<10){
        printf("\n\nO numero %.2f e menor do que dez\n\n", numero);

        } else if (numero>10){
        printf("\n\nO numero %.2f e maior do que dez\n\n", numero);

        } else{
        printf("\n\nO numero %.2f e igual a dez\n\n", numero);
        }
    return 0;
}

