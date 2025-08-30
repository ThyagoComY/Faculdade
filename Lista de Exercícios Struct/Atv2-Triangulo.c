#include <stdio.h>

struct Retangulo{

        float altura;
        float base;
        float area;
};

    int main(){

        struct Retangulo retangulo;
            printf("Digite a base do retangulo: ");
            scanf("%f", &retangulo.base);

            printf("Digite a altura do retangulo: ");
            scanf("%f", &retangulo.altura);

            retangulo.area = (retangulo.base*retangulo.altura);

            printf("A area do retangulo sera: %.2f", retangulo.area);

        return 0;}

