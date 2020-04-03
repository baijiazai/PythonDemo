import turtle
from datetime import *


# 抬起画笔，向前运动一段距离放下
def Skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()


def mk_hand(name, length):
    # 注册 turtle 形状，建立表针 turtle
    turtle.reset()
    Skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    turtle.end_poly()
    # 返回最后记录的多边形。
    hand_from = turtle.get_poly()
    turtle.register_shape(name, hand_from)


def init():
    global sec_hand, min_hand, hur_hand, printer
    # 重置 turtle 指向北
    turtle.mode('logo')
    # 建立三个表针 turtle 并初始化
    mk_hand('sec_hand', 135)
    mk_hand('min_hand', 125)
    mk_hand('hur_hand', 90)
    sec_hand = turtle.Turtle()
    sec_hand.shape('sec_hand')
    min_hand = turtle.Turtle()
    min_hand.shape('min_hand')
    hur_hand = turtle.Turtle()
    hur_hand.shape('hur_hand')

    for hand in sec_hand, min_hand, hur_hand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    # 建立输出文字 turtle
    printer = turtle.Turtle()
    # 隐藏画笔的形状
    printer.hideturtle()
    printer.penup()


def SetupClock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            Skip(-radius - 20)
            Skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align='center', font=('Courier', 14, 'bold'))
            elif i == 30:
                Skip(25)
                turtle.write(int(i / 5), align='center', font=('Courier', 14, 'bold'))
                Skip(-25)
            elif i == 25 or i == 35:
                Skip(20)
                turtle.write(int(i / 5), align='center', font=('Courier', 14, 'bold'))
                Skip(-20)
            else:
                turtle.write(int(i / 5), align='center', font=('Courier', 14, 'bold'))
            Skip(-radius - 20)
        else:
            turtle.dot(5)
            Skip(-radius)
        turtle.right(6)


def Week(t):
    week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return '%s %d %d' % (y, m, d)


def Tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    sec_hand.setheading(6 * second)
    min_hand.setheading(6 * minute)
    hur_hand.setheading(30 * hour)

    turtle.tracer(False)
    printer.forward(65)
    printer.write(Week(t), align='center', font=('Courier', 14, 'bold'))
    printer.back(130)
    printer.write(Date(t), align='center', font=('Courier', 14, 'bold'))
    printer.home()
    turtle.tracer(True)

    # 100ms后继续调用tick
    turtle.ontimer(Tick, 100)


def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟
    turtle.tracer(False)
    init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()


if __name__ == '__main__':
    main()
