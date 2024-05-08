nome = str(input("Digite seu nome completo: ")).title().strip().split()
#nome = nome.split()

print("Nome completo: \033[4;35m{}\033[m".format(" ".join(nome)))
print("Primeiro nome: \033[1;32m{}\033[m".format(nome[0]))
print("Último nome:   \033[1;33m{}\033[m".format(nome[-1]))
