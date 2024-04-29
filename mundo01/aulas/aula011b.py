from random import randint

nome = input("Qual o seu nome? ")
cores = { #isso é um dicionário
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "fecha": "\033[m"
}
cores_lista = [ #isso é uma lista
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
    "\033[m"
]
aleatorio = randint(0, 5)

#print usando itens do dicionário
print(f"Olá! Muito prazer em te conhecer, {cores["vermelho"]}{nome}{cores["fecha"]}!!")

#print usando itens da lista - gerados aleatoriamente
print(f"Olá! Muito prazer em te conhecer, {cores_lista[aleatorio]}{nome}{cores_lista[6]}!!")
