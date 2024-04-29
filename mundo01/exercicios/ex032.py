import calendar

ano = int(input("Digite um ano: "))
if calendar.isleap(ano) == True:
    print(f"\033[7;36m{ano} é um ano Bissexto!\033[m")
else:
    print(f"\033[7;32m{ano} não é um ano Bissexto!\033[m")
