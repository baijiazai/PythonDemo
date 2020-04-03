from turtle import Screen, Turtle, mainloop


def tree(turtle, size, step):
    """ turtle 为工具，size 为数的大小，step 为枝长 """
    if size < step:
        turtle.left(30)
        turtle.forward(size)
        turtle.back(size)
        turtle.right(30)
        return
    turtle.left(30)
    turtle.forward(size)
    tree(turtle, size - step, step)

    turtle.right(60)
    tree(turtle, size - step, step)
    turtle.left(60)

    turtle.back(size)
    turtle.right(30)


def main():
    turtle = Turtle()
    turtle.color('black')
    turtle.setheading(60)
    turtle.speed(0)
    tree(turtle, 50, 5)
    return "EVENTLOOP"


if __name__ == "__main__":
    msg = main()
    mainloop()
