numero1 = int(input('1ª Numero: '))
numero2 = int(input('1ª Numero: '))

while True:

    print("""    \033[33m[1] para somar
    [2] para multiplicar
    [3] para descobrir o maior
    [4] para colocar novos numeros
    [5] para sair do programa\033[m""")
    escolha = int(input('escolha: '))

    if escolha == 1:
        print("{} + {} = {}".format(numero1, numero2, numero1+numero2))
    elif escolha == 2:
        print("{} x {} = {}".format(numero1, numero2, numero1*numero2))
    elif escolha == 3:
        if numero2 > numero1:
            print("o numero {} é maior que {}".format(numero2, numero1))
        else:
            print("o numero {} é maior que {}".format(numero1, numero2))

    elif escolha == 4:
        numero1 = int(input('1ª Numero: '))
        numero2 = int(input('1ª Numero: '))

    elif escolha == 5:
        escolha = str(input('Você realmente deseja sair ? [Y/N]\n: '))
        if escolha in 'Y y':
            print("Bom descanso !!!")
            break
        else:
            print('Voltando . . .')
    else:
        print("Caracteres invalidos, Digite novamente")



