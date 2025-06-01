#include <stdio.h>
int main(){

float peso, excesso, multa;

printf("Digite o peso do peixe que voce pegou: ");
scanf("%f", &peso);

excesso = peso-50;
multa = excesso*4;

if (excesso>0) {
    printf("\nPor voce ter pego um peixe de %.2f kg a mais, tera de pagar em multa cerca de: R$%.2f\n", excesso, multa);
}
else{
    printf("\nVoce nao recebera multa, pois voce pegou um peixe de %.2f kg, que esta abaixo do peso regulamentado. \n", peso);
}

return 0;
}
