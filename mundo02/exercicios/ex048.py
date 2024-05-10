from cores import cor
r = 0
l = int(input("Digite um limite para a soma: "))

for c in range(1, l, 2):
    if c % 3 == 0:
        r += c

titulo = "A soma entre os números ímpares, múltiplos de três, entre 1 e 500 é:"

print(f"{titulo}\n\033[1;7;33m {r:^{len(titulo)}} \033[m")
