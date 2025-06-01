#include <stdio.h>
int main(){

float area, altura, base;

printf("Digite a base do triangulo: ");
scanf("%f", &base);

printf("Digite a altura do triangulo: ");
scanf("%f", &altura);

area = (base*altura)/2;

printf("A area do triangulo sera %.2f", area);

return 0;
}
