import turtle

def anda(tartaruga,passos):
    for i in range(int(passos/2)):
        if (i % 2 == 0):
            tartaruga.penup()
            tartaruga.forward(2)
        else:
            tartaruga.pendown()
            tartaruga.forward(2)

def circulo(tartaruga,tamanho=1):
    for i in range(360):
        tartaruga.forward(tamanho)
        tartaruga.left(1)

def quadradoPontilhado(tartaruga,tamanho = 100, cor = None):
    if (cor == None):
        tartaruga.color("black")
    else:
        tartaruga.color(cor)
    for i in range(1,5):
        anda(tartaruga,tamanho)
        tartaruga.left(90)


bob = turtle.Turtle()
#anda(passos = 100,tartaruga=bob)
#circulo(bob,tamanho = 3)
quadradoPontilhado(bob,200,"pink")
