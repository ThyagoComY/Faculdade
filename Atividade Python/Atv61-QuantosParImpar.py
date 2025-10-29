par = 0
impar = 0
for i in range(1,11):
    n1 = int(input("Digite Um número: "))
    if n1%2==0:
        par+=1
    else:
        impar += 1
print(f"Impares {impar}")
print(f"Pares {par}")