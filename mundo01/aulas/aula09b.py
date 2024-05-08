from random import shuffle
frase = "Curso em Vídeo Python"
print(frase.upper().count("O")) #trasnformar a frase em maiuscula com .upper() e o count() consegue contar as letras maiusculas
print(len(frase))

separa = frase.split()

shuffle(separa) #coloquei um shuffle so pra brincar, pois o .split() transforma a string numa lista

print(separa)
print(separa[0][2]) #mostra o primeiro item da lista e mostra o terceiro caracter desse item
print(" ".join(separa))

frase = frase.replace("Python", "Android")
print(frase)
print(len(frase))

print("""jasljkdnalsjdnalsjd s dajsn daj snlakjs d
alkjsdlkajs lakjs dnakjsd nlakjsd nlakjsd ln
alsjkdal kjsdlakjsd lajsdbalkjsdbalksjdbalksdjb 
sljkadbajsdblajsdblakjsdblajsdblajsdb""") #com aspas """ é possível digitar longos textos
