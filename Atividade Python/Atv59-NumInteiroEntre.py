n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    n1, n2 = n2, n1
soma= 0
for i in range(n1, n2 + 1):
    soma += i

print(soma)
