salario = float(input("coloque aqui o valor do seu salário atual :"))
if salario > 1250:
    print("o aumento no seu salario foi de {:.2f} o valor mensal recebido agr será de {:.2f}".format(salario/100*10,salario/100*10+salario))
else:
    print("o aumento no seu salario foi de {:.2f} o valor mensal recebido agr será de {:.2f}".format(salario/100*15,salario/100*15+salario))