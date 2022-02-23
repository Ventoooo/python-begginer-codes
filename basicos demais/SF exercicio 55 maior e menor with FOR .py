
peso_menor = 0
peso_maior = 0

for c in range(0,5):

    peso = float(input("coloque aqui o peso"))

    if peso > peso_maior:
        peso_maior = peso
    if peso_menor == 0:
        peso_menor = peso
    elif peso < peso_menor:
        peso_menor = peso


print("O MAIOR PESO É DE {}".format(peso_maior))
print("O MENOR PESO É DE {}".format(peso_menor))