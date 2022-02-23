lista = []
listap = []
listai = []
while True:
    num = input('Caso queira parar digite [sair]\n'
                'digite aqui o numero desejado: ').lower().strip()
    if num.isnumeric():
        lista.append(int(num))
    elif num == 'sair':
        print('adicionador finalizado!')
        break
    else:
        print('Caracteres invalidos digite novamente: ')
        del num
print('A lista completa é\n', lista)
for c in lista:
    if c % 2 == 0:
        listap.append(c)
    if c % 2 == 1:
        listai.append(c)
print('A lista com os pares:\n', listap)
print('A lista com os impares:\n', listai)
