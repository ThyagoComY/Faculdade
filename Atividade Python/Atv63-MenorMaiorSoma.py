qnt = int(input("Digite a quantidade de números a ser digitads: "))
numeros = []
for i in range(qnt):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

print(f"\nMenor numers: {menor}\nMaior núnemro: {maior}\nSoma dos números: {soma}\n")