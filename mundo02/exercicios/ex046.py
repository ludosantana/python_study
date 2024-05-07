from time import sleep
from emoji import emojize

i = 0
val_i = None
boom = emojize(":fire:")

def perg():
    if i == 0:
        ver(input("Digite o valor inicial: ").strip())
    else:
        ver(input("Digite o valor final: ").strip())

def ver(n):
    if n.replace(".", "").isdigit():
        if "." in n:
            n = int(float(n)) #se o valor tiver "." transformo ele num float depois em int
            att(n)
        else:
            n = int(n)
            att(n)
    else:
        print(f"{'Digite um valor numérico válido.':^50}")
        perg()

def att(n):
    global i, val_i, val_f
    if i == 0:
        i += 1
        val_i = n
        perg()
    else:
        cont(n)

def cont(f):
    global i, val_i
    if val_i <= f:
        print(f"{'O valor inicial precisa ser maior que o valor final.':^50}\n{'Digite novamente.'.upper():^50}")
        i = 0
        val_i = None
        perg()
    else:
        print(f"{'Contagem regressiva!'.upper():^50}")
        for c in range(val_i, f-1, -1):
            print(f"{c:^50}")
            sleep(1)
        print(f"{' É teetraaa! '.upper():{boom}^50}")

perg()