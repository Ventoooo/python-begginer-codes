from random import randint
from time import sleep

contador = 0
print('='*5, 'adivinhe um numero', '='*5)
while True:
    numerox = int(input("Digite um numero de 1 a 10: "))
    contador += +1
    print('Pensando', end='')
    sleep(1)
    numeropc = randint(1, 10)
    print('. . .')
    print("pensei no numero {}".format(numeropc))
    sleep(2)
    if numerox == numeropc:
        break
print("Parabéns!!!, você conseguiu acertar o numero que eu estava pensando\n A quantidade de vezes que vc tentou foi {}".format(contador))
