from turtle import *


x = 360 / 10
y = 120
for i in range(10):
    if i % 2 == 0:
        color('skyblue')
    else:
        color('pink')
    begin_fill()
    forward(y)
    left(x)
    forward(y)
    left(180 - x)
    forward(y)
    left(x)
    forward(y)
    left(180 - x)
    end_fill()
    left(x)
done()
    