place = str(input("coloque aqui o nome da sua cidade :")).title().strip()
dev2 = place.find("Santo")
if dev2 >= 0:
    print("vôce mora numa cidade proxima")
else:
    print("infelizmente não podemos te contratar")
