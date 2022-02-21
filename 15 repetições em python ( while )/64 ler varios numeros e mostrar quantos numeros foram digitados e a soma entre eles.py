nivelador = 0
somatotal = 0
while True:
    n = int(input("coloque quantos numeros vc quiser \nA condição de parada é digitar [999] \nDigite os numeros desejados: "))
    if n == 999:
        break
    somatotal += n
    nivelador += 1
print("""\033[32mA quantidade de numeros colocados foram de :{}
e a soma entre eles é igual a: {}""".format(nivelador, somatotal))