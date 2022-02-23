tupla = (int(input('Coloque aqui o 1ª numero desejado')),
         int(input('Coloque aqui o 2ª numero desejado')),
         int(input('Coloque aqui o 3ª numero desejado')),
         int(input('Coloque aqui o 4ª numero desejado')))
print('O valor 9 apareceu {} vezes'.format(tupla.count(9)))

if tupla.count(3) != 0:
    print('o valor 3 foi digitado pela primeira vez na posição', tupla.index(3))
else:
    print('Não existe nenhum valor 3')

print('Os numeros pares foram: ', end='')
for c in tupla:
    if int(c) % 2 == 0:
        print(c, end=' ')
