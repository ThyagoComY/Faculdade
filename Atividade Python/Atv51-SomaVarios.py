soma = 0
numero=int(input("Digite um número: "))
while numero!=-999:
    numero=int(input("Digite outro número (-999 para finalizar): "))
    if numero != (-999):
        soma=soma+numero
print(soma)