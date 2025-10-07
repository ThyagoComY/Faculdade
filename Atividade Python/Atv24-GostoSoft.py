queijo=int(input("Digite a quantidade que gostaria de comprar de fatias de queijo: "))
presunto=int(input("Digite a quantidade que gostaria de comprar de fatias de presunto: "))
carne=int(input("Digite a quantidade que gostaria de comprar de rodelas de hamburguer: "))

carnkg = carne*0.1
preskg = presunto*0.05
queikg = queijo*0.05

print(f"Quilos de presunto necessários para a compra: {preskg:.2f}kg")
print(f"Quilos de queijo necessários para a compra: {queikg:.2f}kg")
print(f"Quilos de carne necessários para a compra: {carnkg:.2f}kg")