#include <stdio.h>
int main(){

float distancia, consumo, preco, custo;

printf("Digite a distancia em KM da viagem: ");
scanf("%f", &distancia);

printf("Digite o consumo medio do seu veiculo: ");
scanf("%f", &consumo);

printf("Digite o preço do litro do combustivel na sua regiao: ");
scanf("%f", &preco);

custo = (distancia/consumo)*preco;

printf("O custo estimado com o combustivel sera de %.2f \n", custo);

return 0;
}
