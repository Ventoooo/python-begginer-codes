# Manipulando strings

obs: mudei o nome

frase = 'ola meu nome é vento sem acento'
print(frase[4:12])
                        ###dessa forma os cochetes servem pra escolher de onde a frase começa, tbm da pra pular casas
                        # é só colocar mais dois pontos e definir a quatidade. ex : 4:12:2 pulamos duas casas

                                                                    #o padrão sempre será esse  (X:Y:Z) o X mostra o inicio da frase
                                                                    #                                   o Y mostra o fim
                                                                    #                                   o Z mostra a quantidade de casas a ser puladas

print(frase[0])   #só ira mostrar a letra da casa desejada ## = o

frase_ao_contrario = frase[::-1]   =  'inverso da frase'

# Analise

len(frase) # Lê a quantidade de DE TUDO na frase ## = tô compreguiça


frase.count('o') # a função .count serve pra contar a quantidade de caracteres especificos dejados no objeto?(=frase, neste caso) ## = 2
frase.count('o',0,13) # nesse caso ele conta a quantidade de palavras do inicio (,0,13) até o fim que vc definir (,0,13) ## = 1
#                                                                                 ^                                  ^^

frase.find('ola') # função . find serve para encontrar a palvra especificas dentro da frase e dizer em que casa ela começa  ## = 0
frase.find(' palvraquenãotánafrasecomcerteza') # ela te retorna um -1 como resultado
rfind e lfind
'ola' in frase ## = true
    not in
frase.index(x,y) # acha a posição de algo sendo (x) o objeto que vc procura e y a posição que vc quer começar a procurar

frase.replace('ola','lindo') # a função replace serve pra substituir palavras ## = a variavel >>frase<< ficaria = 'lindo meu nome e vento    sem acento'


frase.upper() ## = frase toda em maiusculo  obs: da pra escolher de onde até onde

frase.lower() ## = frase fica toda em menusculo ###################################


frase.capitalize() ## = todos os caracteres pra minusculo e a primeira letra da frase vai ficar em maiusculo

frase.title ## = todos os caracteres pra minusculo e depois vai colocar a primeira letra de cada palavra da frase em maiusculo


frase.strip() ## = remove todos os espaços no começo e no fim da frase

frase.lstrip() ## = remove todos os espaços que estão do lado esquedo fora da frase  (left)

frase.rstrip() ## = remove todos os espaços que estão do lado direito fora da frase  (right)

#Divisão

frase.split() ## vai criar uma lista com cada palavra e cada palavra vai contar como uma letra na lista por exemplo : ola= 0 , meu = 1, nome= 2 etc...

'='.join(frase) #junta tudo com o separador escolhido.

print("""é isso te mais  lijndo
asdsdjkssdlksd olha o que da pra fazer com 3 aspas""")

#Organizar

sorted(frase) #organiza em ordem alfabetica/numerica


#######criar 'listas'

print(f'{"Lista de compras ?":^40}')

print(f'{"X":.<36}', end='')

print(f'{"X":.>4}')

lista[-1] #mostra o ultimo caractere da lista