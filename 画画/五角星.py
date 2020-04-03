import turtle
import time

t = turtle.Turtle()
t.pensize(5)
t.pencolor('yellow')
t.fillcolor('red')

t.begin_fill()
for _ in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()
time.sleep(2)

t.penup()
t.goto(-150, -120)
t.color('violet')
t.write('Done', font=('Arial', 40, 'normal'))

turtle.mainloop()