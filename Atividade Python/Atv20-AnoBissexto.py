ano = int(input("Digite um ano: "))
if ano%4==0 or ano%100==0:
    if ano%400==0:
        print("Ano bissexto!")
    else:
        print("Ano não é bissexto!")
else:
    print("Ano não é bissexto!")