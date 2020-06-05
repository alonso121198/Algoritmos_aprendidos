
#! /usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt # from pylab import plot,sho
import warnings
warnings.filterwarnings("ignore")




def Feigenbaum(x_n, r):
    return r * x_n * (1 - x_n)



# Fuente https://numpy.org/doc/stable/reference/generated/numpy.arange.html
rango_de_r = np.arange(1,4,0.001) # crea valores de 1 a 4 con pasos de 0.001 

# para tener la precision que queremos 
for i,r in enumerate(rango_de_r):
    rango_de_r[i] = round(r,3)


lista_suprema = []    
fig = plt.figure(figsize=(25,25))    

for r in rango_de_r:
    list_prueba = []
    x_n = 0.5
    list_prueba.append(x_n)
    for i in range(4000-1):
        x_n = Feigenbaum(list_prueba[i],r)
        list_prueba.append(x_n) # se pasa por valor y no por direccion
    print(r)
    lista_suprema.append(list_prueba)
    plt.plot([r]*3000,list_prueba[1000:4000],',b')
    
    
plt.ylabel('x_n')
plt.xlabel('n')
plt.axis([0, 4, 0, 1])  # los ejes limites "x" y "y"
plt.show()        




