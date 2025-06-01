#include <stdio.h>
int main(){

float preco, desconto;

printf("Digite o preco de um produto: ");
scanf("%f", &preco);

desconto = preco - (preco*0.10);

printf("Desconto de 10 porcento foi aplicado, resultando em R$%.2f\n", desconto);
return 0;
}
