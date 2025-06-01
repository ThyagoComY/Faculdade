#include <stdio.h>
#include <string.h>
int main(){

char nome[100], disciplina[30];
float prova1, prova2, prova3, media;

printf("Digite seu nome: ");
fgets(nome, 100, stdin);
nome[strcspn(nome, "\n")] = '\0';

printf("Digite o nome da disciplina: ");
fgets(disciplina, 30, stdin);
disciplina[strcspn(disciplina, "\n")] = '\0';

printf("Digite a nota da primeira prova: ");
scanf("%f", &prova1);

printf("Digite a nota da segunda prova: ");
scanf("%f", &prova2);

printf("Digite a nota da terceira prova: ");
scanf("%f", &prova3);

if (prova1>10 || prova2>10 || prova3>10){
    printf("\nErro, digite um numero entre 0 e 10\n");
    return 0;
}
else if (prova1<0 || prova2<0 || prova3<0){
    printf("\nErro, digite um numero entre 0 e 10\n");
    return 0;
}
else
media = (prova1+prova2+prova3)/3;

printf("\nNome: %s\n", nome);
printf("Nome da disciplina: %s\n", disciplina);
printf("Nota da primeira prova: %.2f\n", prova1);
printf("Nota da segunda prova: %.2f\n", prova2);
printf("Nota da terceira prova: %.2f\n", prova3);
printf("Media das notas: %.2f\n\n", media);



return 0;
}
