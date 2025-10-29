qtd = 0
numero = int(input("Digite um número: "))

while numero != -1:
    qtd = qtd + 1
    numero = int(input("Digite outro número (-1 para finalizar): "))

print(f"A quantidade de números digitados foi {qtd}")