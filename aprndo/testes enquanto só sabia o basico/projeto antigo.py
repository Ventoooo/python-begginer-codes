r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = r9 = 0
x = int(input(''))
nvl = 0
while nvl <= 9:
	nvl = nvl + 1
	corte = x % 10
	x = (corte - x)/10

	if nvl == 1:
		r1 = corte
	elif nvl == 2:
		r2 = corte
	elif r1 == r2:
		print("ta errado filho da puta")
	elif nvl == 3:
		r3 = corte
	elif r2 == r3:
		print("ta errado filho da puta")
	elif nvl == 4:
		r4 = corte
	elif r3 == r4:
		print("ta errado filho da puta")
	elif nvl == 5:
		r5 = corte
	elif r4 == r5:
		print("ta errado filho da puta")
	elif nvl == 6:
		r6 = corte
	elif r5 == r6:
		print("ta errado filho da puta")
	elif nvl == 7:
		r7 = corte
	elif r6 == r7:
		print("ta errado filho da puta")
	elif nvl == 8:
		r8 = corte
	elif r7 == r8:
		print("ta errado filho da puta")
	elif nvl == 9:
		r9 = corte
	elif r8 == r9:
		print("ta errado filho da puta")
	elif nvl == 10:
		print("Parabéns, tá tudo certo meu chapinha")
