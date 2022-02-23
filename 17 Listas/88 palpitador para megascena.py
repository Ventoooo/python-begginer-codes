from random import randint
lista = []
dados = []
aleatorio = int()
limitnum = limit = int(input('Quantos jogos vc deseja jogar ? :'))
while len(lista) != limit:
    while True:
        last_value = randint(0, 60)
        dados.append(last_value)
        for element4 in dados[:-1]:
            if element4 == last_value:
                dados.pop()
        if len(dados) == 6:
            lista.append(dados[:])
            dados.clear()
            break
for elesment3 in range(0, limitnum):
    print(lista[elesment3])
