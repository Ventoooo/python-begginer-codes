contador = 0
limitador = 9

ptermo = int(input("coloque aqui o primeiro termo da P.A: "))
razão = int(input("Coloque aqui a razão: "))

while contador != limitador:

    if contador == 0:
        print('O 1ª termo é:', ptermo)
    contador += +1
    print("O {}ª termo é: {}".format(contador+1, ptermo+razão*contador))

    if contador == limitador:
        limitador2 = int(input("quantos termos vc deseja saber alem desse? : "))
        limitador += limitador2

    if limitador == 0:
        contador = limitador
