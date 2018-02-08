lista1 = [1,2,3,4,5,6]
lista2 = ["a","b","c","d"]

lista1.extend(lista2)
    
print(lista1)
print(lista1[6:])
lista1 = lista1[::-1]
print(lista1)