lista = []
for t in range(0, 5):
    num = int(input(f'digite o {t}ª numero: '))
    if t == 0:
        lista.append(num)
    else:
        for p, c in enumerate(lista):
            if c - num >= 0:  # if c > num: funciona
                lista.insert(p, num)
                break
            if max(lista) < num:
                lista.append(num)
                break
    print(lista)
