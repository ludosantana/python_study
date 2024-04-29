#import math
from math import sqrt, ceil
import emoji
from random import random, randint

n1 = randint(1, 100)
raiz = sqrt(n1)

print(emoji.emojize("A raíz de {} é : {:.2f} :earth_americas:".format(n1, raiz), language='alias'))
