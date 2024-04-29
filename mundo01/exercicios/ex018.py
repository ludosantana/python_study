from math import sin, cos, tan, radians
from cores import cor

angle = float(input("Digite o valor de um ângulo: "))

if angle == 90 or angle == -90:
    a90 = "INFINITO"
    c90 = "0"
    print(f"Ângulo: {cor["verde"]}{angle:>10}°{cor["fecha"]}\nSeno: {cor["azul"]}{sin(radians(angle)):>12.2f}{cor["fecha"]}\nCosseno: {"\033[7;35m":>12} {c90} {cor["fecha"]}\nTangente: {"\033[7;35m":>11} {a90} {cor["fecha"]}")
else:
    print(f"Ângulo: {cor["azul"]}{angle:>10}°{cor["fecha"]}\nSeno: {cor["amarelo"]}{sin(radians(angle)):>12.2f}{cor["fecha"]}\nCosseno: {cor["vermelho"]}{cos(radians(angle)):>9.2f}{cor["fecha"]}\nTangente: {cor["verde"]}{tan(radians(angle)):>8.2f}{cor["fecha"]}")
