num = int(input("Digite um número de 0 a 9999: "))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Você digitou o número: \033[1;31m{}\033[m".format(num))
print("Unidade: \033[1;36m{}\033[m".format(u))
print("Dezena:  \033[1;36m{}\033[m".format(d))
print("Centena: \033[1;36m{}\033[m".format(c))
print("Milhar:  \033[1;36m{}\033[m".format(m))
