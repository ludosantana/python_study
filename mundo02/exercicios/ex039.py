from datetime import datetime
from cores import cor

def question():
    ano = input("Em que ano você nasceu? ").strip()
    verify_entry(ano)

def verify_entry(i):
    if i.isdigit():
        i = int(i)
        alista(i)
    else:
        print("Digite um número válido.")
        question()

def alista(ano):
    idade = datetime.now().year - ano
    if idade == 18:
        print(f"Você nasceu em {cor["azul"]}{ano}{cor["fecha"]}, logo você tem {cor["amarelo"]}{idade}{cor["fecha"]} anos. É hora de se alistar no serviço militar.")
    elif idade < 18:
        print(f"Você tem {cor["amarelo"]}{idade}{cor["fecha"]} anos, ainda faltam {cor["verde"]}{18 - idade}{cor["fecha"]} anos para se alistar.")
    elif idade == 19:
        print(f"Você tem {cor["amarelo"]}{idade}{cor["fecha"]} anos. Você está \033[31m1\033[m ano atrasado.")
    else:
        print(f"Você tem {cor["amarelo"]}{idade}{cor["fecha"]} anos. Você está {cor["vermelho"]}{idade - 18}{cor["fecha"]} anos atrasado.")

question()
