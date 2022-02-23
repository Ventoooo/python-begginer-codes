n1 = float(input("Coloque aqui a sua primeira nota :"))
n2 = float(input("COloque aqui a sua segunda nota :"))


media = (n1 + n2)/2


if media <= 5.0:
    print("SUA MEDIA É DE", media ,"\nVOCE ESTA REPROVADO, SE ESFORCE MAIS!")
if media > 5.0 and media < 7:
    print("SUA MEDIA É DE", media ,"\nVOCE ESTA DE RECUPERAÇÃO")
if media >= 7.0:
    print("SUA MEDIA É DE", media ,"\nPARABÉNS!, VC PASSOU!")