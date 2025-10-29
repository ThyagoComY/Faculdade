valor_horas = float(input("Digite o valor da sua hora: "))
horas = float(input("Digite as suas horas trabalhadas no mês: "))

salario_bruto = valor_horas*horas

if salario_bruto<900:
    inss = (100*0.1)/100
    fgts = (100*0.11)/100
    ir=0
    salario_liq = (salario_bruto-salario_bruto*inss)+salario_bruto*fgts

elif salario_bruto<1500:
    ir = (100*0.05)/100
    inss = (100*0.1)/100
    fgts = (100*0.11)/100
    salario_liq = ((salario_bruto-salario_bruto*inss)-salario_bruto*ir)+salario_bruto*fgts

elif salario_bruto<2500:
    ir = (100*0.10)/100
    inss = (100*0.1)/100
    fgts = (100*0.11)/100
    salario_liq = ((salario_bruto-salario_bruto*inss)-salario_bruto*ir)+salario_bruto*fgts

elif salario_bruto>=2500:
    ir = (100*0.20)/100
    inss = (100*0.1)/100
    fgts = (100*0.11)/100
    salario_liq = ((salario_bruto-salario_bruto*inss)-salario_bruto*ir)+salario_bruto*fgts

print(f"\nSalário bruto: R${salario_bruto:.2f}")
print(f"IR: {ir*100:.1f}%")
print(f"INSS: {inss*100:.1f}%")
print(f"FGTS: {fgts*100:.1f}%")
print(f"Total descontos:: {(ir+inss)*100:.1f}%")
print(f"Salário líquido: R${salario_liq:.2f}\n")

