#include <stdio.h>
int main(){

char turno;

printf("\nDigite a letra correspondete ao seu turno:");
printf("\nM-Matutino\nV-Vespertino\nN-Noturno\n");
scanf("%c", &turno);
if (turno=='M' || turno=='m'){
    printf("Bom Dia!");
}
else if (turno=='V' || turno=='v'){
    printf("Boa Tarde!");
}
else if (turno=='N' || turno=='n'){
    printf("Boa Noite!");
}
else{
    printf("Valor Invalido!");
}
return 0;
}
