from random import randint
list_p = list()
data = dict()
quant = int(input("which is the amount of players: "))
for c in range(0, quant):
    data["Player" + str(c+1)] = randint(0, 6)
list_p = data.copy().items()
print(list_p)
list_p = sorted(list_p, key=lambda a: a[1], reverse=True)
print('\nValues:')
for k, v in data.items():
    print(f'    {k} has: {v}')
print('\nRanking:')
for k, v in list_p:
    print(f"    {k} with: {v}")
