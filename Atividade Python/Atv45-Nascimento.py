nasc_dia=int(input("Digite o dia seu nascimento: "))
nasc_mes=int(input("Digite o mes seu nascimento: "))
nasc_ano=int(input("Digite o ano seu nascimento: "))

dia=int(input("Digite o dia atual: "))
mes=int(input("Digite o mes atual: "))
ano=int(input("Digite o ano atual: "))

if nasc_dia<=31 and dia<=31 and nasc_mes<=12 and mes<=12:
    idade_ano = ano - nasc_ano

    idade_mes = (idade_ano *12) + (mes-nasc_mes)

    idade_dia = idade_mes * 30

    print(f"\nIdade em Anos: {idade_ano}")
    print(f"Idade em Meses: {idade_mes}")
    print(f"Idade em Dias: {idade_dia}\n")
else:
    print("Digite a data corretamente!")
    exit()
