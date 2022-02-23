a = int(input("coloque aqui um numero :"))
b = int(input("coloque aqui um numero :"))
c = int(input("coloque aqui um numero :"))
if c >= b and c >= a:
    print("porra, o numero {} é o maior de todos !".format(c))
if b >= c and b >= a:
    print("porra, o numero {} é o maior de todos !".format(b))
if a >= b and b >= c:
    print("porra, o numero {} é o maior de todos !".format(a))
#menores
if c <= b and c <= a:
    print("porra, o numero {} é o menor de todos !".format(c))
if b <= c and b <= a:
    print("porra, o numero {} é o menor de todos !".format(b))
if a <= b and b <= c:
    print("porra, o numero {} é o menor de todos !".format(a))