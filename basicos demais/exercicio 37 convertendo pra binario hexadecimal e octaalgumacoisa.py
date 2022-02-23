n = int(input("coloque aqui um numero a ser convertido :"))
print("""\033[32mEscolha o seu metodo de conversão:\033[m
   Para Binarios digite: \033[31mBIN\033[m
   Para hexadecimais digite: \033[31mHEX\033[m
   Para Octal digite: \033[31mOCT\033[m""")
escolha = input("\033[32mO que vc deseja ? :").upper()
if escolha == 'BIN':
    binario = format(n,"b")
    print('O seu numero em binario é: ',binario)
if escolha == 'HEX':
    hexagonal = format(n,"x")
    print('O seu numero em hexagonal é: ',hexagonal)
if escolha == 'OCT':
    octagonal = format(n,"o")
    print('O seu numero em octagonal é: ',hexagonal)
#escolha = input(" c")


# bin() hex() oct()
#print('o numero em binario : {2:}'.format(bin(n))
#                           z {2:} pega da segunda casa