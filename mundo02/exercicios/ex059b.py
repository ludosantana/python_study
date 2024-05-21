def verifica_num(m): #funcao que verifica numero, recebe a str para add na pergunta
    while True:
        n = input(m).strip()
        if n.replace(".", "").isdigit():
            if "." in n:
                return round(float(n), 2)
            else:
                return int(n)
        else:
            print("\033[1;31mDigite um número válido.\033[m")
            operacao()
            break

def soma(v_um, v_dois):
    return v_um + v_dois

def mult(v_um, v_dois):
    return v_um * v_dois

def menu():
    print(f"\033[7;32m {'Escolha uma opção:'.upper():^85} \033[m")
    print(f"{'\033[7;34m'} {'[1] - somar'.upper()} \033[m", end="")
    print(f"{'\033[7;35m'} {'[2] - multiplicar'.upper()} ", end="")
    print(f"{'\033[7;34m'} {'[3] - maior ou menor'.upper()} ", end="")
    print(f"{'\033[7;35m'} {'[4] - novos números'.upper()} ", end="")
    print(f"{'\033[7;31m'} {'[5] - sair'.upper()} \033[m")

def operacao():
    while True:
        v_um = verifica_num("Digite o primeiro número: ")#envia a mensagem para a fun verifica e recebe seu valor, guardando na variavel
        v_dois = verifica_num("Digite o segundo número: ")
        menu()
        opcao = verifica_num("Escolha a opção: ")

        if opcao == 1:
            return print(f"{v_um} + {v_dois} = {soma(v_um, v_dois)}")
        elif opcao == 2:
            return print(f"{v_um} x {v_dois} = {mult(v_um, v_dois)}")
        elif opcao == 3:
            return print(f"{max(v_um, v_dois)} é maior que {min(v_um, v_dois)}")
        elif opcao == 4:
            return operacao()
        else:
            print(f"{'Você escolheu sair.'.upper():^85}")
            print(f"\033[7;33m {'Obrigado por utilizar o programa.'.upper():^85} \033[m")
            break

print(f"\033[1;7;33m {'Lista de operações'.upper():^85} \033[m")
operacao()