def verifica_entrada():
    entrada = input("Digite um número inteiro: ").strip()
    if entrada.isdigit():
        entrada = int(entrada)
        return entrada
    else:
        print("Digite um número \033[1;36mINTEIRO\033[m válido.")
        return verifica_entrada()

entrada = verifica_entrada()

print("Escolha a base de conversão:\n\033[7;32m1-Binário\033[m | \033[7;33m2-Octal\033[m | \033[7;34m3-Hexadecimal\033[m")

escolha = int(input("Qual opção você deseja? "))

def opcoes():
    global escolha
    if escolha == 1:
        print(f"O número \033[1;35m{entrada}\033[m em binário é: \033[1;32m{bin(entrada)}\033[m.")
    elif escolha == 2:
        print(f"O número \033[1;35m{entrada}\033[m em octal é: \033[1;33m{oct(entrada)}\033[m.")
    elif escolha == 3:
        print(f"O número \033[1;35m{entrada}\033[m em hexadecimal é: \033[1;34m{hex(entrada)}\033[m.")
    else:
        print("Digite uma das opções solicitadas.")
        escolha = int(input("Qual opção você deseja? "))
        opcoes()
opcoes()
