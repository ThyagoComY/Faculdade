#include <stdio.h>
int main(){

int numero, i, maior, menor;

printf("Digite o 1o numero: ");
scanf("%d", &numero);

maior = menor = numero; //ainda bem que fiz algo parecido quando fiz grupo com os veteranos

for (i=2; i<=3; i++){
    printf("Digite o %do Numero: ", i);
    scanf("%d", &numero);


if (numero > maior){
    (maior = numero);
}
if (numero < menor){
    (menor=numero);
}
}
printf("O maior numero e %d\n", maior);
printf("O menor numero e %d\n", menor);

return 0;
}
