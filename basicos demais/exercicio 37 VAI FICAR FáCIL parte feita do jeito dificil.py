n = int(input(" coloque aqui um numero decimal :"))
n1 = n//16 #primeiro divisor inteiro
if n1 < 16: #finaliza a converção
    print(str(n1)+str(n%16))
else:
    n2 = n1//16 #segundo divisor inteiro
if n2 < 16:  #finaliza a converção

    rn2 = str(n2)
    rn1 = str(n1%16)
    rn = str(n % 16)


    if str(15) == str(n % 16):
        rn = 'F'
    if str(14) == str(n % 16):
        rn = 'E'
    if str(13) == str(n % 16):
        rn = 'D'
    if str(12) == str(n % 16):
        rn = 'C'
    if str(11) == str(n % 16):
        rn = 'B'
    if str(10) == str(n % 16):
        rn = 'A'

    if str(15) == str(n1 % 16):
        rn1 = 'F'
    if str(14) == str(n1 % 16):
        rn1 = 'E'
    if str(13) == str(n1 % 16):
        rn1 = 'D'
    if str(12) == str(n1 % 16):
        rn1 = 'C'
    if str(11) == str(n1 % 16):
        rn1 = 'B'
    if str(10) == str(n1 % 16):
        rn1 = 'A'

    if str(15) == str(n2):
        rn2 = 'F'
    if str(14) == str(n2):
        rn2 = 'E'
    if str(13) == str(n2):
        rn2 = 'D'
    if str(12) == str(n2):
        rn2 = 'C'
    if str(11) == str(n2):
        rn2 = 'B'
    if str(10) == str(n2):
        rn2 = 'A'


    print("{}".format(rn2+rn1+rn))


print("o numero {} em hexadecimal é igual á: {}".format(n,rn2+rn1+rn))

