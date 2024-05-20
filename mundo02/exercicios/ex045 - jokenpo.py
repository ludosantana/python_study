from emoji import emojize
from time import sleep
from random import randint

esc = {
    1: emojize(":raised_fist:"),#pedra
    2: emojize(":hand_with_fingers_splayed:"),#papel
    3: emojize(":victory_hand:")#tesoura
}

i = 0

def jogo():
    global i
    print("1:", esc[1], "| 2:", esc[2], "| 3:", esc[3], )
    ale = randint(1, 3)
    user = int(input("Qual opção você escolhe? "))

    if user < 1 or user > 3: #verifica se o usuario está digitando o intervalo correto
        print("Escolha um valor correto! 1, 2 ou 3.")
        jogo()
    else:
        print("Jo...", end="")
        sleep(1)
        print("ken...", end="")
        sleep(1)
        print("pô!")
        sleep(0.5)

        if ale == user: #condição de empate
            i += 1
            print(f"PLAYER -> {esc[user]} VS {esc[ale]} <- COMPUTADOR")
            print("\033[7;34m Empatou! \033[m Jogue de novo.")
            jogo()
        elif (ale == 1 and user == 3) or (ale == 2 and user == 1) or (ale == 3 and user == 2): #condição de derrota
            print(f"PLAYER -> {esc[user]} VS {esc[ale]} <- COMPUTADOR")
            print(f"\033[7;31m Você perdeu! \033[m {esc[ale]} ganha de {esc[user]}!")
            if i > 0:
                print(f"{i} empate(s) até sua derrota.")
        else:
            print(f"PLAYER -> {esc[user]} VS {esc[ale]} <- COMPUTADOR") #condição de vitória
            print(f"\033[7;32m Você Ganhou! \033[m {esc[user]} ganha de {esc[ale]}!")
            if i > 0:
                print(f"{i} empate(s) até sua vitória")

jogo()