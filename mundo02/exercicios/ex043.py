from math import ceil
i = 0
p = None

def pergunta():
    if i == 0:
        verifica(input("Qual seu peso? ").strip())
    else:
        verifica(input("Qual sua altura? ").strip())

def verifica(x):
    if x.replace(".", "").isdigit():
        atribui_valor(float(x))
    else:
        print("Digite um valor numérico, corretamente.")
        pergunta()

def atribui_valor(x):
    global i, p
    if i == 0:
        i += 1
        p = x
        pergunta()
    else:
        calc_imc(x)

def calc_imc(a):
    imc = p / a ** 2

    print(f"\033[7;34m Seu IMC é de: \033[m")
    if imc < 18.5:
        print(f"\033[7;31m {imc:.2f} \033[m\033[31m Você está abaixo do peso.\033[m")
        print(f"Você precisa ganhar pelo menos \033[1;32m{ceil((18.5 * a ** 2) - (imc * a ** 2))}Kg\033[m.")
    elif 18.5 <= imc < 25:
        print(f"\033[7;32m {imc:.2f} \033[m\033[32m Você está no peso Ideal.\033[m")
    elif 25 <= imc < 30:
        print(f"\033[7;33m {imc:.2f} \033[m\033[33m Você está com sobrepeso.\033[m")
        print(f"Você precisa perder pelo menos \033[1;32m{ceil((imc * a ** 2) - (24 * a ** 2))}Kg\033[m.")
    elif 30 <= imc <= 40:
        print(f"\033[7;35m {imc:.2f} \033[m\033[35m Você está com obesidade.\033[m")
        print(f"Você precisa perder pelo menos \033[1;32m{ceil((imc * a ** 2) - (29 * a ** 2))}Kg\033[m.")
    else:
        print(f"\033[7;31m {imc:.2f} \033[m\033[31m Cuidado, você tem obesidade Mórbida.\033[m")
        print(f"Você precisa perder pelo menos \033[1;32m{ceil((imc * a ** 2) - (39 * a ** 2))}Kg\033[m.")

pergunta()