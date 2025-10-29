cinq=0
while True:
    n1=int(input("Digite um número (0 para finalizar): "))
    if n1 == 50:
        cinq += 1
    elif n1 == 0:
        print(cinq)
        exit()