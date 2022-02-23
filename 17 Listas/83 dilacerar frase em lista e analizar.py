lista = []
cochopen = cochclose = 0
expres = input('coloque aqui sua expressão')
for c in range(0, len(expres)):
    if expres[c] == '(':
        cochopen += 1
    if expres[c] == ')':
        cochclose += 1
if cochopen != cochclose:
    print('Sua expressão esta errada')
else:
    print('tá certinho')