salario = float(input("Digite o seu salário: "))
if salario<280:
    percentual=(100*0.20)/100
    aumento = salario*percentual
    salario_novo = salario + aumento

elif salario>=280 and salario<700:
    percentual=(100*0.15)/100
    aumento = salario*percentual
    salario_novo = salario + aumento

elif salario>=700 and salario<1500:
    percentual=(100*0.1)/100
    aumento = salario*percentual
    salario_novo = salario + aumento

else:
    percentual=(100*0.05)/100
    aumento = salario*percentual
    salario_novo = salario + aumento

print(f"\nSalário antes do reajuste: {salario}")
print(f"Percentual de aumento aplicado: {percentual*100:.1f}%")
print(f"Valor do aumento: {aumento}")
print(f"Salário depois do reajuste: {salario_novo}\n")