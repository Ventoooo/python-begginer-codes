lista = []
for c in range(0, 5):
    num = int(input(f'coloque o {c+1}ª numero: '))
    if c == 0:
        lista.append(num)
        print('colocado na ultima posição')
        print(lista)
    else:
        for posi, d in enumerate(lista):
            if max(lista) < num:
                lista.append(num)
                print('colocado na ultima posição')
                break
            elif num < d:
                lista.insert(posi, num)
                print(f'o valor foi colocado na {posi+1}ª posição')
                break
        print(lista)
