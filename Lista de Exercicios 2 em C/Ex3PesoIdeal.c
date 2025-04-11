#include <stdio.h>
int main(){

float altura, homem, mulher;

printf("\nDigite sua altura em metros: ");
scanf("%f", &altura);

homem = (72.7*altura) - 58;
mulher = (62.1*altura) - 44.7;

printf("\nCom base na sua altura, foi calculado que o seu peso ideal seria:\nMulher: %.2f kg\nHomem: %.2f kg\n", mulher, homem);

return 0;
}
