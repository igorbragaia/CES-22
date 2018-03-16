import turtle
import math

def move(pair):
    """
    moves yano turtle length forward rotating a determined angle
    :param pair: (angle, lenght)
    :return:
    """
    angle = pair[0]
    lenght = pair[1]
    yano.left(angle)
    yano.forward(lenght)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
yano = turtle.Turtle()
yano.pendown()
yano.pensize(5)


R = 100
movements = [
    (0, 100), (315, 50 * math.sqrt(2)), (270, 50 * math.sqrt(2)), (225, 100), (45, 50 * math.sqrt(2)),
    (90, 50 * math.sqrt(2)), (90, 100 * math.sqrt(2)), (225, 100), (315, 50 * math.sqrt(2)),
    (270, 50 * math.sqrt(2)), (225, 100), (135, 100 * math.sqrt(2))
]
for movement in movements:
    move(movement)

wn.mainloop()