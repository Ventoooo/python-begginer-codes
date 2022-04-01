data = {'name': str(input('Player name: ')), 'goals': []}
tot = int(input('how many matches do you play ?'))
for c in range(0, tot):
    data['goals'].append(int(input(f"how many goals in match {c}: ")))
data['total'] = sum(data['goals'])
print('~~'*20)
print(data)
print('~~'*20)
for k, v in data.items():
    print(f'the key {k} has {v}')
print('~~'*20)
print(f'the player {data["name"]} played {tot} rounds.')
for c in range(0, tot):
    print(f' =>on match {c}, he did {data["goals"][c]} goal(s).')
#   for i, v in enumerate(data["goals"]) tbm funcionava