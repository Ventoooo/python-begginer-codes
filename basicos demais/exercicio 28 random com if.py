import random
from time import sleep
userr = int(input("coloque aqui o numero de -1- a -5- que vc acha que o computador vai pensar :"))
pensa = [1,2,3,4,5]
pensou = random.choice(pensa) #melhor seria o randint(0,5) faz ele randomizar um inteiro de 1 a 5
print('pensando....')
sleep(2)
print('pensei no numero {}!'.format(pensou))
if userr == pensou:
    print("MANDOU BEM MÃE DINA !!!!")
else:
    print("você errou, a resposta certa era", pensou)