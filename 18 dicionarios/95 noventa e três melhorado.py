list_p = []
data = {}
data_g = str()
while True:
    data['name'] = str(input("\nPlayer name: "))

    while True:
        tot = input(f"how many matches {data['name']} has played: ")
        if tot.isnumeric():
            tot = int(tot)
            break
        print('\033[31mError! please put only characters numerics\033[m')

    data['goals'] = []
    for c in range(0, tot):
        while True:
            data_g = input(f"how many goals he did on game {c+1}: ")
            if data_g.isnumeric():
                data['goals'].append(int(data_g))
                break
            print('\033[31mError! Please put only characters numerics\033[m')

    list_p.append(data.copy())
    data.clear()

    while True:
        token = str(input('You want to continue? [Y/N]')).strip().upper()
        if token == 'N' or token == 'Y':
            break
        print('\033[31mError! Please put \033[32m-Y-\033[31m to -continue- or \033[32m-N-\033[31m to stop\033[m')
    if token == 'N':
        break

print('\n', '~'*50)
print(f'{"COD":<5}{"NAME":<13}{"GOALS":<20}{"TOTAL":>12}')
print('-'*50)
for i, v in enumerate(list_p):
    print(f'{i:<5}{v["name"]:<13}{str(v["goals"]):<20}{str(sum(v["goals"])):>12}')

while True:
    while True:
        token = input('\nto show the data select the \033[32mCOD\033[m [ -out- tô exit]:').strip().upper()
        if token.isnumeric():
            token = int(token)
            break
        elif token == "OUT":
            break
        print('\033[31mError! Please put only characters numerics\033[m')
    if token == "OUT":
        print('>= Program closed =<')
        break
    print(f'\n{list_p[token]["name"]} player data: ')
    for i, c in enumerate(list_p[token]["goals"]):
        print(f'    -in the {i+1} game he did {c} goals.')
