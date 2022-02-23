aluno = str()
lista = []
dados = []
limit = str()
while limit != 'S' or 'N':

    lista.append(input("coloque o nome do aluno: "))

    for element in range(1, 3):
        dados.append(int(input(f"coloque aqui a {element}ª nota do aluno: ")))

    lista.append(dados[:])
    lista.append(sum(dados)/2)
    dados.clear()

    limit = str(input('Deseja adicionar mais um elemento ? [S/N]: ')).strip().upper()

    if limit in 'Nn':
        print('Os resultados foram: ')
        break

print('='*20)
print('INC.  Nome      Media')
print('='*20)
for element in range(0, len(lista)//3):
    print(f'{element:<4}  {lista[element*3]:<10}{lista[element*3+2]}')

print('Digite o INC do alunos para ver as suas notas na prova ou digite SAIR para encerrar o programa')

while aluno != 'sair':
    while True:
        aluno = input('digite aqui o INC do aluno: ').lower().strip()
        if aluno.isnumeric() and int(aluno) <= (len(lista)//3):
            aluno = int(aluno)
            break
        elif aluno == 'sair':
            print('Programa encerrado.')
            break
        elif aluno != 'sair' and aluno.isalpha():
            del aluno
        print('caracteres invalidos, tente novamente')

    if aluno is int():
        print(f'as nostas do aluno {lista[aluno*3]} foram:')
        for element in range(0, 2):
            print(lista[aluno * 3 + 1][element])
