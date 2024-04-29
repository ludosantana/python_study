from cores import cor

salario = float(input('Salário d funcionário R$ '))
aum = 15
novoSal = salario + (salario * aum / 100)

print(f'O salário com {cor["roxo"]}{aum}%{cor["fecha"]} de aumento ficará: {cor["azul"]}R$ {novoSal:.2f}{cor["fecha"]}.')
