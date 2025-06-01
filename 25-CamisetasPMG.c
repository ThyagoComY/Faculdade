#include <stdio.h>
int main(){

float Pvalor, Mvalor, Gvalor;
int pequeno, medio, grande;

printf("Digite a quantidade de camisetas pequenas que deseja: ");
scanf("%d", &pequeno);

printf("Digite a quantidade de camisetas medias que deseja: ");
scanf("%d", &medio);

printf("Digite a quantidade de camisetas grande que deseja: ");
scanf("%d", &grande);

Pvalor = pequeno*10;
Mvalor = medio*12;
Gvalor = grande*15;

printf("\nValor das roupas:\n");
printf("Camisetas pequenas: R$%.2f\n", Pvalor);
printf("Camisetas medias: R$%.2f\n", Mvalor);
printf("Camisetas grandes: R$%.2f\n", Gvalor);


return 0;
}
