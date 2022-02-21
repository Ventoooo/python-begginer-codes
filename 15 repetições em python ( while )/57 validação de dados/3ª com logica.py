c = 3
while c == 3:
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        c = 4
    else:
        print('tente novamente')
print('Programa encerrado')