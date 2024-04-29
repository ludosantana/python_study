from cores import cor

metro = float(input('Digite um valor em metros: '))
cent = int(metro * 100)
mil = int(metro * 1000)

print('{}Você digitou:\n{} m = {} cm = {} mm{}'.format(cor["verde"], metro, cent, mil, cor["fecha"]))
