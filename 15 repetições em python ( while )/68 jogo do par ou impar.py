from random import randint

nivelador = 0
soma = 0

while True:
    num = int(input('digite um numero: '))
    imip = str(input('Você quer par ou impar [P/I]')).upper().strip()[0]

    num_com = randint(0, 10)
    soma = num + num_com

    print(f"Você escolheu {num} e computador {num_com}, a soma desses numero é igual a {(num_com+num)}\n\
A soma destes numeros é igual a um numero : ",end='')

    if soma % 2 == 0 and imip == 'P':
        print('\033[35mPAR')
        print('\033[32mParabéns você venceu \nVamos novamente!!\033[m')
        nivelador += 1
    elif soma % 2 == 1 and imip == 'I':
        print('\033[35mIMPAR')
        print('\033[32mParabéns você venceu \nVamos novamente!!\033[m')
        nivelador += 1
    else:
        if soma % 2 == 0:
            print('\033[35mPAr')
        if soma % 2 == 1:
            print('\033[35mIMPAr')
        print(f"\033[31mVocê perdeu! \n a quatidade de vezes que você ganhou é de: {nivelador}\033[m")
        break
