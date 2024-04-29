dist = int(input("Qual a distância em Km da viagem? "))

if dist <= 200:
    print(f"A passagem vai custar \033[1;34mR$ {dist * 0.5:.2f}\033[m.")
else:
    print(f"A passagem vai custar \033[1;35mR$ {dist * 0.45:.2f}\033[m.")
