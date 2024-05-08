import pygame
from random import randint

#iniciando o pygame, para reproduzir o som
pygame.init()

#sons
def sound_start():
    pygame.mixer.music.load("processing-02.wav")
    pygame.mixer.music.play()
    pygame.time.wait(3000)
def sound_nope():
    pygame.mixer.music.load("nope.wav")
    pygame.mixer.music.play()
    pygame.time.wait(500)
def sound_success():
    pygame.mixer.music.load("applause.wav")
    pygame.mixer.music.play()
    pygame.time.wait(5000)
def sound_fail():
    pygame.mixer.music.load("fail.wav")
    pygame.mixer.music.play()
    pygame.time.wait(1000)

i = 0 #contador global

#Gerando numero aleatorio
def gera_num():
    return randint(0, 5)

#JOGO
def jogo():
    global i
    #atribuindo a variavel com o numero aleatorio
    n_ale = gera_num()

    #recebe entrada do usuario
    user_entry = input("Digite um número de 0 a 5: ").strip()

    if user_entry.isdigit():
        n_user = int(user_entry)
        if 0 <= n_user <= 5:
            verifica(n_ale, n_user)
        else:
            i += 1
            print("Digite um número INTEIRO entre 0 e 5.")
            sound_nope()
            jogo()
    else:
        i += 1
        print("Letras, espaços e decimais não valem.")
        sound_nope()
        jogo()

#verifica se os numeros sao iguais
def verifica(n_ale, n_user):
    global i

    if n_ale == n_user and i == 0:
        print("Parabéns, você acertou de primeira! O número pensado foi \033[1;32m{}\033[m.".format(n_ale))
        sound_success()
    elif n_ale == n_user and i == 1:
        print("Parabéns, você acertou o número \033[1;34m{}\033[m depois de errar \033[1;32m{}\033[m vez.".format(n_ale, i))
        sound_success()
    elif n_ale == n_user and i > 1:
        print("Parabéns, você acertou o número \033[1;34m{}\033[m depois de errar \033[1;32m{}\033[m vezes.".format(n_ale, i))
        sound_success()
    else:
        i += 1
        print("Que pena, você errou! O número pensado foi \033[1;31m{}\033[m. Tente novamente.".format(n_ale))
        sound_fail()
        jogo()

#Titulo e divisórias
title = ("=" * 20) + " \033[1;30;42mJOGO DA ADIVINHAÇÃO\033[m " + ("=" * 20)
print(title)
print("-" * len(title))
print("Gerando um número aleatório...")
print("-" * len(title))
sound_start()

jogo()
