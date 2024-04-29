from cores import cor

n = input('Digite um número: ')
if n.isnumeric():
    n1 = int(n) - 1
    n2 = int(n) + 1
    print(f'O número anterior ao {cor["azul"]}{n}{cor["fecha"]} é {cor["verde"]}{n1}{cor["fecha"]}, e o próximo é {cor["verde"]}{n2}{cor["fecha"]}.')
elif n.isalpha():
    print(f'{cor["vermelho"]}Você não digitou um número.{cor["fecha"]}')
elif n.isalnum():
    print(f'{cor["roxo"]}Você digitou algum outro caractere junto ao número.{cor["fecha"]}')
