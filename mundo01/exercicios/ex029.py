multa = 7.0
limite = 80
def recebe_vel():
    vel = input("Qual a velocidade do carro (em Km)? ").strip()
    if vel.isdigit():
        vel = int(vel)
        if vel > limite:
            print(f"\033[7;31m Você está acima do permitido! \033[m\nVelocidade permitida: \033[1;32m{limite}Km/h\033[m.\nSua velocidade: \033[1;33m{vel}Km/h\033[m.\nVocê será multado em \033[1;31m R$ {(vel - limite) * multa:.2f}\033[m.")
        elif vel == limite:
            print(f"Você está a \033[7;33m {vel}Km/h \033[m. No limite, cuidado para não ser multado.")
        else:
            print(f"Está a \033[1;32m{vel}Km/h\033[m, abaixo de \033[1;31m{limite}Km/h\033[m. Pode seguir.")
    else:
        print("Digite um número inteiro.")
        recebe_vel()

recebe_vel()