from cores import cor

print(f"\033[7;36m {'Oferta de Consoles'.upper():^60} \033[m")
print(f"\033[7;37m {'':-^60} \033[m")
print(f"\033[7;32m {'Escolha um produto'.upper():^60} \033[m")

print(f"\033[7;34m 1 \033[m{cor["azul"]} PLAYSTATION 5: R$ 3.200{cor["fecha"]}\n\033[7;32m 2 \033[m{cor["verde"]} XBOX SERIES X: R$ 2.950{cor["fecha"]}\n\033[7;31m 3 \033[m{cor["vermelho"]} NINTENDO SWITCH: R$ 2.300{cor["fecha"]}")

play = 3200
xbox = 2950
nintendo = 2300

def escolha_con():
    escolha = int(input("Qual console gostaria de comprar? "))
    if escolha == 1:
        print(f"\033[7m {'Você escolheu o '.upper() + cor["azul"] + ' Playstation 5'.upper():^65} \033[m")
        pagamento(play)
    elif escolha == 2:
        print(f"\033[7m {'Você escolheu o '.upper() + cor["verde"] + ' Xbox Series X'.upper():^65} \033[m")
        pagamento(xbox)
    elif escolha == 3:
        print(f"\033[7m {'Você escolheu o '.upper() + cor["vermelho"] + ' Nintendo Switch'.upper():^65} \033[m")
        pagamento(nintendo)
    else:
        print("Digite uma das opções válidas")
        return escolha_con()

def pagamento(x):
    print(f"\033[7;35m {'Escolha uma condição de pagamento.'.upper():^60} \033[m\n\033[7;32m 1 \033[m Dinheiro 10% OFF\n\033[7;33m 2 \033[m Débito à vista 5% OFF\n\033[7;32m 3 \033[m 2x no cartão.\n\033[7;33m 4 \033[m 3x ou mais 20% juros.")
    escolha = int(input("Qual o método de pagamento? "))

    if escolha == 1:
        print(f"No dinheiro à vista você paga: {cor["amarelo"]}R$ {(x - (x * 10 / 100)):.2f}{cor["fecha"]}")
    elif escolha == 2:
        print(f"No débito à vista você paga: {cor["amarelo"]}R$ {(x - (x * 5 / 100)):.2f}{cor["fecha"]}")
    elif escolha == 3:
        print(f"Parcelando em 2x no crédito, você paga: {cor["amarelo"]}R$ {x}{cor["fecha"]}. {cor["amarelo"]}R$ {(x / 2):.2f}{cor["fecha"]} cada prestação.")
    elif escolha == 4:
        parcelas = int(input("Em quantas vezes? "))
        print(f"Você paga {parcelas}x de {cor["amarelo"]}R$ {((x + (x * 20 / 100)) / parcelas):.2f}{cor["fecha"]}, num total de: {cor["amarelo"]}R$ {(x + (x * 20 / 100)):.2f}{cor["fecha"]}{cor["fecha"]}.")


escolha_con()