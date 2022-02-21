valortotal = caros1000 = menor_preço = nivelador = 0
while True:

    if nivelador == 0:
        nome_produto = input('Nome do produto: ')
        if nome_produto.isalpha():
            nivelador = 1
        else:
            print(' caracteres invalidos digite novamente o nome do produto')

    if nivelador == 1:
        preço = input('Preço do produto: ')
        if preço.isnumeric():
            nivelador = 2
            preço = float(preço)
        else:
            print(' caracteres invalidos digite novamente o nome do produto')

    if nivelador == 2:

        if menor_preço == 0:
            menor_preço = preço
            nome_menor = nome_produto
        if preço < menor_preço:
            menor_preço = preço
            nome_menor = nome_produto

        if preço > 1000:
            caros1000 += 1

        valortotal += preço

        continua = input("Você deseja adicionar mais produtos ? : ").upper()

        if continua in 'NNÃO':
            print(f'''
O valor total foi de \033[31m{valortotal}\033[m
Você comprou \033[31m{caros1000}\033[m produtos com valor acima dos 1000R$
O produto mais barato que você comprou foi \033[31m{nome_menor}\033[m''')
            break

        elif continua in 'SSIM':
            nivelador = 0
        else:
            print('Caracteres invalidos favor digitar novamente')