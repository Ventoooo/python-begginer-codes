from datetime import datetime
import pickle
import os

dadosDICT = {}
dadosH = str()
lista_pickle = {'lucros': [], 'gastos': [], 'lista_caixas': {}}


def horas_():
    horario = datetime.now().strftime('%H:%M')
    return horario


def data_():
    datas = datetime.now().strftime('%d_%m_%Y')
    return datas


def clear():
    print("\n" * 130)


def save_data():
    templ = tempg = 0
    with open(str(data_()) + '.txt', 'w') as historico:

        historico.write(f"Caixa inicial : {lista_pickle['lista_caixas']['caixa_inicial']:.2f}R$\n")
        historico.write(f"Caixa sicred : {lista_pickle['lista_caixas']['caixa_sicred']:.2f}R$\n\n")

        historico.write("LUCROS:\n\n")
        for posi, element in enumerate(lista_pickle['lucros']):
            templ += element["Valor"]
        for posi, element in enumerate(lista_pickle['lucros']):
            a = f'{posi + 1}-    {element["Descrição"]} ===> {element["Valor"]:.2f}R$ as {element["Horario"]}Hs. \n'
            historico.write(str(a))
        historico.write(f'\n            Os LUCROS totais foram de {templ:.2f}R$!\n')

        historico.write("\nGASTOS:\n\n")
        for posi, element in enumerate(lista_pickle['gastos']):
            b = f'{posi + 1}-    {element["Descrição"]} ===> {element["Valor"]:.2f}R$ as {element["Horario"]}Hs. \n'
            historico.write(str(b))
        for posi, element in enumerate(lista_pickle['gastos']):
            tempg += element["Valor"]
        historico.write(f'\n            Os GASTOS totais foram de -{tempg:.2f}R$!\n')

        tempt = float(templ) - float(tempg)
        historico.write(f"\nO lucro diario foi de: {tempt:.2f}R$\n")
        historico.write(f"O valor total dos caixas mais o lucro diário deve ser de: "
                        f"{lista_pickle['lista_caixas']['caixa_sicred']+lista_pickle['lista_caixas']['caixa_inicial']+ tempt:.2f}R$")

        with open(str(data_()) + ".pkl", "wb") as arquivopk:
            pickle.dump(lista_pickle, arquivopk)


#   cria pasta se n existir
if 'PA' not in os.listdir():
    os.mkdir('watchudu/compilar/PA')

# entra na pasta PA
os.chdir('watchudu/compilar/PA')

#   se já existir um pkl com a data de hj no computador carrega os dados

for c in os.listdir():
    if c == str(data_()) + '.pkl':
        with open(str(data_() + '.pkl'), 'rb') as arquivo:
            lista_pickle = pickle.load(arquivo)


#   função para 0
if len(lista_pickle['lista_caixas']) == 0:
    while True:
        dadosH = input('Caixa inicial = ').strip()
        #   confere se o codigo só tem numeros/floats
        if '.' in dadosH:
            validador = dadosH.replace('.', '')
            if validador.isnumeric():
                dadosH = float(dadosH)
                lista_pickle["lista_caixas"]["caixa_sicred"] = dadosH
                break
        elif dadosH.isnumeric():
            dadosH = float(dadosH)
            lista_pickle["lista_caixas"]["caixa_inicial"] = dadosH
            break
        print('Dados invalidos!')

    while True:
        dadosH = input('Caixa Sicred = ')
        if '.' in dadosH:
            validador = dadosH.replace('.', '')
            if validador.isnumeric():
                dadosH = float(dadosH)
                lista_pickle["lista_caixas"]["caixa_sicred"] = dadosH
                break
        elif dadosH.isnumeric():
            dadosH = float(dadosH)
            lista_pickle["lista_caixas"]["caixa_sicred"] = dadosH
            break
        print('Dados invalidos!')
    save_data()

#   novo codigo
while True:
    input('\nenter to continue: ')
    clear()
    print('''\n
    0-  Para mudar o caixa inicial/Caixa Sicred
    1-  Para adicionar os lucros
    2-  Para adicionar os gastos
    3-  Para consultar os resultados diarios
    4-  Para deletar arquivos do sistema
    5-  Para Finalizar
        ''')

    while True:
        way = input('Escolha o numero de uma das opções para prosseguir:').strip()
        if way.isnumeric():
            if int(way) <= 5 or 666:
                break
        print('Caracteres invalidos!')
    clear()

#   função para 0
    if way == '0':
        while True:
            dadosH = input('Caixa inicial = ').strip()
            #   confere se o codigo só tem numeros/floats
            if '.' in dadosH:
                validador = dadosH.replace('.', '')
                if validador.isnumeric():
                    dadosH = float(dadosH)
                    lista_pickle["lista_caixas"]["caixa_sicred"] = dadosH
                    break
            elif dadosH.isnumeric():
                dadosH = float(dadosH)
                lista_pickle["lista_caixas"]["caixa_inicial"] = dadosH
                break
            print('Dados invalidos!')

        while True:
            dadosH = input('Caixa Sicred = ').strip()
            if '.' in dadosH:
                validador = dadosH.replace('.', '')
                if validador.isnumeric():
                    dadosH = float(dadosH)
                    lista_pickle["lista_caixas"]["caixa_sicred"] = dadosH
                    break
            elif dadosH.isnumeric():
                dadosH = float(dadosH)
                lista_pickle["lista_caixas"]["caixa_sicred"] = dadosH
                break
            print('Dados invalidos!')
        save_data()

    #   função para 1
    elif way == '1':
        dadosDICT["Descrição"] = input(f'LUCROS-   Digite uma [DESCRIÇÃO] para o produto: ').strip()
        while True:
            dadosDICT["Valor"] = input('Digite o [VALOR] do produto/serviço: ').strip()
            if '.' in dadosDICT["Valor"]:
                validador = dadosDICT["Valor"].replace('.', '')
                if validador.isnumeric():
                    dadosDICT["Valor"] = float(dadosDICT["Valor"])
                    print(f'\nLUCROS-     Valor de ==>{dadosDICT["Descrição"]}<== adicionado com sucesso !')
                    break
            if dadosDICT["Valor"].isnumeric():
                dadosDICT["Valor"] = float(dadosDICT["Valor"])
                print(f'\nLUCROS-     Valor de ==>{dadosDICT["Descrição"]}<== adicionado com sucesso !')
                break
            print('Dados invalidos!')

        dadosDICT["Horario"] = horas_()
        lista_pickle['lucros'].append(dadosDICT.copy())
        #   salvar dados no pkl
        save_data()
        #
        dadosDICT.clear()

    #   função para 2
    elif way == '2':
        dadosDICT["Descrição"] = input(f'GASTOS-    Digite uma [DESCRIÇÃO] para o produto : ').strip()
        while True:
            dadosDICT["Valor"] = input('Digite o [VALOR] do produto/serviço: ').strip()
            if '.' in dadosDICT["Valor"]:
                validador = dadosDICT["Valor"].replace('.', '')
                if validador.isnumeric():
                    dadosDICT["Valor"] = float(dadosDICT["Valor"])
                    print(f'\nLUCROS-     Valor de ==>{dadosDICT["Descrição"]}<== adicionado com sucesso !')
                    break
            if dadosDICT["Valor"].isnumeric():
                dadosDICT["Valor"] = float(dadosDICT["Valor"])
                print(f'\nValores de ==>{dadosDICT["Descrição"]}<== adicionado com sucesso !')
                break
            print('Dados invalidos!')
        dadosDICT["Horario"] = horas_()
        lista_pickle['gastos'].append(dadosDICT.copy())
        #   salvar dados no pkl
        save_data()
        #
        dadosDICT.clear()

    #   função para 3
    elif way == '3':

        #   função para caixas

        print(f'Caixa inicial: {lista_pickle["lista_caixas"]["caixa_sicred"]:.2f}R$')
        print(f"Caixa sicred: {lista_pickle['lista_caixas']['caixa_inicial']:.2f}R$\n")
        #   função para lucros
        tlL = 0

        print('LUCROS:')
        for i, v in enumerate(lista_pickle['lucros']):
            print(f'    {i + 1}- {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')
            tlL += v["Valor"]
        print(f'\n            Os lucros totais foram de {tlL:.2f}R$!\n')

        #   função para Gastos

        tlG = 0

        print('GASTOS:')
        for i, v in enumerate(lista_pickle['gastos']):
            print(f'    {i + 1}- {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')
            tlG += v["Valor"]
        print(f'\n            OS GASTOS totais foram de -{tlG:.2f}R$!')

        #   função para total

        tlT = float(tlL) - float(tlG)
        print(f"\nO lucro diario foi de: {tlT:.2f}R$")
        print((f"O valor total da soma dos caixas mais o lucro diário deve ser de: "
               f"{lista_pickle['lista_caixas']['caixa_sicred']+lista_pickle['lista_caixas']['caixa_inicial']+ tlT:.2f}R$"))

        #   historico em txt
        save_data()

    elif way == '4':

        #   função para lucros

        print('LUCROS: ')
        for i, v in enumerate(lista_pickle['lucros']):
            print(f'    {i + 1}-    {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')

        #   função para Gastos

        print('GASTOS: ')
        for i, v in enumerate(lista_pickle['gastos']):
            print(f'    {i + 1}-    {v["Descrição"]} ===> {v["Valor"]:.2f}R$ as {v["Horario"]}Hs.')

        # way
        print('''\n\n\nO valor a ser deletado é um :
    0- GASTOS
    1- LUCROS''')
        del_way = str(input('>: ')).strip().upper()
        if del_way == '0':
            while True:
                dadosH = input('coloque o indice do valor que será apagado: ')
                if dadosH.isnumeric and dadosH != '0':
                    if int(dadosH) <= len(lista_pickle['gastos']):
                        del lista_pickle['gastos'][int(dadosH) - 1]
                        print(f"\nO valor de indice ==>{dadosH}<== foi removido com sucesso!")
                        del dadosH
                        break
                print('Dados invalidos, tente novamente!')
        if del_way == '1':
            while True:
                dadosH = input('coloque o indice do valor que será apagado: ')
                if dadosH.isnumeric and dadosH != '0':
                    if int(dadosH) <= len(lista_pickle['lucros']):
                        del lista_pickle['lucros'][int(dadosH) - 1]
                        print(f"\nO valor de indice ==>{dadosH}<== foi removido com sucesso!")
                        del dadosH
                        break
                print('Dados invalidos, tente novamente!')
        #   salvar dados no pkl
        save_data()
        #
    elif way == '5':
        print("Programa finalizado!")
        save_data()
        break

    elif way == '666':
        print("Obrigado por tudo cara, eu te amo!\nVamo viajar quando eu ficar rico")
        print("Sério pra compilar isso foi UM COMPLETO INFERNO por isso o 666.")
        print('E o pior, tudo isso foi por causa de 1 única linha de gambiarra... Mas agr tá tudo certo e é isso que '
              'importa!')
        print("Até mais cara, bom dia, boa noite, boa tarde, bom descanço, durma bem, tenha bons sonhos e tudo mais")
        print("Beijão!!!")
        print("\n esse foi o meu ultimo codigo .py antes de começar a facul ent se eu n estiver falando inglês até o "
              "fim desse ano eu peço que me encha de porrada! \n de leve pfvr.")
