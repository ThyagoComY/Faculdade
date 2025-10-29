conta1=float(input("Digite o valor da primeira conta: "))
conta2=float(input("Digite o valor da segunda conta: "))

juro1 = 0.02 * conta1
juro2 = 0.02 * conta2

total = conta1+conta2+juro1+juro2
restante = 1200-total
print(f"Resto do salário do João: {restante:.2f}")