#include <stdio.h>
int main(){

int money;
int n100, n50, n10, n5, n1;

printf("Digite o valor em dinheiro quer gostaria de retirar: ");
scanf("%d", &money);

if (money>=10 && money<=600){
    n100 = money/100;
    money = money%100;

    n50 = money/50;
    money = money%50;

    n10 = money/10;
    money = money%10;

    n5 = money/5;
    money = money%5;

    n1 = money;

    printf("Notas entregues:\n");
    printf("Notas de 100 reais: %d\n",n100);
    printf("Notas de 50 reais: %d\n",n50);
    printf("Notas de 10 reais: %d\n",n10);
    printf("Notas de 5 reais: %d\n",n5);
    printf("Notas de 1 real: %d\n",n1);


}
else{
    printf("\nValor invalido! Digite um valor entre 10 e 600!");
}


return 0;
}
