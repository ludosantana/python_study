mult = fat = valor = int(input("Digite um valor numérico: "))
sequencia = []

while mult > 1:
    mult -= 1
    fat *= mult
    sequencia.append(str(mult))

print(f"\033[1;34m{valor}!\033[m = {valor}x{"x".join(sequencia)} = \033[1;33m{fat}\033[m.")
