from cores import cor

azul = cor["azul"]
verde = cor["verde"]
vermelho = cor["vermelho"]
fecha = cor["fecha"]

n = input('Digite um número: ')

if n.isnumeric():
    nInt = int(n)
    d = nInt * 2
    t = nInt * 3
    r = nInt ** (1 / 2)
    print(f'O número é: {azul}{n}{fecha}\nSeu dobro é: {verde}{d}{fecha}\nSeu triplo é: {azul}{t}{fecha}\nSua raíz é: {verde}{r:.3}{fecha}')
elif n.isalpha():
    print(vermelho,'Você digitou uma letra, não há o que fazer.',fecha)
else:
    print('Sem valor não há o que fazer.')
