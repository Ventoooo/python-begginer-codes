cores = {'vermelho':'\033[31m',
         'azul':'\033[34m'}
a = int(input("coloque aqui o numero do comprimento da primeira reta :"))
b = int(input("coloque aqui o numero do comprimento da segunda reta :"))
c = int(input("coloque aqui o numero do comprimento da terceira reta :"))
if a + b > c and b + c > a and a + c > b:
    print("mandou bem, da pra fazer um triangulo tranquilão{}{}".format(cores['vermelho'],' Teste de cores!!'))
else:
    print("ta querendo fazer um triangulo com um predio e dois gravetinhos ????{}{}".format(cores['azul'],' Teste de cores 2'))
