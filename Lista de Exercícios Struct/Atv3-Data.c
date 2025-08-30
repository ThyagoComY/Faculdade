#include <stdio.h>

struct Data{
    int dia;
    int mes;
    int ano;
};
int main(){

struct Data data;
printf("Digite o dia em numeros: ");
scanf("%d", &data.dia);

printf("Digite o mes em numeros: ");
scanf("%d", &data.mes);

printf("Digite o ano em numeros: ");
scanf("%d", &data.ano);

printf("\n%d/%d/%d\n", data.dia, data.mes, data.ano);




return 0;
}
