import turtle
import time


turtle.speed('fastest')
turtle.color('yellow')
turtle.pensize(2)
for x in range(1000):
    turtle.forward(2 * x)
    turtle.left(90)
turtle.done()