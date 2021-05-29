import matplotlib.pyplot as plt
#datos////////////////Edades aleatorias////////////////
e = [22,23,25,26,27,28,29,30,31,32,33,34,35,
    70,80,90,91,92,93,94,95,96,97,98,]

bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(e,bins, histtype='bar', rwidth = 0.8, color='blue')

plt.title('Grafico de histograma Ejemplo')
plt.ylabel('y')
plt.xlabel('x')

plt.show()