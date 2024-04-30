from emoji import emojize
from time import sleep
from random import randint

ale = randint(1, 3)

pedra = emojize(":raised_fist:")
papel = emojize(":hand_with_fingers_splayed:")
tesoura = emojize(":victory_hand:")

print("Jo...", end="")
sleep(1)
print("ken...", end="")
sleep(1)
print("pô!")

print(
    "1 |", pedra,"\n"
    "2 |", papel,"\n"
    "3 |", tesoura,
)
user = int(input("Qual opção você escolhe? "))
if user == 1 and ale == 2:
    print(f"Você perdeu! {papel} ganha de {pedra}!")
elif user == 1 and ale == 3:
    print(f"Você ganhou! {pedra} ganha de {tesoura}!")
elif user == 2 and ale == 1:
    print(f"Você ganhou! {papel} ganha de {pedra}!")
elif user == 2 and ale == 3:
    print(f"Você perdeu! {tesoura} ganha de {papel}!")
elif user == 3 and ale == 1:
    print(f"Você perdeu! {pedra} ganha de {tesoura}!")
elif user == 3 and ale == 2:
    print(f"Você ganhou! {tesoura} ganha de {papel}!")
elif user == ale:
    print("Empatou! Jogue de novo.")
