import turtle


def draw_star(turtle, lenght):
    """
    Draws star from turtle movements
    :param turtle: turtle to run on the screen
    :param lenght: each line's lenght
    :return:
    """
    for i in range(5):
        yano.forward(lenght)
        yano.left(-144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

yano = turtle.Turtle()
yano.hideturtle()
yano.color("hotpink")
yano.pensize(5)

yano.penup()
yano.left(90)
yano.forward(100)
yano.right(162)
yano.pendown()

for i in range(5):
    draw_star(yano, 100)

    yano.penup()
    yano.forward(350)
    yano.right(144)
    yano.pendown()

wn.mainloop()