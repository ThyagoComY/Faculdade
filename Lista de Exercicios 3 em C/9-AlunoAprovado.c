#include <stdio.h>
#include <string.h>
int main(){

char nome[100], disciplina[30];
float p1, p2, p3, media;

printf("Digite seu nome: ");
fgets(nome, 100, stdin);
nome[strcspn(nome, "\n")] = '\0';

printf("Digite o nome da disciplina: ");
fgets(disciplina, 30, stdin);
disciplina[strcspn(disciplina, "\n")] = '\0';

printf("Digite a nota da primeira prova: ");
scanf("%f", &p1);

printf("Digite a nota da segunda prova: ");
scanf("%f", &p2);

printf("Digite a nota da terceira prova: ");
scanf("%f", &p3);

media = (p1+p2+p3)/3;

if (media >= 6){
    printf("\nNome do aluno: %s\n", nome);
    printf("Disciplina: %s\n", disciplina);
    printf("Nota da primeira prova: %.2f\n", p1);
    printf("Nota da segunda prova: %.2f\n", p2);
    printf("Nota da terceira prova: %.2f\n", p3);
    printf("Aluno Aprovado!! \nMedia: %.2f\n", media);
    return 0;
}
else
    printf("\nNome do aluno: %s\n", nome);
    printf("Disciplina: %s\n", disciplina);
    printf("Nota da primeira prova: %.2f\n", p1);
    printf("Nota da segunda prova: %.2f\n", p2);
    printf("Nota da terceira prova: %.2f\n", p3);
    printf("Aluno Reprovado! \nMedia: %.2f\n", media);

return 0;
}
