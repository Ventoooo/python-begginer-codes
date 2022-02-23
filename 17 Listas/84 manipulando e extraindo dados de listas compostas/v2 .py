_list = list()
_max = _min = 0
bridge = []
high = []
while True:
    bridge.append(input('white the client name on here: '))
    bridge.append(int(input('white the weight of your client: ')))
    if _list == list():
        _max = _min = bridge[1]
    elif _max < bridge[1]:
        _max = bridge[1]
    elif _min > bridge[1]:
        _min = bridge[1]
    _list.append(bridge[:])
    bridge.clear()
    finisher = input("when you want to get out -TYPE OUT- or -PRESS ENTER- to continue: ").strip().upper()
    if finisher == 'OUT':
        break
for element in range(0, len(_list)):
    if _list[element][1] == _max:
        high.append(_list[element][0])
    if _list[element][1] == _min:
        bridge.append(_list[element][0])

print(f'''the amount of people indexed was {len(_list)}
the maximum weight was {_max} and the name of this persons is:
{high}
the minimum weight was {_min} and the names of this persons is:
{bridge}''')
