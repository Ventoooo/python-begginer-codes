nivelador = 0
limitador = int(input("Coloque aqui até que ponto vc quer ver a sequencia de fibonacci: "))
sequencia = 2
sequencia_anterior = 1
mediador = 0

while limitador != 0:
    if nivelador == 0:
        print('''0
1
1''')
        mediador = ((sequencia - sequencia_anterior) + sequencia)
    else:
        mediador = ((sequencia_anterior) + sequencia)

    print(mediador)
    sequencia_anterior = sequencia
    sequencia = mediador
    if nivelador == limitador:
        print("time out")
        limitador = 0
    nivelador += 1