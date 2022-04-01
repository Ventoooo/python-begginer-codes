print("\n")

c = []
'''
texto = input("Digite uma frase para acrescentar ao arquivo:\n")
arquivo = open('arq01.txt', 'a')
arquivo.write(texto + "\n")
print("Operação concluída no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
arquivo.close()
'''

print("\nTexto alterado:")
arquivo = open('arq01.txt', 'r')
for linha, valores in enumerate(arquivo):
    valores = valores.rstrip()
    c.append(dict(valores))
print(c)
arquivo.close()

for i, e in enumerate(c):
    print(i, e)
