valor=float(input("Digite o valor da conta: "))

valor_div = valor/3

maria = int(valor_div)
gabriel = int(valor_div)

william = valor - (maria+gabriel)

print(f"Parte de Maria: R${maria:.2f}")
print(f"Parte de Gabriel: R${gabriel:.2f}")
print(f"Parte de William: R${william:.2f}")
