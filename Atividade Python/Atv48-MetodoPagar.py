valor=float(input("Digite o valor do produto: "))
print("\nFormas de pagamento:")
print("1-À vista em dinheiro ou pix (10% Desconto)")
print("2-À vista no crédito (5% Desconto)")
print("3-Em 2x sem juros")
print("4-Em 3x")
forma=int(input("Digite o número de acordo com a forma de pagamento: "))

if forma == 1:
    preco = valor-(valor*0.1)
    print(f"Preço a pagar: R${preco:.2f}")

elif forma == 2:
    preco = valor-(valor*0.05)
    print(f"Preço a pagar: R${preco:.2f}")

elif forma == 3:
    preco = valor/2
    print(f"Preço das parcelas: R${preco:.2}\nPreço total: R${valor:.2f}")

elif forma == 4:
    preco = valor*(1+0.1)**3
    parcela = preco / 3
    print(f"Preço das parcelas: R${parcela:.2f}\nPreço total: R${preco:.2f}")