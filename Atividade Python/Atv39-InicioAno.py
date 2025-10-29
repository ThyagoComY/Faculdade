dia=int(input("Digite o dia de uma data (23): "))
mes=int(input("Digite o mes de uma data (07): "))
if mes == 1:
    passados = dia

elif mes>1 and mes<=12:
    passados = (mes-1) * 30 + dia

else:
    print("Digite um mês correto!")
    exit()
    
print(f"Passados-se {passados} dias")