#include <stdio.h>
int main(){

int matricula=0;
char sexo=0;
int altura=0;
int status=0;
int qnt_fem_170=0;
int porc_mas_bom=0;
int qnt_mas_bom=0;
int qnt_mas=0;
int i=0;

for (i=1; i<=50; i++){
    printf("Digite a matricula do %d aluno:\n", i);
    scanf("%d", &matricula);

    printf("Digite M para masculino e F para feminino: ");
    scanf("%s", &sexo);

    printf("Digite a altura do aluno em CM: ");
    scanf("%d", &altura);

    printf("Digite o estado fisico do aluno: (1-Bom, 2-Regular, 3-Ruim)\n");
    scanf("%d", &status);

    if (sexo == 'f' || sexo == 'F'){
        if (altura>170){
            qnt_fem_170++;
        }
    }
    if (sexo == 'M' || sexo == 'm'){
        qnt_mas++;
        if (status=='1'){
            qnt_mas_bom++;
        }
    }
}

    printf("##########RESULTADO##########");
    printf("A quantidade de mulheres com altura maior que 170 eh: %d", qnt_fem_170);
    porc_mas_bom = qnt_mas_bom*100/qnt_mas;
    printf("A porcentagem de homens com status fisico Bom em relação aos outros homens: %d", porc_mas_bom);

return 0;
}


