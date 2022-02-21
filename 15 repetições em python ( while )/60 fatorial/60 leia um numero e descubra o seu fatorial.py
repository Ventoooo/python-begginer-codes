numero = int(input("coloque um numero e descubra o seu fatorial: "))
fato = numero -1
resultado = 0
while fato != 0:
    #print(numero, 'x', fato,'= ',resultado)
    resultado = numero * fato
    print('{} x {} = {}'.format(numero,fato,resultado))
    fato += -1
    numero = resultado

print("\033[32mO resultado desejado é: {}\033[m".format(resultado))

