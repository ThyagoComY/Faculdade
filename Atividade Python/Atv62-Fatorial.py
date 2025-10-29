n=int(input("Digite um número inteiro qualquer: "))
fat=1
for i in range(1,n+1):
    fat*=i
print(f"Fatorial desse número: {fat}")