n = 0

def ver(i): #verifica a entrada do usuário e atualiza a variavel n
    global n
    if i.replace(".", "").isdigit():
        if "." in i:
            n = int(float(i))
        else:
            n = int(i)
    else:
        print("Digite um valor numérico corretamente.")
        ver(input("Digite um número: ").strip())

print("Vamos montar uma TABUADA?")

ver(input("Digite um número: ").strip())

for c in range(0, 11): #conta de 0 a 11 e monta a tabuada
    print(f"{n} x {c} = {c * n}")
