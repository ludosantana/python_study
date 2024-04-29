n1 = float(input('Digite a nota da prova: '))
n2 = float(input('Digite a nota do caderno: '))
media = (n1 + n2) / 2

if media == 10:
    print('A média é {}{:.2f}{}. Nota máxima!'.format("\033[1;32m", media, "\033[m"))
elif 5 <= media <= 9:
    print('A média é {}{:.2}{}. Passou de ano.'.format("\033[1;33m", media, "\033[m"))
else:
    print('A média é {}{:.2}{}. Reprovou!'.format("\033[1;31m", media, "\033[m"))
