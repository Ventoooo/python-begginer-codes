posisao = 0
lista = []
for c in range(0, 5):
    num = int(input('coloca aqui: '))
    if c == 0:

        lista.append(num)
    else:
        # descobre o primeiro numero maior que o numero colocado e apos descobrir coloca ele
        # na mesma casa do maior fazendo o maior ir uma casa para frente
        for pnum, numerodalista in enumerate(lista):
            if numerodalista > num:
                posisao = pnum
                print('O numero foi colocado na casa', pnum+1)
                break
        # caso não exista um numero maior que o numero digitado na lista adiciona +1 a ultima casa
        # da lista resultando na ultima posição
            else:
                posisao = pnum + 1
                print('O numero foi colocado na ultima casa')
        lista.insert(posisao, num)

    print(lista)
