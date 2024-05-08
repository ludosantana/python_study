#recebe dado do usuário
n = input('Digite algo: ')

#verificação do tipo da informação
if n.isnumeric():
    print('{} é um número!'.format(n))
elif n.isalpha():
    print('{} é uma string!'.format(n))
elif n.isalnum() or n.replace(".", "").isalnum():
    print('{} é um caractere alfanumérico!'.format(n))
elif n.replace(".", "").isdigit():
    print('{} é um número decimal.'.format(n))
else:
    print('Não tem nada digitado, apenas espaço em branco.')

if n.isupper():
    print('{} está apenas em maiúscula!'.format(n))
elif n.islower():
    print('{} está apenas em minúscula!'.format(n))
elif n.istitle():
    print('{} está com a primeira letra maiúscula!'.format(n))
