import pickle

lista = {"gastos": {'sapato': 200, 'bolsa': 20}, "ganhos": {'vadias': 350}}

with open("lista.pkl", "wb") as arquivo:    # "wb" = w = white/ b = bites
    pickle.dump(lista, arquivo) # pickle.dump(objeto, arquivo)
#   ler os arquivos
'''
with open("lista.pkl", "rb") as arquivo:
    pickle.load(arquivo)
'''
