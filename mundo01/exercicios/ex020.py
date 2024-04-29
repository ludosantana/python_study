from random import shuffle
from cores import cor

print("Digite os nomes dos alunos para sortear a ordem de apresentação:")
n1 = str(input("Nome: "))
n2 = str(input("Nome: "))
n3 = str(input("Nome: "))
n4 = str(input("Nome: "))
lista = [n1, n2, n3, n4]
#o shuffle() precisa estar numa linha só dele, também não pode colocar em variável, dá erro.
shuffle(lista)
print(f"A ordem de apresentação será:\n1º == {cor["verde"]}{lista[0]}{cor["fecha"]}\n2º == {cor["azul"]}{lista[1]}{cor["fecha"]}\n3º == {cor["vermelho"]}{lista[2]}{cor["fecha"]}\n4º == {cor["amarelo"]}{lista[3]}{cor["fecha"]}")
