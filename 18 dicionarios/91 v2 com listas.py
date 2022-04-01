from random import randint
data = []
list_p = []
while True:
    data.append(input(''' "out" to finish
        Name: '''))
    data.append(int(randint(0, 6)))
    if data[0] == 'out':
        print('Result: ')
        break
    elif len(list_p) == 0:
        list_p.append(data[:])
    else:
        if data[1] >= list_p[-1][1]:
            list_p.append(data[:])
        else:
            for i, e in enumerate(list_p):
                if data[1] <= e[1]:
                    list_p.insert(i, data[:])
                    break
    data.clear()
list_p = reversed(list_p)
for i, c in enumerate(list_p):
    print(f"O {i+1}ª lugar foi do \033[32m{c[0]}\033[m com : \033[31m{c[1]}\033[m")
