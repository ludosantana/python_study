"""
calc = (5 + 3) * 2

if calc == 11:
    print('O Resultado do cálculo é {}'.format(calc))
else:
    print('O Resultado não é 11, é {}'.format(calc))

calc2 = 3 * 5 + 4 ** 2

print(calc2)

nome = input('Qual é seu nome? ')
#adicionando 20 espaços
print('Prazer em te conhecer {:20}!'.format(nome))

#adicionando 20 espaços antes
print('Prazer em te conhecer {:>20}!'.format(nome))

#adicionando 20 espaços e centralizando a entrada
print('Prazer em te conhecer {:^20}!'.format(nome))

#adicionando 20 espaços, centralizando e adicionando caracteres nos espaços
print('Prazer em te conhecer {:=^20}!'.format(nome))

"""
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}.'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
