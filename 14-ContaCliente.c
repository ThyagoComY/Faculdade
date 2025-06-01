#include <stdio.h>
int main (){

    float saldo, saldodis, debito, credito, num;

    printf("\nNumero de acesso da conta: ");
    scanf("%f", &num);

    printf("\nDigite o saldo disponivel: ");
    scanf("%f", &saldo);

    printf("\nDigite o debito: ");
    scanf("%f", &debito);

    printf("\nDigite o credito: ");
    scanf("%f", &credito);

    saldodis = saldo - (debito+credito);

    if (saldodis>0){
        printf("\n\nSaldo Positivo: %.2f\n\n", saldodis);
    }
    else if (saldodis<0){
        printf("\n\nSaldo Negativo: %.2f\n\n", saldodis);
    }
    else printf("\n\nSaldo Zerado ): \n\n");

return 0;
}

