n1=float(input("Digite o primeiro número: "))
n2=float(input("Digite o segundo número: "))

print("Qual operação deseja optar:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
op=input("Digite o número da operação correspondete: ")
if op == '1':
    resultado=n1+n2
    operacao = 'Soma'

elif op == '2':
    resultado=n1-n2
    operacao = 'Subtração'

elif op == '3':
    resultado=n1*n2
    operacao = 'Multiplicação'

elif op == '4':
    if n2 != 0:
        resultado=n1/n2
        operacao='Divisão'
    else:
        print("Erro, Evite um buraco negro, não divida por 0!")
        exit()
else:
    print("Opção inválida!")
    exit()

if resultado % 2 == 0:
    parimpar='Par'
else:
    parimpar='Ímpar'


if resultado > 0:
    sinal='Positivo'
else:
    sinal='Negativo'


if resultado == int:
    tipo='Inteiro'
else:
    tipo='Decimal'

print(f"\nA operação {operacao} resultou em {resultado}")
print(f"Sendo esse resultado um número {parimpar}, {sinal} e {tipo}\n")