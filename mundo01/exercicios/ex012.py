from cores import cor

preco = float(input('Informe o preço do produto R$ '))
desc = 5
novoPreco = preco - (preco * desc / 100)

print(f'O preço deste produto com {cor["verde"]}{desc}%{cor["fecha"]} de desconto vai ficar: {cor["vermelho"]}R$ {novoPreco:.2f}{cor["fecha"]}.')
