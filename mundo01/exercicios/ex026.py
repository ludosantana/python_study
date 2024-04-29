frase = str(input("Digite uma frase: ")).upper().strip()

if frase.count("A") == 1:
    print("A letra \033[1;35m\"A\"\033[m aparece apenas \033[1;31m1\033[m vez.")
    print("A primeira posição da letra \033[1;35m\"A\"\033[m é \033[1;31m{}\033[m.".format(frase.find("A")))
    print("A última posição da letra \033[1;35m\"A\"\033[m é \033[1;31m{}\033[m".format(frase.rfind("A")))
elif frase.count("A") > 1:
    print("A letra \033[1;35m\"A\"\033[m aparece \033[1;31m{}\033[m vezes.".format(frase.count("A")))
    print("A primeira posição da letra \033[1;35m\"A\"\033[m é \033[1;31m{}\033[m.".format(frase.find("A")+1)) #adiciona +1 pq o python começa a contar do 0
    print("A última posição da letra \033[1;35m\"A\"\033[m é \033[1;31m{}\033[m.".format(frase.rfind("A")+1))
else:
    print("A letra \033[1;31m\"A\"\033[m não aparece na frase.")
