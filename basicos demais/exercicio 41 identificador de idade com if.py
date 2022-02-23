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

###Solução para o problema

if idade <= 9:
    print("Você foi classificado para o grupo dos nadadores \033[32mmirins")
if idade > 9 and idade <= 14:
    print("Você foi classificado para o grupo dos nadadores \033[32minfantis")
if idade > 14 and idade <= 19:
    print("Você foi classificado para o grupo dos nadadores \033[32mJuniores")
if idade > 19 and idade <= 20:
    print("Você foi classificado para o grupo dos nadadores \033[32mSeniors")
if idade > 20 :
    print("Você foi classificado para o grupo dos nadadores \033[32mMestre")

