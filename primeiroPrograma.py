#Recebe e mostra o nome do usuário

nome = input('Digite seu nome: ')
print('Que prazer ter você neste curso, {}'.format(nome))

#Recebe e mostra quando o usuário nasceu

dia = input('Informe o dia em que você nasceu: ')
mes = input('Agora, informe o mês: ')
ano = input('Por fim, informe o ano: ')
#print('Muito bem',nome+'! Então você nasceu em', dia+'/'+mes+'/'+ano+'. Que legal!')
print('Muito bem, {}! Então você nasceu em {}/{}/{}! Que legal!'.format(nome,dia,mes,ano))

#Recebe números e soma

numero_um = int(input('Continuando, informe um numero: '))
numero_dois = int(input('Informe mais um número: '))
print('A soma entre {} e {} é {}.'.format(numero_um,numero_dois,numero_um+numero_dois))
