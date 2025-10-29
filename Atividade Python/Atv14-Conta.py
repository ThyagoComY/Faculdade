conta = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo: "))
debito = float(input("Digite o débito: "))
credito = float(input("Digite o crédito: "))

saldodeagora = saldo - debito + credito

print(f"A conta {conta} está com o saldo atual de R${saldodeagora:.2f}")

if saldodeagora >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
