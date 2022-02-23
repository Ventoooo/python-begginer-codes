tupla = ('argel', '1.80','joão', '50cm', 'lauro', '1.75')

print('='*40)
print(f'{"Lista de compras ?":^40}')
print('='*40)
for tipo in range(0, len(tupla)):
    if tipo % 2 == 0:
        print(f'{tupla[tipo]:.<36}', end='')
    else:
        print(f'{tupla[tipo]:.>4}')
