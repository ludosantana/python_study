from cores import cor

larg = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))
mQuad = larg * alt
lTinta = 2.0
r = mQuad / lTinta

print(f'A área total da parede é de {cor["verde"]}{mQuad:.2f}m²{cor["fecha"]}, você vai precisar de {cor["vermelho"]}{r:.2f}{cor["fecha"]} litros de tinta para pintar a parede inteira.')
