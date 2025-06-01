#include <stdio.h>
int main(){

int frangos;
float total;

printf("Digite o numero de frango totais: ");
scanf("%d", &frangos);

total = (frangos*4)+((frangos*3.5)*2);

printf("O custo total da granja com os chips sera de %.2f\n", total);



return 0;
}
