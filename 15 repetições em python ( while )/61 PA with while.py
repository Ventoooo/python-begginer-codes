contador = 0
ptermo = int(input("coloque aqui o primeiro termo da P.A"))
razão = int(input("Coloque aqui a razão"))

while True:

    contador += +1
    print("O {}ª termo é: {}".format(contador, (razão-ptermo)+razão*contador))
    if contador == 10:
        break

