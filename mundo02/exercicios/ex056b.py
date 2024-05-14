somaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0

for p in range(1, 5):
    print(f"----- {p}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if idade > maioridadehomem and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.")
print(f"{totmulher20} mulheres tem menos de 20 anos.")
