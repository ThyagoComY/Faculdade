print("Cardápio \n")
print("--------------------------------------")
print("1 - Filé de frando grelhado      | R$ 34,90kg ")
print("2 - Bife à Milanesa              | R$ 44,90kg ")
print("3 - Strogonoff de Filé Mignon    | R$ 66,90kg ")
print("4 - Lagosta                      | R$ 126,90kg ")
print("5 - Moqueca                      | R$ 54,90kg ")
print("--------------------------------------")
comida=int(input("Digite a opção de comida que deseja:"))

if comida == 1:
    print("Deseja pagar a gorjeta do garçom de 10%% sobre o valor do prato?")
    gorjeta=input("S - Sim |N - Não\n").upper()
    if gorjeta=='S':
        comida = 34.9
        gorjeta = 0.1*comida
    elif gorjeta=='N':        
        comida = 34.9
        gorjeta = 0

if comida == 2:
    print("Deseja pagar a gorjeta do garçom de 10%% sobre o valor do prato?")
    gorjeta=input("S - Sim |N - Não\n").upper()
    if gorjeta=='S':
        comida = 44.9
        gorjeta = 0.1*comida
    elif gorjeta=='N':
        comida = 44.9
        gorjeta = 0

if comida == 3:
    print("Deseja pagar a gorjeta do garçom de 10%% sobre o valor do prato?")
    gorjeta=input("S - Sim |N - Não\n").upper()
    if gorjeta=='S':
        comida = 66.9
        gorjeta = 0.1*comida
    elif gorjeta=='N':
        comida = 66.9
        gorjeta = 0

if comida == 4:
    print("Deseja pagar a gorjeta do garçom de 10%% sobre o valor do prato?")
    gorjeta=input("S - Sim |N - Não\n").upper()
    if gorjeta=='S':
        comida = 126.9
        gorjeta = 0.1*comida
    elif gorjeta=='N':
        comida = 126.9
        gorjeta = 0

if comida == 5:
    print("Deseja pagar a gorjeta do garçom de 10%% sobre o valor do prato?")
    gorjeta=input("S - Sim |N - Não\n").upper()
    if gorjeta=='S':
        comida = 54.9
        gorjeta = 0.1*comida
    elif gorjeta=='N':
        comida = 54.9
        gorjeta = 0

print(f"Valor total a pagar: R${comida+gorjeta}")
