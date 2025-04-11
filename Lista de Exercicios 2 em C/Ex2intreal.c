#include <stdio.h>
int main(){

int n1,n2;
float real, dobro, triplo, cubo;

printf("digite um numero inteiro: ");
scanf("%d", &n1);
printf("digite um outro numero inteiro: ");
scanf("%d", &n2);
printf("digite agora um numero real: ");
scanf("%f", &real);

dobro = (n1*2)*(n2/2);
triplo = 3*n1+real;
cubo = real*real*real;

printf("\nO produto do dobro do primeiro com metade do segundo sera %.2f", dobro);
printf("\nA soma do triplo do primeiro com o terceiro sera %.2f", triplo);
printf("\no terceiro elevado ao cubo sera %.2f\n\n", cubo);

return 0;
}
