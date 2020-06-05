
#! /usr/bin/python3
from numpy import *
import matplotlib.pyplot as plt # from pylab import plot,sho
import warnings
warnings.filterwarnings("ignore")



# Puedo crear una funcion recursiva pero debido a que se pide 1000 iteraciones
# y se necesita los 100 elementos . No me conviene
def Feigenbaum(x_n, r):
    return r * x_n * (1 - x_n)


lista1 = [0] * 1000  # Crea una lista de 1000 elemnentos(lista mutable)
lista2 = [0] * 1000
lista3 = [0] * 1000
for i, x_n1 in enumerate(lista1):
    if i == 0:
        x_n1 = 0.45  # caso base
    else:
        x_n1 = Feigenbaum(lista1[i - 1], 1)

    lista1[i] = x_n1

for i, x_n1 in enumerate(lista2):
    if i == 0:
        x_n1 = 0.5  # caso base
    else:
        x_n1 = Feigenbaum(lista2[i - 1], 1)

    lista2[i] = x_n1

for i, x_n1 in enumerate(lista3):
    if i == 0:
        x_n1 = 0.55  # caso base
    else:
        x_n1 = Feigenbaum(lista3[i - 1], 1)

    lista3[i] = x_n1

'''
# Fuente https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
',' : Marcador de pixel
'''
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(25, 25))
grafico = plt.plot(range(0, 1000), lista1, ',b', range(0, 1000), lista2, 'o-', range(0, 1000), lista3, 'o')
plt.ylabel('x_n')
plt.xlabel('n')
plt.axis([0, 1000, 0, 0.05])  # los ejes limites "x" y "y"
plt.show()