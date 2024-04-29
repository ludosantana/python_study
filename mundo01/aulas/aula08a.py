""" ============================================================
#importa a biblioteca tinteira:
#import math

#importa partes da biblioteca. Esse método não precisa adicionar math.sqrt(), math.ceil()...
#pode-se utilizar o modulo direto: ceil(), sqrt(), floor()
from math import sqrt, ceil, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
#math.ceil => arredonda para cima
#math.floor => arredonda para baixo
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
=============================================================="""
#import emoji
from emoji import emojize

print(emojize("Olá mundo! :earth_americas:", language='alias'))
