contador = 0
limitador = 0
moderador = 10
while moderador != 0:
    limitador += moderador
    while contador != limitador:
        contador += 1
        print(contador,' ', end='')

        if contador == limitador:
            print(end='''
''')
            moderador = int(input("quantos a mais vc quer ver ?"))

