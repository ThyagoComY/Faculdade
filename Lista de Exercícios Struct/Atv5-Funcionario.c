#include <stdio.h>
#include <string.h>

struct Funcionario{

float salario, bonus;
char nome[50];
int anos;

};

int main(){

    struct Funcionario funcionario;

        printf("Digite o nome do Funcionario: ");
        fgets(funcionario.nome, 50, stdin);
        funcionario.nome[strcspn(funcionario.nome, "\n")] = '\0';

        printf("Digite o salario do funcionario: ");
        scanf("%f", &funcionario.salario);

        printf("Digite os anos trabalhados pelo funcionario: ");
        scanf("%d", &funcionario.anos);

        if (funcionario.anos<3){
            funcionario.bonus = funcionario.salario+(funcionario.salario * 0.05);
            printf("O %s, que recebia %.2f, por ter trabalho %d ano(s), recebera %.2f ", funcionario.nome, funcionario.salario, funcionario.anos, funcionario.bonus);
        }
        else{
            funcionario.bonus = funcionario.salario+(funcionario.salario * 0.10);
            printf("O %s, que recebia R$%.2f, por ter trabalho %d ano(s), recebera R$%.2f ", funcionario.nome, funcionario.salario, funcionario.anos, funcionario.bonus);
        }




return 0;
}
