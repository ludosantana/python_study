#manipulando texto
frase = "  Cadeia de Caracteres em Python.  "

print(frase[7]) #mostra o sétimo caracter da string
print(frase[2:15]) #mostra os caracteres entre o 2 e 15
print(frase[2:16:2]) #mostra os caracteres entre 2 e 16 pulando 2 caracteres
print(frase[:8]) #mostra os 8 primeiros caracteres
print(frase[13:]) #mostra os 13 últimos caracteres
print((frase[3::2])) #mostra a partir do terceiro caracter, pulando 2 caracteres
print(frase[:12:2]) #mostra os 12 ultimos caracteres, pulando 2 caracteres

print("a frase \"{}\" possui \"{}\" caracteres.".format(frase, len(frase))) #len() conta o total de caracteres, incluindo espaços
print(frase.count("a")) #conta quantas vezes aparece o caracter entre "". É case sensitive.
print(frase.count("a", 0, 10)) #conta quantos caracteres em "" estão dentro do intervalo especificado.
print(frase.find("eia")) #mostra a posição onde ele encontrou pela primeira vez o trecho ou o caractere entre "".
print(frase.find("Android")) #sempre que seja especificado uma string que não tenha na frase, ele retorna -1
print("Cadeia" in  frase) #retorna true ou false. CASE SENSITIVE
print(frase.replace("Cadeia", "Sequência")) #substitui a string especificada por outra
print(frase.upper()) #CAIXA ALTA
print(frase.lower()) #caixa baixa
print(frase.capitalize()) #primeira letra da frase Maiuscula
print(frase.title()) #primeira letra de todas as palavras em Maiuscula
print(frase.strip()) #elimina espaços (desnecessários) antes e depois da string.
print(frase.rstrip()) #elimina espaços desnecessarios à direita da string
print(frase.lstrip()) #elimina espaços desnecessários à esquerda da string
print(frase.split()) #separa as palavras da string, desconsiderando os espaços e coloca numa lista
print("=".join(frase)) #adiciona o que esta entre "" entre os caracteres da string
