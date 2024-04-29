i = 0
l1 = None
l2 = None
l3 = None

def pergunta():
    if i == 0:
        verifica(input("Medida do lado 01: ").strip())
    elif i == 1:
        verifica(input("Medida do lado 02: ").strip())
    elif i == 2:
        verifica(input("Medida do lado 03: ").strip())

def verifica(n):
    if n.replace(".", "").isdigit():
        atribui_valor(float(n))
    else:
        print("Letras não são permitidas.")
        pergunta()

def atribui_valor(n):
    #após o valor verificado, aqui atribui para as variaveis globais
    global i, l1, l2, l3

    if i == 0:
        i += 1
        l1 = n
        pergunta()
    elif i == 1:
        i += 1
        l2 = n
        pergunta()
    elif i == 2:
        l3 = n
        calculo_tri()

def calculo_tri():
    global i, l1, l2, l3
    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2: #se tiver as condições para existir um triangulo

        if l1 == l2 == l3:
            print(f"{l1}, {l2}, {l3}. Todas as medidas são iguais! Este é um triângulo \033[1;32mEquilátero\033[m.")
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print(f"{l1}, {l2}, {l3}. Duas das medidas são iguais! Este é um triângulo \033[1;33mIsósceles\033[m.")
        else:
            print(f"{l1}, {l2}, {l3}. Todas as medidas são diferentes! Este é um triângulo \033[1;34mEscaleno\033[m.")

    else:
        #reseta as variáveis globais e pergunta as medidas novamente.
        i = 0
        l1 = None
        l2 = None
        l3 = None
        print("Não é possível criar um Triângulo com essas medidas. Tente novamente.")
        pergunta()

pergunta()
