media_das_idades = 0
idade_hmaior = 0
mmenor_vinte = 0
nome_mmenor = 0
nome_hvelho = 0

for vezes in range(1, 5):

    print('='*5, vezes, 'ª pessoa ', '='*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    media_das_idades = media_das_idades + idade

#print(sexo in 'm M') não funciona ao contrario!

    if idade_hmaior < idade and sexo in 'M m':
        idade_hmaior = idade
        nome_hvelho = nome
        print('ok')

    if idade < 20 and sexo in 'F f':
        mmenor_vinte += +1
        nome_mmenor = nome

print("A idade media das idades colocadas é de: {}".format(media_das_idades/4))
print("O nome do homem mais velho é {} e a sua idade é de {}".format(nome_hvelho, idade_hmaior))
print("O nome da garota mais nova é {} e sua idade é de {}".format(nome_mmenor, mmenor_vinte))
