preco = float(input("Qual foi o valor da aquisição do produto? "))
if preco<50:
    preco = preco+preco*0.45
else:
    preco = preco+preco*0.30
print(f"\nO valor de revenda do produto será de R${preco:.2f}\n")