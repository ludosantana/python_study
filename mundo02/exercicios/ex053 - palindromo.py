frase = str(input("Digite uma frase: ")).strip()
f = frase.replace(" ", "").upper()

if f == f[::-1]: # ::-1 mostra a str ou itens da lista ao contrario
    print(f"A frase \033[1;32m'{frase}'\033[m é palíndroma!")
else:
    print(f"A frase \033[1;35m'{frase}'\033[m não é palíndroma.")
