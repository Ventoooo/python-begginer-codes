from random import choice
from time import sleep

###apresentação

print("""SUAS AÇOES:
[ \033[33mPEDRA\033[m ]
[ \033[33mPAPEL\033[m ]
[ \033[33mTESOURA\033[m ]""")

escolha = input(" Escolha uma forma para jogar contra o computador :").lower()
escolhac = choice(['pedra', 'papel', 'tesoura'])

print("pedra...")
sleep(0.5)
print("papel...")
sleep(0.5)
print("tesoura!!!")

print("-=-"*12)
print("O Computador jogou ",escolhac)
print("O Computador jogou ",escolha)
print("-=-"*12)

if escolha == 'papel' and escolhac == 'pedra':
    print("""PEDRA!!!!""")
    sleep(1)
    print("....")
    sleep(1)
    print("ops, vc venceu...""")


if escolha == 'tesoura' and escolhac == 'papel':
    print("""PAPEL!!!!""")
    sleep(1)
    print("....")
    sleep(1)
    print("ops, vc venceu...""")


if escolha == 'pedra' and escolhac == 'tesoura':
    print("""TESOURA!!!!""")
    sleep(1)
    print("....")
    sleep(1)
    print("ops, vc venceu...""")



if escolhac == 'papel' and escolha == 'pedra':
    print("""PAPEL!!!!""")
    sleep(1)
    print("....")
    sleep(1)
    print("VENCI!!!""")



if escolhac == 'tesoura' and escolha == 'papel':
    print("""TESOURA!!!!""")
    sleep(1)
    print("....")
    sleep(1)
    print("VENCI!!!!")



if escolhac == 'pedra' and escolha == 'tesoura':
    print("""PEDRA!!!!""")
    sleep(1)
    print("....")
    sleep(1)
    print("VENCI!!!...")


if escolhac == escolha:
    print("empate, vamos novamente!")
    sleep(1)


#if escolha != ('papel' or 'tesoura' or 'pedra'):
    #print("Vôce realmente deseja sair ? Y/N")
    #out = input("").upper().strip()
    #if out == 'N':
        #escolha =1000
        #print("Você saiu!")