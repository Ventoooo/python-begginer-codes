##retira os espaços dentro da frase
sim = 0

frase = input("coloque aqui a frase que vc deseja analizar").strip().lower()
frase = frase.split()
frase = ''.join(frase)


#variavel com o tamanho da frase

tamanho = len(frase)

#identificador

for b in range(0,tamanho):

    if frase[b] == frase[(tamanho-1)-b]:
        sim = sim + 1
        if sim == tamanho:
            print("É um palindromo!!!")

if sim != tamanho:
    print("Não é um palindromo")


