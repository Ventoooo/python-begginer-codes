n = int(input("coloque aqui o numero que vc quer ver a tabuada :"))
mut = 1
lvl = 1
print("="*37)
while lvl != 11:
    lvl = lvl + 1
    print("{} mutiplicado por {:3} é igual a = {:1}".format(n, mut, n*mut))
    mut = mut + 1
print("="*37)
