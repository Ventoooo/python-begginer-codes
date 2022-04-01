import os
sistema = os.environ
#   print(sistema)
#   print(sistema['USERNAME'])
print(os.getcwd())
novo_caminho = r'C:\Users\fastf\Documents'
os.chdir(novo_caminho)

print(os.listdir())
