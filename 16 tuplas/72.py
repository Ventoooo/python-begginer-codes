sec1a20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = input('digite um numero de 0 a 20\nou digite [sair] para finalizar: ')
        if num in range(0, 21):
            print('tudo ok')
            break
        elif num in 'SairsairSAIR':
            break
        else:
            print('\033[31mcaracteres invalidos, digite novamente\033[m')
    if num in 'SairsairSAIR':
        break
    resposta = sec1a20[int(num)]
    print(resposta)
print('programa encerrado!')
