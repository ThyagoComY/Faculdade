nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 0 and idade <= 2:
    tipo = "bebê"
elif idade >= 3 and idade <= 11:
    tipo = "Criança"
elif idade >= 12 and idade <= 21:
    tipo = "Jovem"
elif idade >= 22 and idade <= 64:
    tipo = "Adulto"
elif idade >= 65 and idade <= 100:
    tipo = "Idoso"
else:
    tipo = "Muito velhinho"

print(f"{nome} está com {idade} anos e pela tabela é considerado um {tipo}")