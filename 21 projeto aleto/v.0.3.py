from datetime import datetime
import pickle
import os


def horas_():
    horario = datetime.now().strftime('%H:%M')
    return horario


def data_():
    datas = datetime.now().strftime('%d_%m_%Y')
    return datas


def vermelhoevidencia_(x):
    r = f'\033[31m{x}\033[m'
    return r


def clear():
    print("\n" * 130)


dadosDICT = {}
dadosH = str()
lista_pickle = {'lucros': [], 'gastos': []}

#   cria pasta se n existir
if 'PA' not in os.listdir():
    os.mkdir('./PA')

# entra na pasta PA
os.chdir(os.path.dirname(__file__) + '/PA')

#   se já existir um pkl com a data de hj no computador

for c in os.listdir():
    if c == str(data_()) + '.pkl':
        with open(str(data_() + '.pkl'), 'rb') as arquivo:
            lista_pickle = pickle.load(arquivo)
print(lista_pickle)
#   novo codigo
while True:
    input('anyway')

    print('''\n
    0-\033[33mPara adicionar o caixa inicial/Caixa Sicred\033[m
    1-\033[33mPara adicionar os lucros\033[m
    2-\033[33mPara adicionar os gastos\033[m
    3-\033[33mPara consultar os resultados diarios\033[m
    4-\033[33mPara deletar arquivos do sistema\033[m
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
        lista_pickle['lucros'].append(dadosDICT.copy())
        #   salvar dados no pkl
        with open(str(data_()) + ".pkl", "wb") as arquivo:
            pickle.dump(lista_pickle, arquivo)
        #
        print(lista_pickle['lucros'])
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
        lista_pickle['gastos'].append(dadosDICT.copy())
        #   salvar dados no pkl
        with open(str(data_()) + ".pkl", "wb") as arquivo:
            pickle.dump(lista_pickle, arquivo)
    #
        print(lista_pickle['gastos'])
        dadosDICT.clear()

    #   função para 3
    elif way == '3':

        clear()

        #   função para lucros

        tlL = 0

        print('\033[32mLUCRO\033[m')

        for i, v in enumerate(lista_pickle['lucros']):
            print(f'    {i + 1}-    {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')

            tlL += v["Valor"]

        print(f'\033[32mO lucro total é de {tlL:.2f}R$!\033[m')

        #   função para Gastos

        tlG = 0

        print(vermelhoevidencia_('GASTOS:'))

        for i, v in enumerate(lista_pickle['gastos']):
            print(f'    {i + 1}-    {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')

            tlG += v["Valor"]

        print(f'\033[31mO GASTO total é de {tlG:.2f}R$!\033[m')

        #   função para total

        tlT = float(tlL) - float(tlG)

        print(f"\n\033[33mO lucro diario foi de: {tlT:.2f}R$\033[m")
