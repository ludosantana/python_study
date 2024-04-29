n1 = int(input("Número 01: "))
n2 = int(input("Número 03: "))
n3 = int(input("Número 04: "))

#solucao do guanabara
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O menor valor digitado foi \033[1;34m{menor}\033[m.")
print(f"O maior valor digitado foi \033[1;35m{maior}\033[m.")


# MINHA SOLUCAO
# print(f"O maior número é {max(n1, n2, n3)}.\nO menor número é {min(n1, n2, n3)}.")