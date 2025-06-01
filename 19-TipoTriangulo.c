#include <stdio.h>
int main(){

float lado1, lado2, lado3;

printf("Digite o tamanho de um dos lados de um triangulo: ");
scanf("%f", &lado1);

printf("Digite o tamanho de um outro lado do triangulos: ");
scanf("%f", &lado2);

printf("Digite o tamanho de um outro lado do triangulo: ");
scanf("%f", &lado3);

if ((lado1+lado2>lado3) && (lado1+lado3>lado2) && (lado2+lado3>lado1)){

    if (lado1==lado2 && lado2==lado3){
        printf("E um triangulo equilatero");
}
    else if (lado1==lado2 || lado2==lado3 || lado1==lado3){
        printf("E um triangulo isosceles");
}
    else{
        printf("E um triangulo escaleno");
}
}else {
    printf("Os dados inseridos não fazem sentido matematicamente na formacao de um triangulo tlg?");
}

return 0;
}
