frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]#tratamento de string como se fosse junto[1] índice da letra. No caso de tras para frente

if inverso == junto:
    print("Temos um palíndromo.")
else:
    print("A frase digitada não é um palíndromo.")
