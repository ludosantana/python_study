from cores import cor

nFloat = float(input('Digite um número: '))
n = int(nFloat)
i = 0
print('-' * 15)

# minha solução com while (aqui precisa definir a variavel de i antes.)
while i <= 10:
    r = i * n
    print(f'{cor["roxo"]}{i:2}{cor["fecha"]} x {cor["roxo"]}{n:2}{cor["fecha"]} = {cor["verde"]}{r}{cor["fecha"]}')
    i += 1

"""Outra solução com for, onde os parametros do range são primeiro o valor do i e o segundo a quantidade.
Dessa maneira não precisa de variavel para o i.

for i in range(0, 11):
   print('{:<3} x {:>2} = {}'.format(i, n, i * n))
"""
print('-' * 15)
