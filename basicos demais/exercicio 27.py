nome = input("coloque aqui o seu nome :").strip().title()
last = len(nome.split())
print("o seu primeiro nome é {} \nO seu ultimo nome é {}".format(nome.split()[0],nome.split()[last-1]))

#print(nome.split()[last])
#print(nome.split()[2])