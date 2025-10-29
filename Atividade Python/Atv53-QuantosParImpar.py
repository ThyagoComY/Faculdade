par = 0
impar = 0
while True:
    n1 = int(input("Digite Um número (-999 para finalizar): "))
    if n1%2==0:
        par=0
    elif n1==-999:
        print(impar)
        exit()
    else:
        impar += 1
