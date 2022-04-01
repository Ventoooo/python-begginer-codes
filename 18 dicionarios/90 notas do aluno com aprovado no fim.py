all_elements = {'Name': str(input('Put the student name: ')), 'Point': float(input('Put the test score: '))}
if all_elements['Point'] >= 7:
    all_elements['Situation'] = '\033[32mApproved\033[m'
else:
    all_elements['Situation'] = '\033[31mreproved\033[m'
for k, v in all_elements.items():
    print(f'{k} is {v}.')
