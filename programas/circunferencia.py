x = int(input("Informe a coordenada x: "))
y = int(input("Informe a coordenada y: "))
raio = 3
dis =  x**2  + y**2 

if (dis > raio**2):
    print("Fora da circunferencia")
elif (dis == raio**2):
    print("Sob a circunferencia")
else:
    print("Dentro da circunferencia")