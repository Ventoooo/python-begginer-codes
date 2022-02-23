resposta = 0

n = int(input("coloque um numero e descubra se ele é primo"))
for c in range(2,n+1):

    if n % c == 0:
        resposta += 4
        print('\033[33m{} \033[m'.format(c), end='')
    else:
        print('{} '.format(c), end='')
if resposta > 4:
    print("n é primo")
else:
    print("é primo")




