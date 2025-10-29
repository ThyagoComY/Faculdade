turno = input("Em que turno você estuda?\n(M - Matutino, V - Vespertino, N - Noturno):\n")

if turno == 'M' or turno == 'm':
    print("Bom dia!")
elif turno == 'V' or turno == 'v':
    print("Boa tarde!")
elif turno == 'N' or turno == 'n':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
