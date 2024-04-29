nome = str(input("Digite um nome completo: ")).strip()

if "SILVA" in nome.upper():
    print("Você \033[1;35mfaz\033[m parte da família SILVA")
else:
    print("Você \033[1;31mnão\033[m faz parte da família SILVA.")
