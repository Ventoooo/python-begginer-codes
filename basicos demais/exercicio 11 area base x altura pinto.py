n1 = float(input("digite aqui a altura da parede que vc quer pintar :"))
n2 = float(input("digite aqui a largura da parede retangular que você quer pintar :"))
p = float(input("1 litro de tinta pinta quantos metros quadrados de parede :"))
print("sabendo que 1 L de tinta pinta {}M quadrados da parede e que sua parede tem {} de area, vamos precisa de {} Litros de tinta para pintar toda a parede".format(p, n1*n2, n1*n2/p))
#acertei de primeira não sei nem como.