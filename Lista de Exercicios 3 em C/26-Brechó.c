#include <stdio.h>
int main(){

float valor, lucro;

printf("Digite o valor do produto: ");
scanf("%f", &valor);

if (valor<50){
    lucro = valor+(valor*0.45);
    printf("O valor de revenda sera de R$%.2f", lucro);
}
else{
    lucro = valor+(valor*0.3);
    printf("O valor de revenda sera de R$%.2f", lucro);

}
return 0;
}
