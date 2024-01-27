#turtle
from turtle import Turtle, Screen

my_screen = Screen()
donatelo = Turtle()
donatelo.color("orange")
donatelo.shape("turtle")
donatelo.forward(40)
donatelo.right(90)
donatelo.forward(40)
donatelo.right(90)
donatelo.forward(40)
donatelo.right(90)
donatelo.forward(400)
donatelo.home()
raph = Turtle()

raph.color("red")
raph.pencolor("blue")
raph.shape("turtle")
raph.penup()
raph.setposition(-120,100)
raph.pendown()

x = 10

while x <= 50:
    raph.circle(x)
    donatelo.circle(x+5)
    x+=10










my_screen.exitonclick()