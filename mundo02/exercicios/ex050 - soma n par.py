def pergunta():
    for c in range(6):
        while True: #Se o result. do user for True, termina o While e avança para a prox. etapa do For.
            if verifica(input("Digite um número: ").strip()):
                break

numeros = []
numero = 0
def verifica(n):
    global numero
    if n.replace(".", "").isdigit():
        if "." in n:
            print("Digite um número inteiro.")
            return False
        else:
            if int(n) % 2 == 0:
                numeros.append(n)
                numero += int(n)
            return True
    else:
        print("Não pode digitar letras.")
        return False

pergunta()

if numero == 0:
    print("Você digitou apenas números ímpares ou 0. Então não houve soma.")
elif len(numeros) == 1:
    print(f"Só há um número par: \033[4;35m{numero}\033[m")
else:
    print(f"A soma dos números: {" + ".join(numeros)} = \033[1;32m{numero}\033[m")