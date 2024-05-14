numero = 0
total = 0

def pergunta():
    while True:
        if verifica(input("Digite um número inteiro: ").strip()):
            break

def verifica(n):
    global numero
    if n.replace(".", "").isdigit():
        if "." in n:
            print("Não é permitido decimais.")
            return False
        else:
            numero = int(n)
            return True
    else:
        print("Digite um número corretamente.")
        return False

pergunta() #chamo a func pergunta

for c in range(1, numero + 1):
    if numero % c == 0:
        print("\033[33m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print(f"{c} \033[m", end=" ")

if total == 2:
    print(f"\n{numero} é número primo.")
else:
    print(f"\n{numero} não é número primo.")
