### Inserções

a = int(input("coloque aqui o numero do comprimento da primeira reta :"))
b = int(input("coloque aqui o numero do comprimento da segunda reta :"))
c = int(input("coloque aqui o numero do comprimento da terceira reta :"))

### Metodos finais

if a + b > c and b + c > a and a + c > b:
    print("\033[1:32mCom essas medidas de reta vc Pode fazer um triangulo")
    if a == b == c:
        print("O triangulo formado é equilátero")
    elif a == b or b == c or c == a:
        print("O triangulo formado é isósceles")
    if a != b != c:
        print("O triangulo formado é escaleno")
else:
    print("\033[1:31mCom essas medidas de reta vc NÃO Pode fazer um triangulo")

