#minha solução
'''
import math

catOposto = float(input("Informe o valor do Cateto Oposto: "))
catAdjacente = float(input("Informe o valor do Cateto Adjacente: "))

print("O comprimento da hipotenusa é: {:.2f}".format(math.hypot(catOposto, catAdjacente)))
'''

#guanabara

co = float(input("Informe o valor do Cateto Oposto: "))
ca = float(input("Informe o valor do Cateto Adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print("O valor da hipotenusa é: {:.2f}".format(hi))
