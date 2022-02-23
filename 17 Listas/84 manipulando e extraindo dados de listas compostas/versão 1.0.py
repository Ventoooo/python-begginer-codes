lista_unica = list()
bridge = list()
max_name = []
min_name = []
finisher = str()
while True:
    bridge.append(input('Put your name on here: '))
    bridge.append(int(input('Put your weight on here: ')))
    lista_unica.append(bridge[:])
    bridge.clear()
    finisher = input("Do you want to continue ?").strip().upper()
    if finisher == 'N':
        break
for element in range(0, len(lista_unica)):
    bridge.append(lista_unica[element][1])
for element in range(0, len(lista_unica)):
    if max(bridge) == lista_unica[element][1]:
        max_name.append(lista_unica[element][0])

    elif min(bridge) == lista_unica[element][1]:
        min_name.append(lista_unica[element][0])

print(f'''A quantidade de pessoas cadastradas foi de {len(lista_unica)}
A(s) pessoa(s) mais pesada(s) tem o peso de {max(bridge)}
São eles: {max_name}
A(s) pessoa(s) mais leve(s) tem o peso de {min(bridge)}
São eles: {min_name}''')
