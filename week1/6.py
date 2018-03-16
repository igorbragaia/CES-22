import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")


for format in [3, 4, 6, 8]:
    yano = turtle.Turtle()
    yano.shape("turtle")
    yano.forward(50)
    for loops in range(2):
        for i in range(format):
            yano.left(360 / format)
            yano.forward(50)
    yano.clear()
    yano.hideturtle()
