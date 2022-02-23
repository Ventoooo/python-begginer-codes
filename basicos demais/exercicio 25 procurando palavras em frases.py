nome = input(" coloque aqui o seu nome completo :")
nomeconf = "silva" in nome
if nomeconf == True:
    print("Vc faz parte da familia silva... Prepare-se pra ser executado")
    print("""disparando em 
    3..
    2...
    1...
    MORRAA!!!""")
else:
    print("Bem vindo",nome.split()[0].title())