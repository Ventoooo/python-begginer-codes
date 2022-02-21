fatorial = int(input("fatorial do nomeuro :"))
nivelador_decre = fatorial
while nivelador_decre != 0:

    print("{} ".format(nivelador_decre), end="")
    nivelador_decre -= 1

    if nivelador_decre != 0:
        fatorial *= nivelador_decre
    else:
        fatorial *= 1
    if nivelador_decre != 0:
        print("x ", end="")
    else:
        print("= {}".format(fatorial), end="")
