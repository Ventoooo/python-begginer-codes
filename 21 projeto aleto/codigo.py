from datetime import datetime
import pickle


def horas_():
    horario = datetime.now().strftime('%H:%M')
    return horario


def data_():
    datas = datetime.now().strftime('%d/%m/%Y')
    return datas


def vermelhoevidencia_(x):
    r = f'\033[31m{x}\033[m'
    return r


def clear():
    print("\n" * 130)


dadosH = str()

dadosDICT = {}

lista_caixas = {}

lista_lucros = []

lista_gastos = []

lista_pickle = {'lucros': [], 'gastos': []}
#   criar pasta com a data


#   codigo

while True:

    #   colocar valor inicial do caixa

    if len(lista_caixas) == 0:
        while True:
            dadosH = input('Caixa inicial = ')
            if dadosH.isnumeric():
                dadosH = float(dadosH)
                lista_caixas["caixa inicial"] = dadosH
                break
            print('Dados invalidos!')

        while True:
            dadosH = input('Caixa Sicred = ')
            if dadosH.isnumeric():
                dadosH = float(dadosH)
                lista_caixas["caixa sicred"] = dadosH
                break
            print('Dados invalidos!')

    print('''\n
0-\033[33mPara adicionar o caixa inicial/Caixa Sicred\033[m
1-\033[33mPara adicionar os lucros\033[m
2-\033[33mPara adicionar os gastos\033[m
3-\033[33mPara consultar os resultados diarios\033[m
    ''')
    way = input('Escolha um numero para prosseguir:').strip()


#   função para 1
    if way == '1':
        dadosDICT["Descrição"] = input(f'\033[32mGANHO\033[m - Digite uma descrição sobre o produto: ')
        while True:
            dadosDICT["Valor"] = input('Digite o \033[32mvalor\033[m a ser adicionado: ')
            if dadosDICT["Valor"].isnumeric():
                dadosDICT["Valor"] = float(dadosDICT["Valor"])
                break
            print('Dados invalidos!')
        dadosDICT["Horario"] = horas_()
        lista_lucros.append(dadosDICT.copy())
        print(lista_lucros)
        dadosDICT.clear()

#   função para 2
    elif way == '2':
        dadosDICT["Descrição"] = input(f'{vermelhoevidencia_("GASTO")} - Digite uma descrição ao produto : ')
        while True:
            dadosDICT["Valor"] = input('Digite o \033[31mvalor\033[m do produto/serviço: ')
            if dadosDICT["Valor"].isnumeric():
                dadosDICT["Valor"] = float(dadosDICT["Valor"])
                break
            print('Dados invalidos!')
        dadosDICT["Horario"] = horas_()
        lista_gastos.append(dadosDICT.copy())
        print(lista_gastos)
        dadosDICT.clear()

#   função para 3
    elif way == '3':
        clear()

    #   função para lucros
        tlL = 0
        print('\033[32mLUCRO\033[m')
        for i, v in enumerate(lista_lucros):
            print(f'    {i+1}-    {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')
            tlL += v["Valor"]
        print(f'\033[32mO lucro total é de {tlL:.2f}R$!\033[m')

    #   função para Gastos
        tlG = 0
        print(vermelhoevidencia_('GASTOS:'))
        for i, v in enumerate(lista_gastos):
            print(f'    {i+1}-    {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')
            tlG += v["Valor"]
        print(f'\033[31mO GASTO total é de {tlG:.2f}R$!\033[m')

    #   função para total
        tlT = float(tlL) - float(tlG)
        print(f" O lucro diario foi de: {tlT:.2f}R$")
