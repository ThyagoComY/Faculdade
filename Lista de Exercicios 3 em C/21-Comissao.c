#include <stdio.h>
int main(){

float comissao, valorvendas, salariofixo, salariofinal;

printf("Digite seu sal�rio fixo: ");
scanf("%f", &salariofixo);

printf("Digite o Valor das suas vendas: ");
scanf("%f", &valorvendas);

comissao = valorvendas*0.04;
salariofinal = comissao + salariofixo;

printf("Comiss�o: R$%.2f\nSalario Final: R$%.2f", comissao, salariofinal);


return 0;
}
