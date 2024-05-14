from cores import cor
r = 0
l = int(input("Digite um limite para a soma: "))
i = 0

for c in range(3, l+1, 6):
    r += c
    i += 1
"""
for c in range(1, l, 2):
    if c % 3 == 0:
        r += c
        i += 1
"""

titulo = f"A soma entre os {i} números ímpares, múltiplos de três, entre 1 e {l} é:"

print(f"{titulo}\n\033[1;7;33m {r:^{len(titulo)}} \033[m")
