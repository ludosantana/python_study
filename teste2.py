from random import randint

contador = 0 #variavel global
def gera_num_ale():
    n = randint(0, 5)
    return n

def recebe_num():
    n = input("Digite um número entre 0 e 5: ").strip()
    return n

def verifica_num():
    global contador #acessar a variavel global
    n_recebido = recebe_num() #coloca a função que recebe numero numa variavel

    if n_recebido.isdigit(): #verifica se o numero é um digito válido
        n_recebido = int(n_recebido) #se for um dig valido, transforma em INT
        if -1 < n_recebido < 6: #verifica se o num é de 0 até 5
            compara_nums(n_recebido)
        else:
            contador += 1
            print("Digite um número entre 0 a 5.")
            verifica_num() #se o num não estiver entre 0 a 5, executa a fun novamente
    else:
        contador += 1
        print("Não é um digito válido.")
        verifica_num() #se n for um dig valido, executa a funcao novamente

def compara_nums(n_recebido):
    global contador #acessar a variavel global
    num_ale = gera_num_ale()
    num_user = n_recebido
    compara = num_user == num_ale

    if compara == True and contador == 0:
        print(f"Parabéns você acertou de primeira! O Número sorteado foi {num_ale}!")
    elif compara == True and contador > 0:
        print(f"Parabéns, você acertou depois de {contador} tentativas. O número sorteado foi {num_ale}.")
    else:
        contador += 1
        print(f"Você errou! O número sorteado foi {num_ale}. Tente novamente!")
        verifica_num()

verifica_num()
