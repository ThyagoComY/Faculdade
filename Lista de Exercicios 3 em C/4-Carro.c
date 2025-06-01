#include <stdio.h>
#include <string.h>
int main(){

char nome[100], placa[9], modelo[50], cor[30];

printf("Digite seu nome: ");
fgets(nome, 100, stdin);
nome[strcspn(nome, "\n")] = '\0';

printf("Digite a placa do carro: ");
fgets(placa, 9, stdin);
placa[strcspn(placa, "\n")] = '\0';

printf("Digite o modelo do carro: ");
fgets(modelo, 50, stdin);
modelo[strcspn(modelo, "\n")] = '\0';

printf("Digite a cor do carro: ");
fgets(cor, 30, stdin);
cor[strcspn(cor, "\n")] = '\0';

printf("Nome: %s\n", nome);
printf("Placa do carro: %s\n", placa);
printf("Modelo do carro: %s\n", modelo);
printf("Cor do carro: %s\n", cor);

return 0;
}
