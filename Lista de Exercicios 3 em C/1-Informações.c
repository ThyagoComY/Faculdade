#include <stdio.h>
#include <string.h>
int main(){

char nome[150], endereco[150], sexo[30], telefone[20];
int idade;

printf("Digite seu nome completo: ");
fgets(nome, 150, stdin);
nome[strcspn(nome, "\n")] = '\0';

printf("Digite sua idade: ");
scanf("%d", &idade);
getchar();

printf("Digite o seu Sexo: ");
fgets(sexo, 30, stdin);
sexo[strcspn(sexo, "\n")] = '\0';

printf("Digite seu endereco: ");
fgets(endereco, 150, stdin);
endereco[strcspn(endereco, "\n")] = '\0';

printf("Somente em numeros, digite seu telefone com o DDD: ");
fgets(telefone, 20, stdin);
telefone[strcspn(telefone, "\n")] = '\0';

printf("Nome: %s\n", nome);
printf("Idade: %d\n", idade);
printf("Sexo: %s\n", sexo);
printf("Endereco: %s\n", endereco);
printf("Telefone: %s\n", telefone);

return 0;
}
