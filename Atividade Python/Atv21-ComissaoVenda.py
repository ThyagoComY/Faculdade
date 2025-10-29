salario=float(input("Digite seu salário fixo: "))
venda=float(input("Digite o valor das suas vendas: "))

comissao = 0.04*venda
salario_final=salario+comissao

print(f"\nValor da comissão: R${comissao:.2f}\nSalário final: R${salario_final:.2f}\n")