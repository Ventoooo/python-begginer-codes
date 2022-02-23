tamanho = 0
tupla = ('sapato', 'tijolo', 'computador', 'lima', 'loja', 'feliz')
for escada in tupla:
    print('Na palavra:', escada, '\ntemos :', end=' ')
    for cada in range(0, len(tupla[tamanho])):
        if tupla[tamanho][cada] in 'aeiou':
            print(tupla[tamanho][cada], end=' ')
    tamanho += 1
    print('\n')
