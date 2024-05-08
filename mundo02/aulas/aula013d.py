l = []
for c in range(0, 3):
    n = int(input("Digite um valor: ")) #faço a pergunta 3x
    l += [n] #e adiciono os valores na lista
print(l)
v = int(input("Qual item da lista gostaria de mostrar? "))
print(l[v])
print("FIM")
