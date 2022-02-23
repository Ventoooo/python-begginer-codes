from datetime import datetime

data = str(input("Coloque aqui o seu ano de nascimento :")).strip()

########### SEPARAR DATAS DE HJ ##############

datahj = (datetime.today().strftime('%Y-%m-%d'))
datahj2 = datahj.replace('-',' ')
datahj2 = datahj2.split()

dataano = int(datahj2[0])
datames = int(datahj2[1])
datadia = int(datahj2[2])

#seperador de datas perguntadas

if '/' in data:
    ano2 = data.replace('/',' ')
    ano2 = ano2.split()
else:
    ano2 = data.split()
dia = int(ano2[0])
mes = int(ano2[1])
anov = int(ano2[2])

###Calculo da idade

idade = int(anov - dataano)*-1
if datames < mes or datadia < dia:
    idade = idade - 1

### solução final

if (idade - 18) < 0:
    print("Ainda faltam algum tempo para vc se alistar")
if (idade - 18) == 0:
    print("Esta na hora de se alistar")
if ((idade - 18)) > 0:
    print(' Vc esta em divida com o serviço militar \n \033[31m{} ANOS\033[m de atraso !'.format(idade - 18))

