print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

pt = int(input("Primeiro termo: "))
r = int(input("Razão: "))

for c in range(0, 10):
    print(f"{pt} →", end=" ")
    pt += r
print("ACABOU!")
