dias = 60 * int(input('Quantos dias alugados? '))
km = 0.15 * float(input('E quantos quilômetros percorridos? '))

print('O serviço todo ficou em {} R$ {:.2f} {} a pagar.'.format("\033[1;30;45m", km + dias, "\033[m"))
