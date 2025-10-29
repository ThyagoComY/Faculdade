nome = input("Digite seu Nome: ")
sexo = input("De acordo com seu gênero\nDigite F para Feminino\nDigite M para Masculino\n").upper()
print("Sobre seu estado civil:")
print("1-Solteira(o)")
print("2-Casada(o)")
print("3-Divorciada(o)")
print("4-Viúva(o)")
print("5-União estável")
estado = int(input("Digite o número de acordo com seu estado civil: "))

if sexo == 'F' and estado == 2:
    tempo = input("Digite seu tempo de casada em anos: ")
    print("Agradecido!")
else:
    print("Agradecido!")