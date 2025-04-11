#include <stdio.h>
int main(){

float dinhora, horas, soma;

printf("Quanto voce recebe por hora? ");
scanf("%f", &dinhora);

printf("Quantas horas voce trabalha no mes? ");
scanf("%f", &horas);

 soma = dinhora*horas;

 printf("voce recebe por mes %.2f", soma);

return 0;
}
