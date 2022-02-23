vfinanciamento = float(input("Coloque aqui o valor da casa a ser comprada :"))
vsalario = float(input("Coloque aqui o valor do salario do financiador em questão :"))
meses = (int(input("coloque aqui a quantidade de anos em que o financiador planeja pagar :"))*12)
#vfinanciamento = 20000
#vsalario = 1000
#meses = 60
print(""" O valor da prestação será de {:.2f} 
      
      """.format(vfinanciamento/meses))
if (vfinanciamento/meses) < (vsalario/100*30):
    print("\033[32mAs condições para o financiamento foram aceitas!")
    print(meses)
else:
    print("\033[31mInfelizmente as condições para o financiamento não foram aceitas\nTenha uma boa tarde!!")