sal = float(input("Qual seu salário? R$ "))

if sal > 1250:
    print(f"Aumento: \033[1;32m10%\033[m.\nNovo salário \033[1;36mR$ {sal + (sal * 10 / 100):.2f}\033[m.")
else:
    print(f"Aumento: \033[1;32m15%\033[m.\nNovo salário \033[1;36mR$ {sal + (sal * 15 / 100):.2f}\033[m.")
