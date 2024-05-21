def verifica_num(mensagem): #funcao que verifica numero, recebe a str para add na pergunta
    while True:
        n = input(mensagem).strip()
        if n.replace(".", "").isdigit():
            if "." in n:
                return round(float(n), 2)
            else:
                return int(n)
        else:
            print("\033[1;31mDigite um número válido.\033[m")

def opcao_menu(): #funcao que verifica numero, recebe a str para add na pergunta
    while True:
        n = input("Escolha a opção: ").strip()
        if n.isdigit():
            return int(n)
        else:
            print("\033[1;31mDigite um número válido.\033[m")

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

        while True:
            menu()
            opcao = opcao_menu()

            if opcao == 1:
                print(f"{v_um} + {v_dois} = {v_um + v_dois}")
            elif opcao == 2:
                print(f"{v_um} x {v_dois} = {v_um * v_dois}")
            elif opcao == 3:
                if v_um > v_dois:
                    print(f"{v_um} é maior que {v_dois}.")
                elif v_um < v_dois:
                    print(f"{v_dois} é maior que {v_um}.")
                else:
                    print("Os valores são iguais.")
            elif opcao == 4:
                break #o break encerra esse while e volta para o primeiro
            elif opcao == 5:
                print(f"{'Você escolheu sair.'.upper():^85}")
                print(f"\033[7;33m {'Obrigado por utilizar o programa.'.upper():^85} \033[m")
                return #o return faz com que o primeiro while se encerre também

print(f"\033[1;7;33m {'Lista de operações'.upper():^85} \033[m")
operacao()
