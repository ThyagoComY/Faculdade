peso = float(input("Digite o peso de peixes em kg: "))


if peso > 50:
    excesso = peso- 50
    multa = excesso* 4
else:
    excesso= 0
    multa= 0

print(f"\nPeso total: {peso:.2f}kg")
print(f"Excesso: {excesso:.2f}kg")
print(f"Multa a pagar: R${multa:.2f}\n")
