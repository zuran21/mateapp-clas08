import matplotlib.pyplot as plt
# datos/////////////Vacunacion contra covid segun su edad////////////////
#edades//
e = [20,21,22,23,24,25,26,27,28,29,30,31]
#Días de vacunacion
Bins = [50,60,70,80,90,100]
#Grafico
plt.hist(e,Bins, color ='Blue')

#Denominacion de ejes y titulos
plt.title('Vacunacion segun su edad')
plt.ylabel('Edades')
plt.xlabel('Dias de vacunacion')

plt.show()