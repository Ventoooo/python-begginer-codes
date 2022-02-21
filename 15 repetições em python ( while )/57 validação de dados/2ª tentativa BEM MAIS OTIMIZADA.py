while True:
    sexo = str(input("sexo [M/F]: ")).strip().lower()
    if sexo == 'm' or sexo == 'f':
        break
    else:
        print("caracteres invalidos, tente novamente")
print('programa finalizado')