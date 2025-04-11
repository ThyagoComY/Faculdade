#include <stdio.h>
int main(){

float ganho_hora, horas_trab, salario, inss, imposto, sindicato, descontos, liquido;

printf("Quanto e o seu ganho por hora? ");
scanf("%f", &ganho_hora);

printf("Quantas horas trabalhou esse mes? ");
scanf("%f", &horas_trab);

salario = (ganho_hora*horas_trab);
inss = (salario * 0.08);
imposto = (salario * 0.11);
sindicato = (salario * 0.05);
descontos = (inss+imposto+sindicato);
liquido = (salario - descontos);

printf("O seu salario bruto e %.2f \n\nOs valores descontados foram: \nImposto de renda: R$%.2f \nINSS: R$%.2f \nSindicato: R$%.2f \nO salario liquido sera de R$%.2f\n\n", salario, imposto, inss, sindicato, liquido);

return 0;
}
