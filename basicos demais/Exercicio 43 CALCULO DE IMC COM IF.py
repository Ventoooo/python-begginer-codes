altura = float(input("Coloque aqui a sua altura :"))
peso = float(input("coloque aqui o seu peso :"))
imc = peso / (altura * altura)

###possiveis erros





###Solução final
if imc < 18.5:
    print("O seu IMC é de: {:.2f}".format(imc))
    print("\033[31mVocê esta abaixo do peso!")
if imc >= 18.5 and imc <= 25:
    print("O seu IMC é de: {:.2f}".format(imc))
    print("\033[32mVocê esta no peso ideal!")
if imc >= 25 and imc <= 30:
    print("O seu IMC é de: {:.2f}".format(imc))
    print("\033[33mVocê esta com sobrepeso!")
if imc >= 30 and imc <= 40:
    print("O seu IMC é de: {:.2f}".format(imc))
    print("\033[1:31mVocê esta \033[31mOBESO!")
if imc > 40:
    print("O seu IMC é de: {:.2f}".format(imc))
    print("\033[1:31mVocê esta com obesidade morbida!")


