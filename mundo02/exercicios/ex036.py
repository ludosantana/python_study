from cores import cor
def verifica_valor_casa():
    casa = input("Qual o valor do imóvel? R$ ").strip()
    if casa.replace(".", "").isdigit():
        casa = int(casa)
        return casa
    else:
        print("\033[7;31mDigite um valor numérico correto.\033[m")
        return verifica_valor_casa() #precisei utilizar o return aqui ou o primeiro valor incorreto seria adicionado à variavel la em baixo.

def verifica_valor_salario():
    salario = input("Qual seu salário? R$ ").strip()
    if salario.replace(".", "").isdigit():
        salario = float(salario)
        return salario
    else:
        print("\033[7;31mDigite um valor numérico válido.\033[m")
        return verifica_valor_salario()

def verifica_valor_ano():
    anos = input("Gostaria de pagar em quantos anos? ").strip()
    if anos.replace(".", "").isdigit():
        anos = int(anos)
        return anos
    else:
        print("\033[7;31mDigite um valor numérico válido.\033[m")
        return verifica_valor_ano()

def simulacao(casa, salario, anos):
    meses = anos * 12
    prestacao = casa / meses
    limite_sal = salario * 30 / 100
    por = prestacao * 100 / salario #encontra a % equivalente da prestacao ao salario

    if prestacao <= limite_sal:
        print(f"{cor["verde"]}Parabéns, você conseguiu o empréstimo para comprar sua casa!{cor["fecha"]}")
        print("\033[7;32m -=- \033[m" * 12)
        print(f"\033[4mValor do imóvel: {cor["roxo"]}R$ {casa:.2f}{cor["fecha"]}")
        print(f"\033[4mValor das prestações: {cor["azul"]}R$ {prestacao:.2f}{cor["fecha"]}")
        print(f"\033[4mSeu salário: {cor["verde"]}R$ {salario:.2f}{cor["fecha"]}")
        print(f"\033[4mMeses a pagar: {cor["amarelo"]}{meses}{cor["fecha"]}")
    else:
        print(f"{cor["vermelho"]}A prestação da casa equivale a {por:.2f}% do seu salário.\nNão será possível realizar o empréstimo.{cor["fecha"]}")
        print("\033[7;31m -=- \033[m" * 10)
        print(f"\033[4mValor do imóvel: {cor["roxo"]}R$ {casa:.2f}{cor["fecha"]}")
        print(f"\033[4mValor das prestações: {cor["vermelho"]}R$ {prestacao:.2f}{cor["fecha"]}")
        print(f"\033[4mSeu salário: {cor["vermelho"]}R$ {salario:.2f}{cor["fecha"]}")
        print(f"\033[4mMeses a pagar: {cor["amarelo"]}{meses}{cor["fecha"]}")

casa = verifica_valor_casa()
salario = verifica_valor_salario()
ano = verifica_valor_ano()

simulacao(casa, salario, ano)
