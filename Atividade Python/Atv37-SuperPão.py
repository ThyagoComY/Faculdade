pedido = -1
total = 0
while pedido != 0:
    print("100 - Pãozinho |R$ 1,00")
    print("101 - Broa     |R$ 3,50")
    pedido=int(input("Digite o código da comida, quando terminar, digite 0: "))
    if pedido == 0:
        break
    
    elif pedido == 100:
        total += 1
    
    elif pedido == 101:
        total += 3.5

poupanca = total  *0.1


print(f"Total do pedido: R${total:.2f}")
print(f"Valor para guardar na poupança: R${poupanca:.2f}")