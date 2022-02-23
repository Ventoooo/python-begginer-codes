from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os numeros ramdomizados foram: ', end='')
for x in tupla:
    print(x, end=' ')
print(f'\n o maior numero ramdomizado foi: {max(tupla)}\n o menor numero ramdomizado foi: {min(tupla)}')
