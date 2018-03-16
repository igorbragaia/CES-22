import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")

R = 150

yano = turtle.Turtle()
yano.shape("turtle")

# centering yano
yano.hideturtle()
yano.left(90)
yano.forward(150)
yano.left(-90)

yano.clear()
yano.showturtle()

yano.left(-90)
yano.right(18)
yano.showturtle()

while True:
    yano.forward(2 * R * math.cos(math.pi / 10))
    yano.left(180 - 36)

wn.mainloop()