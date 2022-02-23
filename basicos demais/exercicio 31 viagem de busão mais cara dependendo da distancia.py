km = float(input("coloque aqui a kilometragem total da sua viagem e calcularemos o valor !"))
if km > 200:
    print("sua viagem ira custar {:.2f}".format(km*0.45))
else:
    print("sua viagem ira custar {:.2f}".format(km*0.50))