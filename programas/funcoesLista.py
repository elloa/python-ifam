import random
import numpy as np # depende da pre-instalacao do Anaconda
                   # conda install numpy
                   
''' um comentario
grande
ocupando varias 
linhas '''

lista = []
for i in range(100):
    x = random.randint(1,100)
    lista.append(x)
    
print(lista)

print(13 in lista)
print(len(lista))

print(sum(lista))
print(max(lista))
print(min(lista))
print(np.sum(lista))
print(np.std(lista))