from datetime import datetime

quantidade = int(input("Quantas pessoas vai adicionar? "))
pessoas = []
ano_vigente = datetime.now().year

for c in range(quantidade):
    nome = input("Nome: ")
    data = int(input("Ano de nasc: "))
    pessoas.append({"nome": nome, "data_nas": data})

menores = []
maiores = []

for pessoa in pessoas:
    idade = ano_vigente - pessoa["data_nas"]
    if idade < 21:
        menores.append(pessoa)
    else:
        maiores.append(pessoa)

print(f"\033[7;32m Pessoas maiores de idade: {len(maiores)} \033[m")
for pessoa in maiores:
    print(f"Nome: {(pessoa["nome"]):.9} Ano de Nascimento: {pessoa["data_nas"]}")

print(f"\n\033[7;33m Pessoas menores de idade: {len(menores)} \033[m")
for pessoa in menores:
    print(f"Nome: {pessoa["nome"]:.9} Ano de Nascimento: {pessoa["data_nas"]}")
