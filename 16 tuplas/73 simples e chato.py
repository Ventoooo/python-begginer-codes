t = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
     'RB Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
     'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('Os 5 primeiros colocados são: ')
for c in range(0,5):
     print(t[c], end='')
     if c != 4:
          print(', ',end='')

print('\nOs 4 ultimos colocados são: ')
for o in range(-4,0):
     print(t[o],end='')
     if o != -1:
          print(', ',end='')

print('\nTodos os times em ordem alfabetica são: ')
print(sorted(t))

print('O time da chapecoense esta na {}ª posição'.format(t.index('Chapecoense')))
