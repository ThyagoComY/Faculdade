consumo=float(input("Digite o consumo médio do carro: "))
viagem=float(input("Digite a distância da viagem: "))
preco=float(input("Digite o preço do combustível: "))

custo = (viagem/consumo)*preco

print("\nCusto estimado da viagem de carro: ", custo, "\n")