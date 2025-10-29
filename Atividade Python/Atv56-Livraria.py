livros = int(input("Quantos livros você comprou no bimestre? "))

if livros == 0:
    pontos = 0
elif livros == 1:
    pontos = 5
elif livros == 2:
    pontos = 15
elif livros == 3:
    pontos = 30
else:
    pontos = 60

print(f"Você ganhou {pontos} pontos.")

if 20 <= pontos <= 30:
    print("Brindes disponíveis: Eco Bag ou Caneta personalizada.")
elif 35 <= pontos <= 60:
    print("Brindes disponíveis: Livro (até R$30) ou Luminária de cabeceira.")
elif pontos >= 65:
    print("Brindes disponíveis: 2 Livros (até R$100) ou Power Bank.")
else:
    print("Tem nada para você")
