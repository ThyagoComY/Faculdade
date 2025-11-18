#include <stdio.h>
#include <string.h>

#define MAX 5 //maximo de 5 alunos

typedef struct{
    char nome[50];
    float nota[3], media;
    int matricula;
} Aluno;

void cadastrarAlunos(Aluno *alunos, int *quantidade);
void calcularMedias(Aluno *alunos, int quantidade);
float calcularMediaTurma(Aluno *alunos, int quantidade);
void exibirRelatorio(Aluno *alunos, int quantidade); 

int main(){
    
    Aluno turma[MAX];
    int qtd =5;

    cadastrarAlunos(turma, &qtd);
    calcularMedias(turma, qtd);
    exibirRelatorio(turma, qtd);
    
    return 0;
}

//parte de cadastrar os alunos
void cadastrarAlunos(Aluno *alunos, int *quantidade){

    for (int i=0; i<*quantidade; i++){
        printf("\nAluno %d\n", i+1);

        printf("Digite o nome do aluno: ");
        fgets((alunos+i)->nome, 50, stdin);
        (alunos+i)->nome[strcspn((alunos+i)->nome, "\n")] = '\0';     //isso faz com que n quebre a linha

        printf("Digite a matricula do aluno: ");
        scanf("%d", &(alunos+i)->matricula);

        getchar();
        
        for (int n=0; n<3;n++){
            printf("Nota %d:", n+1);
            scanf("%f", &(alunos+i)->nota[n]);
        }
        
        getchar();
    }
}

//calculo da media dos alunos de forma individual

void calcularMedias(Aluno *alunos, int quantidade){
    for (int i=0; i<quantidade; i++){
        float soma =0;
        for (int n=0; n<3; n++){
            soma += (alunos+i)->nota[n];
        }
        (alunos+i)->media = soma/3;
    }
}

//media geral da turma

float calcularMediaTurma(Aluno *alunos, int quantidade){
    float soma =0;

    for (int i=0; i<quantidade; i++){
        soma+=(alunos+i)->media;
    }

    return soma/quantidade;
}


//exibição do relatorio

void exibirRelatorio(Aluno *alunos, int quantidade){
    float maior = alunos[0].media;
    float menor = alunos[0].media;
    int aprovados = 0;


    for (int i=0; i<quantidade; i++){
        printf("\nAluno: %s\n", alunos[i].nome);
        printf("Matricula: %d\n", alunos[i].matricula);
        printf("Média: %.2f\n", alunos[i].media);

        if (alunos[i].media > maior){
            maior = alunos[i].media;
        }
        if (alunos[i].media < menor){ 
            menor = alunos[i].media;
        }
        if (alunos[i].media >= 7){
            aprovados++;
        }
    }
//aqui vai receber o calculo da media geral da turma
    float mediaTurma = calcularMediaTurma(alunos, quantidade);

    printf("\n----ANÁLISE DA TURMA-------\n");
    printf("Maior média: %.2f\n", maior);
    printf("Menor média: %.2f\n", menor);
    printf("Média geral da turma: %.2f\n", mediaTurma);
    printf("Número de alunos aprovados: %d\n", aprovados);
}
