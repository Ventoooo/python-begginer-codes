inserir = input("coloque aqui o numero/letra/quaquer coisa e vamos te dizer seus tipos : ")
print("é um numero ?", inserir.isnumeric())
print("é uma letra ?", inserir.isalpha())
print("contem letras e numeros ?", inserir.isalnum())
print("é um decimal ?", inserir.isdecimal())
print("é um espaço ?", inserir.isspace())
print("Contem letras maiusculas ?", inserir.isupper())
print("Contem letras minusculas ?", inserir.islower())
#Na verdade o .is serve pra ver se nós podemos transformar algo no que se pede
