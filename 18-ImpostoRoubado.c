#include <stdio.h>
int main(){

float fgts, ir, sindicato, inss, salario_bruto, salario_liq, total_desc, valor_hora, horas;

printf("Digite seu valor por hora trabalhada: ");
scanf("%f", &valor_hora);

printf("Digite o tempo que você trabalha em horas: ");
scanf("%f", &horas);

salario_bruto = valor_hora*horas;
fgts = salario_bruto*0.11;
inss = salario_bruto*0.10;
sindicato = salario_bruto*0.03;

if (salario_bruto<900) {

    salario_liq = salario_bruto -(salario_bruto*0.10)+(salario_bruto*0.11);
    printf("Salario Bruto: R$%.2f\n", salario_bruto);
    printf("O valor descontado foi do INSS(10%%%) e foi pago adicional o FGTS (11%%%) ");
    printf("\nSeu salario liquido: %.2f\n\n\n", salario_liq);
}
else if (salario_bruto >= 900 && salario_bruto < 1500){

    ir = salario_bruto*0.05;
    total_desc = inss+ir+sindicato;
    salario_liq = salario_bruto-total_desc+fgts;
    printf("Salario Bruto: R$%.2f", salario_bruto);
    printf("Valores descontados:");
    printf("\nIR (5%%%): R$%.2f\nINSS (10%%%): R$%.2f\nSindicato (3%%%): R$%.2f", ir, inss, sindicato);
    printf("\nSalario liquido + FGTS (11%%%): R$%.2f\n\n", salario_liq);
}
else if (salario_bruto >= 1500 && salario_bruto < 2500){

    ir = salario_bruto*0.10;
    total_desc = inss+ir+sindicato;
    salario_liq = salario_bruto-total_desc+fgts;
    printf("Salario Bruto: R$%.2f", salario_bruto);
    printf("Valores descontados:");
    printf("\nIR (10%%%): R$%.2f\nINSS (10%%%): R$%.2f\nSindicato (3%%%): R$%.2f", ir, inss, sindicato);
    printf("\nSalario liquido + FGTS (11%%%): R$%.2f\n\n", salario_liq);
}
else if (salario_bruto >= 2500){

    ir = salario_bruto*0.15;
    total_desc = inss+ir+sindicato;
    salario_liq = salario_bruto-total_desc+fgts;
    printf("Salario Bruto: R$%.2f", salario_bruto);
    printf("Valores descontados:");
    printf("\nIR (15%%%): R$%.2f\nINSS (10%%%): R$%.2f\nSindicato (3%%%): R$%.2f", ir, inss, sindicato);
    printf("\nSalario liquido + FGTS (11%%%): R$%.2f\n\n", salario_liq);
}

return 0;
}
