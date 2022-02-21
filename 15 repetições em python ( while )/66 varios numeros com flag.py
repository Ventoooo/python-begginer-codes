soma = 0
while True:
    print("Para parar digite [ 999 ]")
    num = int(input("coloque um numero: "))
    print(num)
    if num == 999:
        break
    soma += num
print(f"\033[32mA soma foi de {soma}\033[m")