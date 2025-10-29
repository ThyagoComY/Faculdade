tipo=input("Digite o tipo de combustível: A-álcool, G-gasolina\n")
litro=int(input("Digite a quantidade, em litros, de combustível: "))

if tipo == 'A' or tipo == 'a':
    if litro<20:
        preco=(litro*1.9)-(litro*0.03)
    else:
        preco=(litro*1.9)-(litro*0.05)

elif tipo == 'G' or tipo == 'g':
    if litro<20:
        preco=(litro*2.5)-(litro*0.04)
    else:
        preco=(litro*2.5)-(litro*0.06)

print(f"Valor a ser pago {preco:.2f}")        