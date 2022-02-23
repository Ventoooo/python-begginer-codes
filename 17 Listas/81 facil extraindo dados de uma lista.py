lista = []
p5 = str()
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

print(f'A quantidade de numeros digitados foi de: {len(lista)}')
print(f'A lista organizada em ordem decrescente é:\n'
      f'{sorted(lista, reverse=True)}')
for i, c in enumerate(lista):
    if c == 5:
        p5 = p5 + str(i) + '...'
if 5 in lista:
    print(f'A quantidade de numeros 5 que foi digita é de {lista.index(5)},'
          f' e eles estão na posição {p5}')
else:
    print('não tinha nenhum 5 na lista')
