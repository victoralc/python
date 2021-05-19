import random as rd


def jogar():

    print("################################")
    print("Bem vindo ao jogo da adivinhacao")
    print("################################")

    numero_secreto = rd.randrange(1, 101)
    tentativas = 3
    round = 1

    print("Qual o nivel de dificuldade")
    print("(1) Facil, (2) Medio, (3) Dificil")

    nivel = int(input("Escolha o nivel: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    for round in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(round, tentativas))
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("Voce digitou ", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Voce acertou.")
            break
        elif maior:
            print("Chute é maior que o numero secreto")
        elif menor:
            print("Chute é menor que o numero secreto")

    print("Fim de jogo")
    print("Numero secreto é: ", numero_secreto)
