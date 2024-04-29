real = float(input('Quantos reais você tem na carteira? R$ '))
dolar = 3.27
calc = real / dolar

if calc >= 1.0:
    print('Você pode comprar \033[7;30;42m US$ {:.2f} \033[m'.format(calc))
else:
     print('\033[7;30;41m Você não tem dinheiro o suficiente para comprar dólar. \033[m')
