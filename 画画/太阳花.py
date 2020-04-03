import turtle
import time

t = turtle.Turtle()
t.color('red', 'yellow')
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)
t.end_fill()
turtle.mainloop()
