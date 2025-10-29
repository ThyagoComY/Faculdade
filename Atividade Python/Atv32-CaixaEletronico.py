money = int(input("Digite um valor entre 10 a 600 para retirar em dinheiro: "))
if money>=10 and money<=600:
    n100 = money//100
    money = money%100

    n50 = money//50
    money = money%50

    n10 = money//10
    money = money%10

    n5 = money//5
    money = money%5

    n1 = money

    print("Notas entregues:\n")
    print(f"Notas de 100 reais: {n100}")
    print(f"Notas de 50 reais: {n50}")
    print(f"Notas de 10 reais: {n10}")
    print(f"Notas de 5 reais: {n5}")
    print(f"Notas de 1 real: {n1}")
else:
    print("Valor Inválido, digite um valor entre 10 e 600!")