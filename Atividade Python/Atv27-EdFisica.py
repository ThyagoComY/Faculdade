for i in range(50):
    i+=1
    matricula = input(f"Digite a matrícula do {i}º aluno: ")
    sexo = (input("Digite o sexo, F para Feminino e M para Masculino: "))
    altura = float(input("Digite a altura em cm: "))
    print("\nDigite o status físico de acordo com a tabela:")
    status = input("1 para Bom, 2 Para Regular, 3 para Ruim:\n")

    if sexo == 'f' or sexo =='F':
        if altura>170:
            qnt_fem_170=0
            qnt_fem_170+=1
    if sexo == 'm' or sexo == 'M':
        qnt_mas=0
        qnt_mas+=1
        if status=='1':
            qnt_mas_bom=0
            qnt_mas_bom+=1

print("##########---RESULTADO---##########")
print(f"A quantidade de mulheres com altura maior que 170 é {qnt_fem_170}")
porc_mas_bom = qnt_mas_bom*100/qnt_mas
print(f"A porcentagem de homens com status fisico Bom em relação aos outros homens: {porc_mas_bom}")