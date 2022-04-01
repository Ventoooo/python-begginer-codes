from datetime import datetime


def horas_():
    horario = datetime.now().strftime('%H:%M')
    return horario


def data_():
    datas = datetime.now().strftime('%d/%m/%Y')
    return datas


dadosV = dadosD = dadosH = str()

lista_caixas = {}

lista_lucros = []

lista_gastos = []

while True:
    print('''\n
0-\033[33mPara adicionar o caixa inicial/Caixa Sicred\033[m
1-\033[33mPara adicionar os lucros\033[m
2-\033[33mPara adicionar os gastos\033[m
3-\033[33mPara consultar os resultados diarios\033[m
    ''')
    way = input('Escolha um numero para prosseguir:').strip().upper()
    if way == '0':
        lista_caixas['Caixa inicial'] = float(input('Caixa inicial = '))
        lista_caixas['Caixa Sicred'] = float(input('Caixa Sicred = '))
    elif way == '1':
        lista_lucros.append({'valor': float(input('Digite o \033[31mvalor\033[m a ser adicionado: ')),
                             'Descrição': str(input('Digite uma descrição sobre o produto: ')),
                             'Horario': horas_()})
    elif way == '2':
        lista_gastos.append({'valor': float(input('Digite o valor a ser descontado: ')),
                             'Descrição': str(input('Digite uma descrição sobre o produto: ')),
                             'Horario': horas_()})
    elif way == '3':
        while True:
            print('''\n1-\033[33mPara consultar o lucros até o momento\033[m
2-\033[33mPara consultar os gastos até o momento\033[m
3-\033[33mPara consultar o valor final do caixa\033[m
4-\033[33mPara voltar a adicionar valores\033[m''')
            way2 = input('Escolha um numero para prosseguir:').strip().upper()
            if way2 == '1':
                tl = 0
                for i, v in enumerate(lista_lucros):
                    print(f'    {i}-    {v["Descrição"]} > {v["valor"]}R$ as {v["Horario"]}Hs.')
                    tl += v["valor"]
                print(f'\033[32mO lucro total é de {tl}R$!\033[m')
