R = 0
contagem = 0
print('coloque aqui 6 numeros a ser somados')
print('Obs: só serão somados os numeros que forem pares')
for c in range(0,6,):
    x = int(input(" numero :"))
    if (x % 2) == 0:
        R = R + x
        contagem = contagem + 1
print("{} desses numeros eram pares e a soma deles é igual á {}".format(contagem,R))