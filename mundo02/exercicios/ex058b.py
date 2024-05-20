from random import randint
contador = 0

def pergunta_num():
    global contador
    while True: #loop infinito
        entrada = input("Digite um número de 0 a 10: ").strip()
        contador += 1
        if entrada.isdigit():
            numero = int(entrada)
            if 0 <= numero <= 10:
                return numero #return para o loop
            else:
                print("Digite um número entre 0 e 10.")
        else:
            print("Digite um número válido.")

def jogo_adivinha():
    numero_ale = randint(0, 10)
    while True:
        numero_user = pergunta_num()
        if numero_user < numero_ale:
            print("Tente um número maior.")
        elif numero_user > numero_ale:
            print("Tente um número menor.")
        else:
            print(f"\033[1;7;32m Parabéns! Você acertou! Número secreto: {numero_ale}. Tentativas: {contador} \033[m")
            break

jogo_adivinha()