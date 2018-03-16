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
# building the only possible case, the last one, without writing same edges more than once
movements = [
    (90, 100), (-45, 50 * math.sqrt(2)), (-90, 50 * math.sqrt(2)), (-135, 100),
    (135, 100 * math.sqrt(2)), (135, 100), (135, 100 * math.sqrt(2)), (135, 100)
]
for movement in movements:
    move(movement)

wn.mainloop()