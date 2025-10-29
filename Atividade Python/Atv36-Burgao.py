pedido = -1
total = 0
while pedido != 0:
    print("Digite o código do pedido que quiser:")
    print("Cachorro Quente  |100|     R$ 11,20")
    print("Ovo Simples      |101|     R$ 8,30")
    print("Bauru com Ovo    |102|     R$ 11,50")
    print("Hambúrguer       |103|     R$ 16,20")
    print("Refrigerante     |201|     R$ 6,00")
    print("Suco             |202|     R$ 7,50")
    print("Água Mineral     |203|     R$ 4,70")
    pedido=int(input("Digite o código do produto, quando terminar, digite 0: "))
    if pedido == 0:
        break
    
    elif pedido == 100:
        total += 11.2

    elif pedido == 101:
        total += 8.3

    elif pedido == 102:
        total += 11.5

    elif pedido == 103:
        total += 16.2

    elif pedido == 201:
        total =+ 6

    elif pedido == 202:
        total += 7.5

    elif pedido == 203:
        total += 4.7

print(f"Total do pedido: R${total:.2f}")
    
    