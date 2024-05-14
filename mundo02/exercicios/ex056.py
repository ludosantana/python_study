pessoas = []
media = 0
nome_mais_velho = None
idade_mais_velho = -1
nome_mulheres = []
idade_mulheres = 20
quantia = 4
i = 0

#loop para pegar informações
for c in range(quantia):
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo: ").title().strip()
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

for pessoa in pessoas:
    # calcula a média de idade
    media += pessoa["idade"] / quantia

    # busca os homens e adiciona o mais velho à variavel
    if pessoa["sexo"].find("Masc") == 0 and pessoa["idade"] > idade_mais_velho:
        nome_mais_velho = pessoa["nome"]
        idade_mais_velho = pessoa["idade"]

    # busca as mulheres e adiciona as com menos de 20 anos à variavel
    if pessoa["sexo"].find("Fem") == 0 and pessoa["idade"] < idade_mulheres:
        nome_mulheres.append({"nome": pessoa["nome"], "idade": pessoa["idade"]})
        i += 1

print(f"A média de idade deste grupo é de: {int(media)} anos.")
if nome_mais_velho == None:
    print("Não há homens na lista.")
else:
    print(f"O homem mais velho da lista é: {nome_mais_velho}, com {idade_mais_velho} anos.")

if i > 1:
    print(f"{i} mulheres tem menos de 20 anos:")
    for pessoa in nome_mulheres:
        print(f"{pessoa["nome"]}, com {pessoa["idade"]} anos.")
elif i == 1:
    print(f"Apenas {i} mulher tem menos de 20 anos:")
    for pessoa in nome_mulheres:
        print(f"{pessoa["nome"]}, com {pessoa["idade"]} anos.")
else:
    print("Não há mulheres na lista com menos de 20 anos.")
