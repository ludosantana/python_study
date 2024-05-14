from datetime import datetime

ano = datetime.now().year
i = 0

for c in range(7):
    nas = int(input("Ano de nascimento: "))
    idade = ano - nas
    if idade < 21:
        i += 1

print(f"{i} pessoa(s) são menores de idade.")
print(f"{7 - i} pessoa(s) são maiores de idade.")
