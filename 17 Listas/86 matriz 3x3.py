lista = []
for c in range(0, 3):
    lista.append([int(input(f'numero da 0, {c}: '))])
for c in range(0, 3):
    lista.append([int(input(f'numero da 1, {c}: '))])
for c in range(0, 3):
    lista.append([int(input(f'numero da 2, {c}: '))])
print(f"""{lista[0],lista[1],lista[2]}
{lista[3],lista[4],lista[5]}
{lista[6],lista[7],lista[8]}""")
