#nome = str(input("Digite o nome de uma cidade: ")).title()
cid = str(input("Em que cidade você nasceu? ")).strip()

""" MINHA SOLUÇÃO
if nome.find("Santo") == 0 or nome.find("São") == 0 or nome.find("Santos") == 0 or nome.find("Santa") == 0:
    print("A primeira palavra de \"{}\" é um santo.".format(nome))
else:
    print("A primeira palavra não é santo, ou não tem nada de santo na palavra.")
"""
print(cid[:5].upper() == "SANTO")
