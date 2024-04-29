cores = {
    "verde": "\033[1;32m",
    "roxo": "\033[4;35m",
    "fecha": "\033[m"
}

#Desafio 001 - Hello World
print('Hello, {}World!{}'.format(cores["verde"], cores["fecha"]))

#Hello World com variavel
msg = f'Hello, {cores["roxo"]}World!{cores["fecha"]}'
print(msg)
