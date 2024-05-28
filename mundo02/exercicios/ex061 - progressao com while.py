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

while True:
    pt = valida("Digite o primeiro termo: ")
    r = valida("Digite a razão: ")
    c = 0
    while c < 10:
        c += 1
        print(f"{pt} →", end=" ")
        pt += r
    print("Acabou!")
    break
