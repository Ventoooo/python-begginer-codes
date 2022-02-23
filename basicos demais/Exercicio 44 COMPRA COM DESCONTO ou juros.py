from time import sleep

valor = int(input("Coloque o valor do produto :"))

###Apresentação

print(""" Escolha o metodo de pagamento:
 \033[32mA vista/cheque: 10% OFF
 Debito : \033[32m 5% OFF
 Em até duas vezes: \033[32m SEM JUROS
 Em três ou mais vezes: \033[32m 20% de juros\033[m""")

###mediador

print(' ')
sleep(1)

###Metodo de escolha

escolha = input(""" Escolha o metodo de pagamento:
Escreva \033[31mDIN\033[m Para a opção de dinheiro/cheque
Escreva \033[31mDE\033[m Para a opção de débito
Escreva \033[31m2X\033[m Para a opção de duas vezes no cartão
Escreva \033[31mPAR\033[m Para a opção de Parcelado

: """).upper()

if escolha == 'DIN':
    print("O valor a ser pago será de {:.2f}".format((valor/100*10-valor)*-1))
elif escolha == 'DE':
    print("O valor a ser pago será de {:.2f}".format((valor/100*5-valor)*-1))
elif escolha == '2X':
    print("O valor a ser pago será de {:.2f}".format((valor)))
elif escolha == 'PAR':
    print("O valor a ser pago será de {:.2f}".format((valor/100*20+valor)))
else:
    print("Opção invalida de pagamento !")
