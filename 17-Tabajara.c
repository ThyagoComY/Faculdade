#include <stdio.h>
int main(){

float bef_money, aft_money, more_money, percent;

printf("Digite seu salario atual: ");
scanf("%f", &bef_money);

if (bef_money <= 280){
    percent = 0.2;
    more_money = percent * bef_money;
    aft_money = bef_money+more_money;
    printf("\n\nSeu salario atual: %.2f\n", bef_money);
    percent = 0.2 * 100;
    printf("Percentual de aumento: %.2f\n", percent);
    printf("Valor do aumento: R$%.2f\n", more_money);
    printf("Salario apos aumento: R$%.2f \n\n\n", aft_money);
}
else if (bef_money <= 700 && bef_money > 280){
    percent = 0.15;
    more_money = percent * bef_money;
    aft_money = bef_money+more_money;
    printf("\n\nSeu salario atual: %.2f\n", bef_money);
    percent = 0.15 * 100;
    printf("Percentual de aumento: %.2f\n", percent);
    printf("Valor do aumento: R$%.2f\n", more_money);
    printf("Salario apos aumento: R$%.2f \n\n\n", aft_money);
}
else if (bef_money <= 1500 && bef_money > 700){
    percent = 0.10;
    more_money = percent * bef_money;
    aft_money = bef_money+more_money;
    printf("\n\nSeu salario atual: %.2f\n", bef_money);
    percent = 0.10 * 100;
    printf("Percentual de aumento: %.2f\n", percent);
    printf("Valor do aumento: R$%.2f\n", more_money);
    printf("Salario apos aumento: R$%.2f \n\n\n", aft_money);
}
else
    (bef_money > 1500);{                          //código desnecessariamente grande
    percent = 0.05;
    more_money = percent * bef_money;
    aft_money = bef_money+more_money;
    printf("\n\nSeu salario atual: %.2f\n", bef_money);
    percent = 0.05 * 100;
    printf("Percentual de aumento: %.2f\n", percent);
    printf("Valor do aumento: R$%.2f\n", more_money);
    printf("Salario apos aumento: R$%.2f \n\n\n", aft_money);
}

return 0;
}
