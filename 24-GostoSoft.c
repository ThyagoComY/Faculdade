#include <stdio.h>
int main(){

int queijo, presunto, carne;
float carnkg, preskg,queikj;

printf("Digite a quantidade que gostaria de comprar de fatias de queijo: ");
scanf("%d", &queijo);

printf("Digite a quantidade que gostaria de comprar de fatias de presunto: ");
scanf("%d", &presunto);

printf("Digite a quantidade que gostaria de comprar de rodelas de hamburguer: ");
scanf("%d", &carne);

carnkg = carne*0.1;
preskg = presunto*0.05;
queikj = queijo*0.05;

printf("\nQuilos de presunto: %.2fkg\n", preskg);
printf("Quilos de queijo: %.2fkg\n", queikj);
printf("Quilos de carne de hamburguer: %.2fkg\n", carnkg);


return 0;
}
