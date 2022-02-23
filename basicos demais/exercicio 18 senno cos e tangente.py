import math
an = math.radians(int(input("coloque aqui o valor do angulo desejado :")))
cos = math.cos(an)
tang = math.sin(an)
seno = math.tan(an)
print(" Seno do angulo é igual á {:.3f} \n Cos é igual á {:.3f}\n Tang é igual á {:.3f}".format(seno,cos,tang))