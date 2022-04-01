from random import randint
from time import sleep
rank = 1
temp_ = {}
results = {'player1': randint(0, 6), 'player2': randint(0, 6),
           'player3': randint(0, 6), 'player4': randint(0, 6)}
results2 = sorted(results.values(), reverse=True)
print('the values drawn were:')
for k, v in results.items():
    print(f'    {k} has: \033[32m{v}\033[m')
    sleep(0.5)
print('the rank of this players is:')
for c in results2:
    for k, v in results.items():
        if c == v:
            temp_[str(k)] = v
for k, v in temp_.items():
    print(f'{rank}ª- {k} was: \033[32m{v}\033[m')
    rank += 1
    sleep(0.5)
