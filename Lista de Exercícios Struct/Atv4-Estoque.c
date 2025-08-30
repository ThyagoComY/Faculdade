#include <stdio.h>
#include <string.h>

struct Produto{

char nome[60];
float preco, estoque;
int quant;

};

int main(){

    struct Produto produto;

    printf("Digite o nome do produto: ");
    fgets(produto.nome, 60, stdin);
    produto.nome[strcspn(produto.nome, "\n")] = '\0';

    printf("Digite o preco do produto: ");
    scanf("%f", &produto.preco);

    printf("Digite a quantidade do produto: ");
    scanf("%d", &produto.quant);

    produto.estoque = produto.preco*produto.quant;

    printf("\nO valor total do produto %s em estoque eh: %.2f\n",produto.nome, produto.estoque);


return 0;
}
