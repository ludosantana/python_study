def valida(mensagem):
    while True:
        n = input(mensagem).strip()
        if n.replace(".", "").isdigit():
            if "." in n:
                return round(float(n), 2)
            else:
                return int(n)
        else:
            print("Digite um valor numérico.")

def valida_int(mensagem):
    while True:
        n = input(mensagem).strip()
        if n.replace(".", "").isdigit():
            return int(n)
        else:
            print("Digite um valor numérico.")

while True:
    pt = valida("Digite o primeiro termo: ")
    r = valida("Digite a razão: ")
    c = 0
    limite = 10
    while c < limite:
        c += 1
        print(f"{pt} →", end=" ")
        pt += r
    print("Acabou!")

    limite += valida_int("Gostaria de mais quantos termos? ")

    if limite > 0:
        c = 0 #reseta o contador
        pt -= 10 #reseta o valor do primeiro termo
        while c < limite:
            c += 1
            print(f"{pt} →", end=" ")
            pt += r
        print("Acabou!")

    break
