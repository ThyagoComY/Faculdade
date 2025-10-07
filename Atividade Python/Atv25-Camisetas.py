pequeno=int(input("Quantas camisetas pequenas você quer? "))
medio=int(input("Quantas camisetas médias você quer? "))
grande=int(input("Quantas camisetas grandes você quer? "))

Pvalor = pequeno*10;
Mvalor = medio*12;
Gvalor = grande*15;

print("\nValor das roupas:\n");
print(f"Camisetas pequenas: R${Pvalor:.2f}")
print(f"Camisetas medias: R${Mvalor:.2f}")
print(f"Camisetas grandes: R${Gvalor:.2f}")