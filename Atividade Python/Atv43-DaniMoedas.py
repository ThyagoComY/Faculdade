moeda_um=int(input("Digite quantas moedas de 1 Centavos você tem: "))
moeda_cinco=int(input("Digite quantas moedas de 5 Centavos você tem: "))
moeda_dez=int(input("Digite quantas moedas de 10 Centavos você tem: "))
moeda_vinte=int(input("Digite quantas moedas de 25 Centavos você tem: "))
moeda_cinq=int(input("Digite quantas moedas de 50 Centavos você tem: "))
moeda_real=int(input("Digite quantas moedas de 1 Real você tem: "))

total_moeda_um = moeda_um *0.01
total_moeda_cinco = moeda_um *0.05
total_moeda_dez = moeda_um *0.10
total_moeda_vinte = moeda_um *0.25
total_moeda_cinq = moeda_um *0.50
total_moeda_real = moeda_um *1

total=total_moeda_cinco + total_moeda_cinq + total_moeda_dez + total_moeda_real + total_moeda_um + total_moeda_vinte
print(f"Total em reais: R${total:.2f}")