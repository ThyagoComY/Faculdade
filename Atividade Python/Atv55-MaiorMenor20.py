numbers = []
while True:
    n1=int(input("Digite um número: "))
    numbers.append(n1)
    if len(numbers) == 20:
        maior = max(numbers)
        menor = min(numbers)
        print(f"Maior: {maior} Menor: {menor}")
        exit()
