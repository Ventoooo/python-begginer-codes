sexo = str(input("digite o seu sexo: [M/F]")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("caracteres invalidos, digite o seu sexo novamente: ")).strip().upper()[0]
print("Dados guardados com sucesso")