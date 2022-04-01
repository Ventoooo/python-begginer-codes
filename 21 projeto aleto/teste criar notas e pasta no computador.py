import os
from datetime import datetime
import pickle


def horas_():
    horario = datetime.now().strftime('%H:%M')
    return horario


def data_():
    datas = datetime.now().strftime('%d_%m_%Y')
    return datas


#   coleta dados do sistema e entra na pasta documents

sistema = os.environ
newway = str(sistema['USERPROFILE']) + r'\Documents'
os.chdir(newway)

#   cria pasta caso não exista
if 'PA' not in os.listdir():
    os.mkdir('./PA')

#   entra na pasta PA
newway = str(sistema['USERPROFILE']) + r'\Documents' + r'\PA'
os.chdir(newway)

# se já existir um txt com a data de hj


#   cria um txt com a data caso n exista
texto = input("Digite uma frase para acrescentar ao arquivo:\n")

arquivo = open(data_() + '.txt', 'w')
arquivo.write(texto + "\n")
print("Operação concluída no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()

print(os.listdir())

print(sistema)