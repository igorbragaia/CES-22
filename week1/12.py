import turtle
import math


wn = turtle.Screen()
wn.bgcolor("lightgreen")

def draw(shape, R, show_begining=False):
    yano = turtle.Turtle()
    yano.shape(shape)
    if show_begining:
        yano.stamp()
    yano.speed(1000)
    yano.hideturtle()
    yano.penup()
    yano.left(90)
    for i in range(12):
        yano.right(30)
        yano.forward(R)
        yano.stamp()
        yano.right(180)
        yano.forward(R)
        yano.left(180)

draw("turtle", 120, show_begining=True)
draw("arrow", 90)


wn.mainloop()