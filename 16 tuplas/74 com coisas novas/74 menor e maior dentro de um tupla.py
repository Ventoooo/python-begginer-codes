from random import randint
maior = menor = 0
tup = str()
for num in range(0,5):
    aleatorio = str(randint(0,9))
    tup += aleatorio
print(tuple(tup))

## separando o menor
for num in range(0,5):
    if num == 0:
        menor = tup[0]
    if int(menor) > int(tup[num]):
        menor = tup[num]
print(f'o menor numero da tupla é {menor}')

### ''  '' maior
for num in range(0,5):
    if int(maior) < int(tup[num]):
        maior = tup[num]
print(f'o maior numero da tupla é {maior}')