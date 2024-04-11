""" Draw a Spirograph """

import turtle as b
import random


bim = b.Turtle()
b.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


def draw_spirograph(size_of_graph):
    for _ in range(100):
        bim.speed("fastest")
        bim.color(random_color())
        bim.circle(100)
        bim.setheading(bim.heading() + size_of_graph)


draw_spirograph(5)

screen = b.Screen()
screen.exitonclick()
