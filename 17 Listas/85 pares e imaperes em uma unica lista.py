lista = [], []
for c in range(0, 7):
    while True:
        num = input('coloque um numero: ')
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('caracteres invalidos, tente novamente')
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
print(f'''Os valores pares foram:\n{sorted(lista[0])}
Os valores impares foram:\n{sorted(lista[1])}''')
