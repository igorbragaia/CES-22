import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")

R = 150

yano = turtle.Turtle()
yano.shape("turtle")

# centering yano
yano.penup()
yano.hideturtle()
yano.left(90)
yano.forward(150)
yano.left(-180)
yano.right(18)
yano.pendown()

for i in range(5):
    yano.forward(2 * R * math.cos(math.pi / 10))
    yano.left(144)

wn.mainloop()