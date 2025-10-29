print("Escolha a carne que deseja comprar: \n")
print("Valores referente até 5kg:")
print("1 - Filé Duplo | R$ 34,90kg ")
print("2 - Alcatra | R$ 44,90kg ")
print("3 - Picanha | R$ 66,90kg ")
print("--------------------------------------")
print("Valores referente acima de 5kg:")
print("1 - Filé Duplo | R$ 35,80kg ")
print("2 - Alcatra | R$ 46,80kg ")
print("3 - Picanha | R$ 67,80kg \n")

tipo=int(input("Digite, de acordo com a numeração, a carne escolhida (1,2 ou 3): "))
quilo=float(input("Digite a quantidade em KG desejada: "))
cartao=input("Deseja utilizar o cartão da loja para ter 5%% de desconto?").upper

if tipo == 1:
    carne = 'Filé Duplo'
    preco = 34.9 if quilo <= 5 else 35.8
elif tipo == 2:
    carne = 'Alcatra'
    preco = 44.9 if quilo <= 5 else 46.8
elif tipo == 3:
    carne = 'Picanha'
    preco = 66.9 if quilo <= 5 else 67.8
else:
    print("algum dado errado")
    exit()

total = preco*quilo
desconto = total * 0.05 if cartao =='S' else 0
valor= total - desconto

print("\n===========================")
print(f"Carne: {carne}")
print(f"Quilos: {quilo:.2f} kg")
print(f"Preço por kg: R${preco:.2f}")
print(f"Preço total: R${total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if cartao == 'S' else 'Outro'}")
print(f"Desconto: R${desconto:.2f}")
print(f"Valor a pagar: R${valor:.2f}")
print("=========================")