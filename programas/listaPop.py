import random

lista = []
for i in range(100):
    x = random.randint(1,100)
    lista.append(x)
    
print(lista)
x = lista.pop()
print("Elemento removido: ",x)
print("Lista agora:",lista)

y = lista.pop(0)
print("Elemento removido:",y)
print("Lista agora:",lista)

lista[1] = ["a","b","c"]
print(lista)