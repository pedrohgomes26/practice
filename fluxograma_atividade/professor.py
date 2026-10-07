

continuar = "Sim"

while continuar == "Sim":
    aluno = input("Digite o nome do aluno: ")

    presenca = int(input("Digite a % de presença do aluno: "))

    media = float(input("Digite a media do aluno: "))

    if presenca >= 75:
        print("Aprovado")
    else:
        print("Reprovado")

    if media >= 6:
        print("aprovado")
    elif media == 5:
        print("Recuperação")
    else:
        print("Reprovado")

    continuar = input("Deseja continuar: ")