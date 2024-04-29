from cores import cor
from datetime import datetime

i = 0 #variavel global para contar as entradas erradas

#função que pergunta ao usuario
def question():
    if i < 5:
        verifica_entrada(input("Em que ano você nasceu? ").strip()) #envia resposta para funcao verifica_entrada()
    else:
        verifica_entrada(input("Pare de brincadeira e digite um valor correto: ").strip()) #envia resposta para funcao verifica_entrada()

#funcao que verifica se a entrada é um digito e o converte em INT
def verifica_entrada(x):
    global i
    if x.isdigit():
        x = int(x)
        calc_idade(x) #quando convertido em INT, envia o valor para a funcao calc_idade()
    else:
        i += 1
        print("Digite um valor correto.")
        question()

def calc_idade(x):
    ano_user = x
    ano_atual = datetime.now().year
    res = ano_atual - ano_user
    if res <= 9:
        print(f"Você tem {cor["verde"]}{res}{cor["fecha"]} anos. Sua categoria é {cor["azul"]}MIRIM{cor["fecha"]}.")
    elif 10 <= res <= 14:
        print(f"Você tem {cor["verde"]}{res}{cor["fecha"]} anos. Sua categoria é {cor["azul"]}INFANTIL{cor["fecha"]}.")
    elif 15 <= res <= 19:
        print(f"Você tem {cor["verde"]}{res}{cor["fecha"]} anos. Sua categoria é {cor["azul"]}JÚNIOR{cor["fecha"]}.")
    elif res == 20:
        print(f"Você tem {cor["verde"]}{res}{cor["fecha"]} anos. Sua categoria é {cor["azul"]}SÊNIOR{cor["fecha"]}.")
    else:
        print(f"Você tem {cor["verde"]}{res}{cor["fecha"]} anos. Sua categoria é {cor["azul"]}MASTER{cor["fecha"]}.")

question()
