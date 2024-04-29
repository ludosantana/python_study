def start():
    num = input("Digite um número inteiro: ").strip()
    if num.isdigit():
        num = int(num)
        par_impar(num)
    else:
        print("Digite corretamente.")
        start()

def par_impar(num):
    if num % 2 == 0:
        print(f"\033[1;35m{num}\033[m é um número par.")
    else:
        print(f"\033[1;36m{num}\033[m é um número ímpar.")

start()
