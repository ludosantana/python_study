from random import shuffle, randint
from cores import cor

cores = []
#esse for pega os itens do dicionario COR e coloca na lista CORES, em forma de tupla
for c, v in cor.items():
    cores.append(v)

print("Digite os nomes dos alunos para sortear a ordem de apresentação:")

qtd_nomes = int(input("Quantos nomes? ")) #define quantos nomes serão adicionados
lista = []

for c in range(qtd_nomes):
    lista.append(input("Nome: "))#adiciona nomes à lista

shuffle(lista) #o shuffle() precisa estar numa linha só dele, também não pode colocar em variável, dá erro.

print("A ordem de apresentação será:")

for c in range(qtd_nomes):
    print(f"{c+1:2}º == {cores[randint(0, 7)]}{lista[c]}{cores[8]}")
