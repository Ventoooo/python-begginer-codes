listinha = []
while True:
    autenticador = input('Coloque um numero: ')

    if autenticador.isnumeric():
        if int(autenticador) in listinha:
            print('\033[31mEssa COISA já existe na lista\033[m')
            del autenticador
        else:
            listinha.append(int(autenticador))
            print('Valor adicionado com sucesso!')
    elif autenticador in 'PararPARARparar':
        print('processo finalizado\nOs resultados analizados foram:')
        break
    else:
        print('\033[31mcaracteres invalidos\033[m')
    print("Se seu desejo for finalizar digite [PARAR]")
print(sorted(listinha))
