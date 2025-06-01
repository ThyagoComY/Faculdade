#include <stdio.h>
int main(){

int ano;

printf("Insira um ano: ");
scanf("%d", &ano);

if (ano % 4 == 0 || ano % 100 == 0){
    if (ano % 400 == 0){
        printf("Seu ano e bissexto!");
    }
    else{
        printf("Seu ano nao e bissexto");
    }
}
else{
    printf("Seu ano nao e bissexto");
}

return 0;
}
