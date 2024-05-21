condicao = 0

while condicao == 0:
    numero_um = float(input("Digite o primeiro número: "))
    numero_dois = float(input("Digite o segundo número: "))

    print("[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do programa")
    opcao = int(input("Escolha qual operação deseja fazer: "))

    if opcao == 1:
        print(f"{numero_um} + {numero_dois} = {numero_um + numero_dois}")
        condicao = 1
    elif opcao == 2:
        print(f"{numero_um} x {numero_dois} = {numero_um * numero_dois}")
        condicao = 1
    elif opcao == 3:
        if numero_um > numero_dois:
            print(f"{numero_um} é maior que {numero_dois}")
        else:
            print(f"{numero_dois} é maior que {numero_um}")
        condicao = 1
    elif opcao == 5:
        condicao = 1
