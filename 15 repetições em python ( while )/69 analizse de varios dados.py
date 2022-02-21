contador = h_maior18 = m_menor20 = hcount = continua = 0
while True:

    while contador != 2:
        if contador == 0:

            idade = input("Idade: ")
            if idade.isnumeric():
                contador += 1
                idade = int(idade)
            else:
                print('Caracteres invalidos, tente novamente')

        if contador == 1:
            sexo = str(input("Sexo [M/F]: ")).strip()[0]
            if sexo in 'MmFf':
                contador += 1
            else:
                print('Caracteres invalidos, tente novamente')

        if contador == 2:
            if sexo in 'Mm':
                hcount += 1

            if idade > 18 and sexo in 'Mm':
                h_maior18 += 1

            if idade < 20 and sexo in 'Ff':
                m_menor20 += 1

    continua = str(input('Você deseja continuar ? [S/N]'))
    if continua in 'Nn':
        print(f'''A quantidade de mulheres menores de 20 anos é de: {m_menor20}
        A quantidade de homens maiores de 18 é de: {h_maior18}
        A quantidade total de homens é de: {hcount}''')
        break
    elif continua in 'Ss':
        contador = 0
    else:
        print('Caracteres invalidos, tente novamente')
