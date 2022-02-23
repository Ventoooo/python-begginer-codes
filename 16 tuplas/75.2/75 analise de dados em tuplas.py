tupla = pares = str()
paresqt = 0


for c in range(0, 4):
    while True:
        num = input('coloque um valor: ')
        if num.isnumeric():
            break
        else:
            print('Caracteres invalidos, tente novamente')
    tupla += num + ' '
tupla = tuple(tupla.split())


print('Você digitou os valores: ', ', '.join(tupla))


if tupla.count('9') != 0:
    print('o valor 9 apareceu', tupla.count('9'), 'ª vez')
else:
    print('O valor 9 não foi digitado')


if tupla.count('3') != 0:
    print('o primeiro valor 3 foi digitado como ', tupla.index('3')+1, 'ª valor')
else:
    print('o valor 3 não foi digitado')


for c in range(0, 4):
    if int(tupla[c]) % 2 == 0:
        paresqt += 1
        pares += tupla[c] + ' '
print(f'A quantidade de numeros pares digitados foram de {paresqt} e os numeros em questão foram {pares}')
