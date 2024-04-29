from math import floor
from emoji import emojize
from cores import cor

number = float(input("Digite um número decimal: "))

print(emojize(f"O número {cor["amarelo"]}{number:.2f}{cor["fecha"]} tem a parte inteira {cor["azul"]}{floor(number)}{cor["fecha"]} {"\033[44m"} :thumbs_up: {cor["fecha"]}", language='alias'))
