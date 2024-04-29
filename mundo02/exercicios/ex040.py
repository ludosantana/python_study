i = 0 #variavel global para identificar qual pergunta fazer
n1 = None #variavel global que recebe o n1 atualizado.
def question():
    if i == 0:
        verifica(input("Digite a primeira nota: ").strip())
    elif i == 1:
        verifica(input("Digite a segunda nota: ").strip())

def verifica(n):
    if n.replace(".", "").isdigit():
        notas(float(n))
    else:
        print("Digite um número corretamente.")
        question()

def notas(n):
    global i, n1
    if i == 0:
        n1 = n
        i += 1
        question()
    elif i == 1:
        media(n)

def media(n2):
    media = (n1 + n2) / 2
    if media >= 7:
        print(f"\033[7;32m Parabéns, aprovado! \033[m\nSua média foi \033[1;32m{media:.2f}\033[m, muito bem!")
    elif 5 <= media < 7:
        print(f"\033[7;33m Recuperação! \033[m\nSua média foi \033[1;33m{media:.2f}\033[m.")
    else:
        print(f"\033[7;31m Que pena, reprovado! \033[m\nSua média foi \033[1;31m{media:.2f}\033[m.")

question()
