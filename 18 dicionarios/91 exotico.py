from random import randint
from time import sleep
# import operator
jogador = 1
Dict = {}
quantidade_de_jogadores = 4
for c in range(quantidade_de_jogadores):
    Dict['Jogador' + str(jogador)] = randint(1, 7)
    jogador += 1
lista = list(Dict.copy().items())
# print(sorted(lista, key=operator.itemgetter(1)))
ordem = sorted(lista, key=lambda a: a[1], reverse=True)
print(ordem)
print('Valores sorteados: ')
for c in lista:
    print(f'    O {c[0]} tirou {c[1]}')
    sleep(1)
print('Ranking dos Jogadores: ')
for v, c in enumerate(ordem):
    print(f'    Em {v+1}° lugar: {c[0]} com {c[1]}')
    sleep(1)
