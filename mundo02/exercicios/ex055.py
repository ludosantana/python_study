pesos = []

for c in range(5):
    pesos.append(input("Digite um peso: "))

print(f"Entre os pesos: {", ".join(pesos)}\nO maior é: {max(pesos)}.\nO menor é: {min(pesos)}")
