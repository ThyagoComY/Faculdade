#include <stdio.h>
#include <string.h>
int main() {

    char nome[100];
    int idade;

    printf("Digite seu nome: ");
    fgets(nome, 100, stdin);

    nome[strcspn(nome, "\n")] = '\0';

    printf("Agora digite sua idade: ");
    scanf("%d", &idade);

    if (idade <= 2)
    {
        printf("\n\n%s esta com %d anos, e pela tabela e considerado um Bebe! \n\n", nome, idade);
        }
    else if (idade<=11 && idade>=3)
    {
        printf("\n\n%s esta com %d anos, e pela tabela e considerado uma crianca! \n\n", nome, idade);
        }
    else if (idade<=21 && idade>=12)
    {
        printf("\n\n%s esta com %d anos, e pela tabela e considerado um jovem adulto(a)! \n\n", nome, idade);
        }
    else if (idade<=64 && idade>=22)
    {
        printf("\n\n%s esta com %d anos, e pela tabela e considerado um adulto(a)! \n\n", nome, idade);
        }
    else if (idade<=100 && idade>=65)
    {
        printf("\n\n%s esta com %d anos, e pela tabela e considerado um idoso(a)! \n\n", nome, idade);
        }
    else
        printf("\n\n%s esta com %d anos, e pela tabela e considerado muito velho! \n\n", nome, idade);
return 0;
}
