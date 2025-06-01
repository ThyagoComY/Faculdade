#include <stdio.h>
int main(){

float n1 ,n2 ,n3 ,n4;

printf("Digite sua nota do primeiro bimestre: ");
scanf("%f", &n1);

printf("Digite sua nota do segundo bimestre: ");
scanf("%f", &n2);

printf("Digite sua nota do terceiro bimestre: ");
scanf("%f", &n3);

printf("Digite sua nota do quarto bimestre:");
scanf("%f", &n4);

if (n1>10 || n2>10 || n3>10 || n4>10){
    printf("\nErro, digite um numero entre 0 e 10\n");
    return 0;
}
else if (n1<0 || n2<0 || n3<0 || n4<0){
    printf("\nErro, digite um numero entre 0 e 10\n");
    return 0;
}
else
printf("Nota 1: %.2f\n", n1);
printf("Nota 2: %.2f\n", n2);
printf("Nota 3: %.2f\n", n3);
printf("Nota 4: %.2f\n", n4);

 return 0;
}
