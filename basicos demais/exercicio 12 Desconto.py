n = int(input("coloque aqui o valor do produto desejado :"))
por = int(input("coloque aqui o valor do desconto desejado :"))
print('o valor do produto com {} de desconto é {:.2f}R$'.format(por,n-(n/100)*por))
