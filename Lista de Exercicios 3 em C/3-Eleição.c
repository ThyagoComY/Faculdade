#include <stdio.h>
#include <string.h>
int main(){

char nome[100], titulo[12], numero[6];

printf("Digite seu nome: ");
fgets(nome, 100, stdin);
nome[strcspn(nome, "\n")] = '\0';

printf("Digite seu numero do titulo: ");
fgets(titulo, 12, stdin);
titulo[strcspn(titulo, "\n")] = '\0';

printf("Digite o numero do seu candidato: ");
fgets(numero, 100, stdin);
numero[strcspn(numero, "\n")] = '\0';

printf("Nome: %s\n", nome);
printf("Titulo eleitoral: %s\n", titulo);
printf("Numero do candidato: %s\n", numero);

return 0;
}
