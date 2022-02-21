notas50 = notas20 = notas10 = notas1 = validador = 0
while True:
    while validador != 1:

        valor = input("Valor a ser sacado: ")
        if valor.isnumeric():
            valor = int(valor)
            validador = 1
        else:
            print('caracteres invalidos tente novamente')

    if valor >= 50:
        notas50 = valor // 50
        valor = valor % 50
    if valor >= 20:
        notas20 = valor //20
        valor = valor % 20
    if valor >= notas10:
        notas10 = valor // 10
        valor = valor % 10
    if valor >= 1:
        notas1 = valor // 1

    print(f'''São:
{notas50} notas de 50R$
{notas20} notas de 20R$
{notas10} notas de 10R$
{notas1} notas de 1R$''')
    while validador != 2:
        continua = input('você deseja continuar? [Y/N}').strip()[0]
        if continua not in 'YyNn':
            print('Caracteres invalidos, tente novamente')
        else:
            validador = 2

    if continua in 'Nn':
        print('programa encerrado')
        break
    if continua in 'Yy':
        notas50 = notas20 = notas10 = notas1 = 0
        validador = 0
