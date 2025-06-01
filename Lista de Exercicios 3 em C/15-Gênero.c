#include <stdio.h>
int main(){

char genero;

printf("Digite seu gênero de acordo com a letra\n");
printf("F ou M: ");
scanf(" %c", &genero);

if (genero == 'F' || genero == 'f'){
    printf("Feminino");
}
else if (genero == 'M' || genero == 'm'){
    printf("Masculino");
}
else
    printf("Sexo invalido");

return 0;
}
