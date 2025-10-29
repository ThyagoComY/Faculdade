lata = -1
total = 0
while lata != 0:
    print("100 - Lata 350ml    ")
    print("101 - Garrafa 600ml ")
    print("102 - Garrafa 2l    ")
    lata=int(input("Digite o código do Refrigerante que desejar, quando terminar, digite 0: "))
    if lata == 0:
        break
    
    elif lata == 100:
        total += 350
    
    elif lata == 101:
        total += 600
    
    elif lata == 102:
        total += 2000

total = total /1000

print(f"Total de litros em refrigerante: {total}l")