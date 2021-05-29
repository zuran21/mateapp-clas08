import matplotlib as plt
import numpy as np
costo=[]#variable dependiente y
cambio_de_aceite=[]#variable independiente x

with open ("datos.csv", encoding= 'uft-8', newline='' ) as f:
#reader -csv.reader(F)
reader = enumerate(csv.reader(f))

for i, now in reader:
    if i>0:
        try:
            costo.append(int(now[0]))
            cambio_de_aceite.append(int(now[1]))
        except exception:
            Print(exception)

            #plt.scatter(cambio_de_aceite,costo,c="g", alpha=0.5,marker=r'$/clubsuit$ , label="luck", s=100)
            plt.scatter(cambio_de_aceite,costo,c="g", alpha=0.5,s=100)
            plt.xlabel("cambio de aceite")
            plt.ylabel("costo")
            plt.show()