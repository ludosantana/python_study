a = float(input("medida 01: "))
b = float(input("medida 02: "))
c = float(input("medida 03: "))

if a < b + c and b < a + c and c < a + b:
    print("É possível criar um triângulo!")
else:
    print("Não é possível criar um triângulo.")
