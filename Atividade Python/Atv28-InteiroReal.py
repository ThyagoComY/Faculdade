n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = float(input("Digite um número real: "))

resultado1 = (2 * n1) * (n2 / 2)
resultado2 = (3 * n1) + n3
resultado3 = n3 ** 3

print(f"\nO produto do dobro do primeiro com metade do segundo é: {resultado1:.2f}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado2:.2f}")
print(f"O terceiro elevado ao cubo é: {resultado3:.2f}\n")
