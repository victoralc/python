import re
import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = choose_word().upper()
    acertou_tudo = False
    enforcou = False
    acertou_parte_da_palavra = False
    letras_acertadas = ["_"] * len(palavra_secreta)  # List comprehension
    errors = 0

    while (not enforcou and not acertou_tudo) or acertou_parte_da_palavra:
        chute = input("Digite uma letra ou a palavra\n")
        chute = chute.strip().upper()

        if palavra_secreta == chute:
            print("Parabens! Resposta correta:", chute)
            break
        elif chute in palavra_secreta:
            if chute not in letras_acertadas:
                print("Chute esta na palavra")
                acertou_parte_da_palavra = True

                indexes = [i.start() for i in re.finditer(chute, palavra_secreta)]
                for i in indexes:
                    letras_acertadas[i] = chute
                print(letras_acertadas)

                if palavra_secreta == "".join(letras_acertadas):
                    print("Parabens! Voce ganhou:", letras_acertadas)
                    break
            else:
                print("Ja chutou isso. Tente outra palavra")


    print("Fim do jogo")


def choose_word():
    file = open("palavras.txt", 'r')
    words = [line.strip() for line in file]
    file.close()
    return random.choice(words)

if __name__ == "__main__":
    jogar()
