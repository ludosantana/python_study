from random import shuffle
from cores import cor

print("Digite os nomes dos alunos para sortear a ordem de apresentação:")

lista = []
for c in range(4):
    lista.append(input("Nome: "))#adiciono os nomes à lista

shuffle(lista) #o shuffle() precisa estar numa linha só dele, também não pode colocar em variável, dá erro.

print(f"A ordem de apresentação será:\n1º == {cor["verde"]}{lista[0]}{cor["fecha"]}\n2º == {cor["azul"]}{lista[1]}{cor["fecha"]}\n3º == {cor["vermelho"]}{lista[2]}{cor["fecha"]}\n4º == {cor["amarelo"]}{lista[3]}{cor["fecha"]}")
