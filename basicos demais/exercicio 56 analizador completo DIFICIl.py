media_idades = 0
homem_velho = 0
mulher_menos = 0
nomehvelho = 0

for c in range(0, 4):

    nome = input("Coloque aqui o seu nome :").strip().capitalize()
    idade = int(input("coloque aqui a sua idade :"))
    uiuisexo = input("coloque aqui o seu sexo :").lower()

    media_idades = media_idades + idade

    if uiuisexo == 'm' and idade > homem_velho or uiuisexo == 'masculino' and idade > homem_velho or uiuisexo == 'homem' and idade > homem_velho:
        homem_velho = idade
        nomehvelho = nome

    elif idade < 20 and uiuisexo == 'feminino' or idade < 20 and uiuisexo == 'f' or idade < 20 and uiuisexo == 'mulher':
        mulher_menos = mulher_menos + 1

    if uiuisexo != 'm' or 'f' or 'masculino' or 'feminino' or 'homem' or 'mulher':
        print('caracteres invalidos')
        break


print("""A MEDIA DAS IDADES É DE: {}
O NOME DO HOMEM MAIS VELHO É: {}
A QUANTIDADE DE MULHERES MENORES DE 20 ANOS É DE: {}""".format(media_idades/4, nomehvelho, mulher_menos))

#nem foi tão dificil
