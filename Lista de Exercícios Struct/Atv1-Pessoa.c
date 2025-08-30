#include <stdio.h>
#include <string.h>

struct Pessoa{
        char nome[50];
        int idade;
        float altura;
    };
    int main(){
        struct Pessoa pessoa;
            printf("Qual o seu nome? ");
            fgets(pessoa.nome, sizeof(pessoa.nome), stdin);
            pessoa.nome[strcspn(pessoa.nome, "\n")] = '\0';

            printf("Qual sua idade? ");
            scanf("%d", &pessoa.idade);

            printf("Qual sua altura em metros? ");
            scanf("%f", &pessoa.altura);

            printf("\nNome: %s\n", pessoa.nome);
            printf("Idade: %d\n", pessoa.idade);
            printf("Altura: %.2fm\n", pessoa.altura);




        return 0;
    }

