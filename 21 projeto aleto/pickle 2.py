import pickle

arquivo = open('lista.pkl', 'rb')
lista = pickle.load(arquivo)
print(lista)