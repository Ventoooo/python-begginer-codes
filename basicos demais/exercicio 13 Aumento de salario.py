n = float(input("coloque aqui o salario atual da VITIMA : "))
por = float(input("coloque aqui a porcentagem de aumento que a VITIMA vai receber"))
print("o aumento foi de \033[1;30m {}% \033[m resultando num salario mensal de {:.2f}".format(por,( n / 100 ) * por + n))
#tranquilo
