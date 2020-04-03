import turtle

turtle.pensize(2)
turtle.bgcolor('black')
turtle.speed(0)
colors = ['red', 'yellow', 'purple', 'blue']

for x in range(400):
    turtle.forward(2 * x)
    turtle.color(colors[x % 4])
    turtle.left(91)

turtle.done()
