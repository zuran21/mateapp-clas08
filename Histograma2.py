#import numpy as np
import matplotlib.pyplot as plt
#edades de un grupo de personas.
datos = [1,2,3,4,5,6,7,8,9, #10
10,15,16, #3
25,26,27,28,29 #5
,35, #1
45,46,47,48,49, 50,51,52] #8
div= [0,10,20,30,40,50]

inicio  = 0
fin = 50
ancho = 10
#div=np.linspace(inicio, fin,round(1+(fin - inicio )/ancho)) #definimos las diviciones, rounr definimos el munero de elemmentos. 
plt.hist(datos, 5)#definir los datos que se han ingresado.------>numero de bins
plt.grid()#Para agregar cuadricula
plt.show()#para ejecutrar.