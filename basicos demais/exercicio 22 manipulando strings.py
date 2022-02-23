nome = input(" Coloque aqui o seu nome completo :")
#maiusculo e menusculo
print("oi, seu nome maiusculo é :",nome.upper())
print("oi, seu nome maiusculo é :",nome.lower())
#contar sem os espaços
nomenovo = nome.split()
print("seu nome completo tem essa quatidade de caracteres :",len(''.join(nomenovo)))
#quantas letras tem o primeiro nome
print("Seu primeiro nome tem essa quatidade de caracteres :",len(nomenovo[0]))
