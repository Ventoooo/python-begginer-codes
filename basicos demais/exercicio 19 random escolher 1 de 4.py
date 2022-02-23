import random
a = input("coloque aqui o nome do primeiro aluno :")
b = input("coloque aqui o nome do segundo alundo :")
c = input("coloque aqui o nome do terceiro aluno :")
d = input("coloque aqui o nome do quarto alundo :")
valores = [a,b,c,d]
print("O VERDADEIRO ESCOLHIDO FOI ?", random.choice(valores))