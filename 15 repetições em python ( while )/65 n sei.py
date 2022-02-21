finalizador = 0
contador = 0
media = 0
nmaior = 0
###gambi###
nmenor = 999999
###gambi###
while finalizador != 'n':
    n = int(input("coloque o numero: "))
    media += n
    contador += 1
    if n > nmaior:
        nmaior = n
    if n < nmenor:
        nmenor = n
    finalizador = str(input("Você deseja continuar ? [Y/N]: ").lower().strip())
print("""a media entre os numero colocados é de {:.2f}
Você colocou {} numeros
O maior deles foi {}
O menor deles foi {}""".format(media/contador,contador,nmaior,nmenor))

#ssolução pra gambi
#if contado == 1:
    #nmaior = nmenor = n
#else:
    #if n > nmaior:
        #nmaior = n
    #if n < nmenor:
        #nmenor = n
