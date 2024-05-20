from random import randint

def valida():#valida se a entrada do user é um num válido
    while True:
        n = input("Adivinhe um número de 0 a 10: ").strip()
        if n.replace(".", "").isdigit():
            if "." in n:
                print("Digite um número inteiro.")
            else:
                return int(n) #return para o loop
        else:
            print("Digite um número válido.")

def verifica():
    c = 0 #contador de tentativas
    na = 0
    nu = -1
    while na != nu:
        na = randint(0, 10) #gera um num ale a cada tentativa
        nu = valida()
        print(f"O número pensado foi: \033[1;35m{na}\033[m e você escolheu: \033[1;32m{nu}\033[m")
        c += 1
    print(f"""
        Parabéns! Você acertou!
        O número pensado foi: {na}
        Você escolheu o número: {nu}
        Você tentou {c} vezes até acertar!
    """)

verifica()
