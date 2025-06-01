#include <stdio.h>
int main(){

float area, base, altura;

printf("Digite a base do retangulo: ");
scanf("%f", &base);

printf("Digite a altura do retangulo: ");
scanf("%f", &altura);

area = base*altura;

printf("A area do retangulo sera %.2f", area);

return 0;
}
