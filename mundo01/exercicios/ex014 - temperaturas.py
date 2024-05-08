from cores import cor

#function que calcula Celsius para outras medidas
def calcCelsius():
    tempC = float(input('Informe a temperatura em °C: '))
    tempF = tempC * 1.8 + 32
    tempK = tempC + 273.15
    print(f'Celsius = {cor["azul"]}{tempC}°C{cor["fecha"]}\nFahrenheit = {cor["verde"]}{tempF:.2f}°F{cor["fecha"]}\nKelvin = {cor["amarelo"]}{tempK:.2f}°K{cor["fecha"]}')
    continuar()

#function que calcula Fahrenheit para outras medidas
def calcFah():
    tempF = float(input('Informe a temperatura em °F: '))
    tempC = (tempF - 32) / 1.8
    tempK = (tempF - 32) / 1.8 + 273.15 #ou também "tempC + 273.15"
    print(f'Fahrenheit = {cor["azul"]}{tempF}°F{cor["fecha"]}\nCelsius = {cor["verde"]}{tempC:.2f}°C{cor["fecha"]}\nKelvin = {cor["amarelo"]}{tempK:.2f}°K{cor["fecha"]}')
    continuar()

#function que calcula kelvin para outras medidas
def calcKelvin():
    tempK = float(input('Informe a temperatura em °K: '))
    tempC = tempK - 273.15
    tempF = (tempK - 273.15) * 1.8 + 32 #ou também "tempC * 1.8 + 32"
    print(f'Kelvin = {cor["azul"]}{tempK}°K{cor["fecha"]}\nCelsius = {cor["verde"]}{tempC:.2f}°C{cor["fecha"]}\nFahrenheit = {cor["amarelo"]}{tempF:.2f}°F{cor["fecha"]}')
    continuar()

def continuar():
    cont = input('Gostaria de fazer outra conversão?\n[0] - Sim | [1] - Não: ').strip()

    if cont.isdigit():
        cont = int(cont)
        if cont == 0:
            choose()
        elif cont == 1:
            print('\033[7;32m Obrigado por utilizar nosso sistema. \033[m') #FINALIZA O PROGRAMA
        else:
            print("\033[7;33m Digite uma das opções pedidas. \033[m")
            continuar()
    else:
        print("\033[7;33m Digite uma das opções pedidas. \033[m")
        continuar()

def choose():
    escolha = input(f'Digite um dos números para fazer a conversão desejada:\n\033[1m{cor["azul"]}[1] - Celsius | {cor["roxo"]}[2] - Fahrenheit | {cor["amarelo"]}[3] - Kelvin:\033[m ').strip()
    if escolha.isdigit():
        escolha = int(escolha)#precisa converter para int para poder fazer a comparação abaixo
        if escolha == 1:
             calcCelsius()
        elif escolha == 2:
            calcFah()
        elif escolha == 3:
            calcKelvin()
        else:
            print("\033[7;33m Digite um das opções pedidas. \033[m")
            choose()
    else:
        print("\033[7;33m Digite uma das opções pedidas. \033[m")
        choose()

choose()