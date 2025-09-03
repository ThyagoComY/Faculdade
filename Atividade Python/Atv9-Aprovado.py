nome=input("Digite o nome do aluno: ")
disciplina=input("Digite o nome da disciplina: ")
n1 = float(input("Digite a nota da primeira prova: "))
n2 = float(input("Digite a nota da segunda prova: "))
n3 = float(input("Digite a nota da terceira prova: "))

media = (n1+n2+n3)/3

if (media>=6):
    print("\nAluno", nome,"Aprovado na disciplina de", disciplina)
    print("Notas das 3 provas em sequência: ")
    print("Prova 1: ", n1)
    print("Prova 2: ", n2)
    print("Prova 3: ", n3)
    print("Media das notas: ", media, "\n")
else:
    print("\nAluno", nome,"Reprovado na disciplina de", disciplina)
    print("Notas das 3 provas em sequência: ")
    print("Prova 1: ", n1)
    print("Prova 2: ", n2)
    print("Prova 3: ", n3)
    print("Media das notas: ", media, "\n")  