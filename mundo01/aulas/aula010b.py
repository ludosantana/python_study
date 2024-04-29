nome = str(input("Qual é seu nome? "))
if nome == "Gustavo":
    print("Que nome lindo você tem!", end=" ")
else:
    print("Seu nome é tão normal!", end=" ")
print("Bom dia {}!".format(nome))
