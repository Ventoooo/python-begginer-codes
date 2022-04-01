while True:
    data = {'Name': input("name: "),
            'Year': (2022 - int(input("age: "))),
            'CTPS': input("Put [ 0 ] if you don't have\nCarteira de Trabalho: ")}
    if data['CTPS'] == '0':
        data['CTPS'] = "Don't have"
        break
    else:
        data['contratação'] = int(input("Ano de contratação: "))
        data['salario'] = float(input("Salário: "))
        data['Aposentadoria'] = data['contratação'] + 35 - data['Year']
        break
print('=-='*20)
for k, v in data.items():
    print(f'- {k} is {v}')
