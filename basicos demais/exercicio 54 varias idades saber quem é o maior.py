from datetime import date

menor = 0
maior = 0
for c in range(0,7):
    ano = int(input("COLOQUE AQUI O SEU ANO DE NASCIMENTO"))

    ##separando ano
    ano_atual = str(date.today()).replace('-',' ')
    ano_atual = ano_atual.split()[0]
    ano_atual = int(ano_atual)

    #resolvendo a logica
    if ano_atual - ano < 21:
        menor = menor + 1
    elif ano_atual - ano >= 21:
        maior = maior + 1

print("Destas 7 pessoas {} delas é maior de idade e {} são menores".format(maior,menor))