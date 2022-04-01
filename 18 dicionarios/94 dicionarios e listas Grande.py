list_ = []
medium = 0
female_s = []
while True:
    data = {"name": input("Name: "), "age": int(input("Age: "))}

    while True:
        data["sex"] = input("Sex: [M/F]").upper()
        if data["sex"] in "MF":
            break
        print("\033[31m error, try again.\n is allowed only \033[32m[M/F]\033[m\033[31m in this question.\033[m\n")
    while True:
        tok = input("wanna continue [Y/N]?").upper().strip()
        if tok in "YNyn":
            break
        print("\033[31m error, try again.\n is allowed only \033[32m[Y/N]\033[m\033[31m in this question.\033[m\n")

    list_.append(data.copy())

    if data["sex"] == 'F':
        female_s.append(data["name"])

    medium += data["age"]
    data.clear()
    if tok == "N":
        break

print('~~'*20)
print(f'A) altogether we have {len(list_)} peoples registered')
print(f'B) The medium age is {medium/len(list_)}')
print(f'C) the women registered is', end=' ')
for v in female_s:
    print(v, end=' ')
print('.')
print(f'D) list of people that are above the medium:')
for v in list_:
    if v["age"] > medium/len(list_):
        for k, e in v.items():
            print(f'\033[33m    {k} = {e}', end='; ')
        print()
    else:
        print("\033[33m none\033[m")
