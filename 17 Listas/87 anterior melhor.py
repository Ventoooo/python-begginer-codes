lista = []
pares = []
for c in range(0, 3):
    lista.append(int(input(f'numero da 0, {c}: ')))
for c in range(0, 3):
    lista.append(int(input(f'numero da 1, {c}: ')))
for c in range(0, 3):
    lista.append(int(input(f'numero da 2, {c}: ')))
print(f"""{lista[0],lista[1],lista[2]}
{lista[3],lista[4],lista[5]}
{lista[6],lista[7],lista[8]}""")

for index, element in enumerate(lista):
    if element % 2 == 0:
        pares.append(lista[index])
print(f'O valor da soma de todos os pares é de: {sum(pares)}')
print(f'O valor da soma de toda a terceira coluna é de: {lista[2]+lista[5]+lista[8]}')
print(f'O maior valor da segunda linha é de {max(lista[3:6])}')
