import random
lvl = True
x = input(" 1 nome dos alunos")
y = input("2 nome dos alunos")
u = input(" 3nome dos alunos")
t = input(" 4nome dos alunos")
#while lvl == True:
grupos = [x, y, u, t]
#print(random.shuffle( grupos ))
#proximos = ([x, y, u, t] - grupos)
gruposseq = random.sample(grupos, 4)
print("o primeiro grupo é :", gruposseq[0])
print("o segundo grupo é :", gruposseq[1])
print("o terceiro é :", gruposseq[2])
print("o ultimo grupo é :", gruposseq[3])
