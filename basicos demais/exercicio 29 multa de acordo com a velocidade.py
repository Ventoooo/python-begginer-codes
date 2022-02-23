velocidade = float(input("coloque aqui a velocidade que o carro estava andando :"))
if velocidade >= 80:
    print("""\033[1;31m    Você ultrapassou a velocidade limite da pista de 80 KM
    O veiculo em questão sera multado de acordo com o limite de velocidade da pista!
    O valor a ser pago será de: {:.2f} R$""".format(7*(velocidade-80)))
else:
    print("\033[1;32m Você estava a {} KM, uma velocidade permitida pela via\n Tenha uma boa tarde !!\033[1;32m".format(int(velocidade)))