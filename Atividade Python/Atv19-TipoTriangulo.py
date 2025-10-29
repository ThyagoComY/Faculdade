lado1=float(input("Digite um dos lados de um triângulo: "))
lado2=float(input("Digite um outro lado do triângulo: "))
lado3=float(input("Digite um outro lado do triângulo: "))

if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>1:
    if lado1==lado2 and lado2==lado3:
        print("É um triângulo equilátero!")
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("É um triângulo isósceles!")
    else:
        print("É um triângulo escaleno!")
else:
    print("Matematicamente não faz sentido ser um triangulo com esses dados")