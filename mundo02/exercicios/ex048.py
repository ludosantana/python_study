from cores import cor
r = 0
l = int(input("Digite um limite para a soma: "))

for c in range(1, l, 2):
    if c % 3 == 0:
        r += c

print(f"A soma entre os {cor['azul']}números ímpares{cor['fecha']}, {cor['amarelo']}múltiplos de três{cor['fecha']}, entre 1 e 500 é:\n\033[7;35m {r:^50} \033[m")
