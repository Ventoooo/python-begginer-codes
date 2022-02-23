lista = []
for valores in range(0, 5):
    lista.append(int(input(f'digite o valor desejado para posição {valores}: ')))
menor = maior = lista[0]
posisaomenor = posisaomaior = str()
for p, c in enumerate(lista):
    if maior < lista[p]:
        maior = lista[p]
    elif menor > lista[p]:
        menor = lista[p]
print(f'Aqui esta a lista: {lista}')

for p, c in enumerate(lista):
    if maior == c:
        posisaomaior = posisaomaior + str(p) + '...'
for p, c in enumerate(lista):
    if menor == c:
        posisaomenor = posisaomenor + '...' + str(p)
lista2 = lista[:]
print(f'''O maior numero esta na posição: {posisaomaior} e seu valor é de: {maior}
O menor numero esta na posição: {posisaomenor} e seu valor é de: {menor}''')
