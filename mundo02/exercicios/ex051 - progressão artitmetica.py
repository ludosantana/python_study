i = 0
pt = 0
r = 0
pa = []


def pergunta():
    if i == 0:
        verifica(input("Digite o primeiro termo: ").strip())
    else:
        verifica(input("Digite a razão: ").strip())


def verifica(n):
    if n.replace(".", "").isdigit():
        if "." in n:
            atribui_valor(float(n))
        else:
            atribui_valor(int(n))
    else:
        print("Letra não é válida. Digite novamente.")
        pergunta()


def atribui_valor(n):
    global i, pt, r
    if i == 0:
        pt = n
        i += 1
        pergunta()
    else:
        r = n


pergunta()

for c in range(10):
    pa.append(str(round(pt, 1)))#transformo em str para armazenar na lista, pois o .join() só funciona com str
    pt += r

print(f"Primeiro Termo: {pa[0]}\nRazão: {r}\nPA = ({', '.join(pa)})")
