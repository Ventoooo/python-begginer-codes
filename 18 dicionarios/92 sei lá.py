while True:
    data = {'Nome': input("nome: "),
            'Ano': input("ano de nascimento: "),
            'CTPS': input("Put [ 0 ] if you don't have\nCarteira de Trabalho: ")}
    if data['CTPS'] == '0':
        break
    else:
        data['contratação'] = int(input("Ano de contratação: "))

