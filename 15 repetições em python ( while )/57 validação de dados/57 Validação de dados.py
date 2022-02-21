passe = 0
while passe != 1:
    sexo = str(input("Sexo [F/M]: ")).strip().upper()
    if sexo == 'M' or sexo == 'F':
        passe = 1
    else:
        print('Caracteres invalidos, digite novamente')

if sexo == 'F':
    print('você é uma mulher')
else:
    print('você é um homem')

