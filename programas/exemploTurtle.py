import turtle

def circulo(tartaruga):
    for i in range(360):
        tartaruga.forward(1)
        tartaruga.left(1)


bob = turtle.Turtle()
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.color("blue")
bob.width(3)

circulo(bob)
