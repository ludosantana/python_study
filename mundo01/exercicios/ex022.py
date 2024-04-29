def nome(): #criei uma funcao apenas por graça
    #recebendo a informação do usuario
    name = str(input("Digite seu nome completo: ")).strip()

    print("Olhe algumas configurações do seu nome:")
    print("-" * 50)
    nameS = name.split() #divido as palavras numa lista
    #name = " ".join(name) #junto os itens da lista, adicionando espaço entre eles

    #CAIXA ALTA
    print(name.upper())

    #caixa baixa
    print(name.lower())

    #SOLUÇÃO DO GUANABARA - bem mais simples
    print("Seu nome tem ao todo \033[1;35m{}\033[m letras.".format(len(name) - name.count(" ")))
    print("Seu primeiro nome tem \033[1;36m{}\033[m letras.".format(len(nameS[0])))

    """ MINHA SOLUÇÃO
    #numero de letras, desconsiderando os espaços
    nameSplit = name.split() #primeiro dividi as palavras, colocando numa lista
    nameJoin = "".join(nameSplit) #depois juntei os itens da lista, sem espaço entre elas
    print("Seu nome possui {} caracteres.".format(len(nameJoin))) #leio o numero de caracteres de todos os itens da lista (ja sem espaços)
    print("O primeiro nome possui {} caracteres.".format(len(nameSplit[0]))) #leio o numero de caracteres do primeiro item da lista
    """

#aqui chamo a funcao
nome()