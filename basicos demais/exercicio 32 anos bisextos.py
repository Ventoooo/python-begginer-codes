from datetime import date
ano = int(input("coloque aqui o ano que vc acha ser bisexto :"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano%100 != 0 or ano%400 == 0:
    print("\033[4;31;40mEste ano de {} definitivamente é bisexto!\033[m".format(ano))
else:
    print("\033[7;40mEsse ano de {} não é bisexto\033[m".format(ano))