mutiplicador = 0
while True:
    if mutiplicador == 0:
        num = int(input('Quer ver a tabuada de que valor ? : '))
    if num < 0:
        print('\033[31mprograma encerrado')
        break
    mutiplicador += 1
    print('{} x {} = {}'.format(num,mutiplicador,num * mutiplicador))
    if mutiplicador == 10:
        mutiplicador = 0



