s = "abcdefghiklmnopqrs"

lista = []
for letra in s:
    lista.append(letra)
    
print(lista)

lista2 = [letras for letras in s]
print(lista2)

lista3 = [x**2 for x in range(1,100) if (x%2 ==0)]
print(lista3)

lista4 = [x*y for x in [1,2,3] for y in [4,5,6]]
print(lista4)

lista5 = [0]*10
print(lista5)