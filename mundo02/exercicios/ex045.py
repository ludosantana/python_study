from emoji import emojize
from time import sleep
from random import randint

pedra = emojize(":raised_fist:")
papel = emojize(":hand_with_fingers_splayed:")
tesoura = emojize(":victory_hand:")

def jogo():
    print("Jo...", end="")
    sleep(1)
    print("ken...", end="")
    sleep(1)
    print("pô!")
    sleep(0.2)

    print("1:", pedra, "| 2:", papel, "| 3:", tesoura,)
    ale = randint(1, 3)
    user = int(input("Qual opção você escolhe? "))

    if user == 1 and ale == 2:
        print(f"PLAYER -> {pedra} vs {papel} <- COMPUTADOR")
        print(f"\033[7;31m Você perdeu! \033[m {papel} ganha de {pedra}!")
    elif user == 1 and ale == 3:
        print(f"PLAYER -> {pedra} vs {tesoura} <- COMPUTADOR")
        print(f"\033[7;32m Você ganhou! \033[m {pedra} ganha de {tesoura}!")
    elif user == 2 and ale == 1:
        print(f"PLAYER -> {papel} vs {pedra} <- COMPUTADOR")
        print(f"\033[7;32m Você ganhou! \033[m {papel} ganha de {pedra}!")
    elif user == 2 and ale == 3:
        print(f"PLAYER -> {papel} vs {tesoura} <- COMPUTADOR")
        print(f"\033[7;31m Você perdeu! \033[m {tesoura} ganha de {papel}!")
    elif user == 3 and ale == 1:
        print(f"PLAYER -> {tesoura} vs {pedra} <- COMPUTADOR")
        print(f"\033[7;31m Você perdeu! \033[m {pedra} ganha de {tesoura}!")
    elif user == 3 and ale == 2:
        print(f"PLAYER -> {tesoura} vs {papel} <- COMPUTADOR")
        print(f"\033[7;32m Você ganhou! \033[m {tesoura} ganha de {papel}!")
    elif user == 1 and ale == 1:
        print(f"PLAYER -> {pedra} vs {pedra} <- COMPUTADOR")
        print("\033[7;34m Empatou! \033[m Jogue de novo.")
        jogo()
    elif user == 2 and ale == 2:
        print(f"PLAYER -> {papel} vs {papel} <- COMPUTADOR")
        print("\033[7;34m Empatou! \033[m Jogue de novo.")
        jogo()
    elif user == 3 and ale == 3:
        print(f"PLAYER -> {tesoura} vs {tesoura} <- COMPUTADOR")
        print("\033[7;34m Empatou! \033[m Jogue de novo.")
        jogo()
jogo()