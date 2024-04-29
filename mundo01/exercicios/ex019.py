#minha solução
'''
from random import choice

n1 = input("Nome um: ")
n2 = input("Nome dois: ")
n3 = input("Nome três: ")
n4 = input("Nome quartro: ")

print("O escolhido para limpar o quadro é: {}".format(choice([n1, n2, n3, n4])))
'''

#guanabara
import random

n1 = str(input("Primeiro nome: "))
n2 = str(input("Segundo nome: "))
n3 = str(input("Terceiro nome: "))
n4 = str(input("Quarto nome: "))
lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista)
print("O aluno escolhido foi: {} {} {}".format("\033[7;35m", random.choice(lista), "\033[m"))