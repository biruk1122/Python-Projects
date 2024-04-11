""" Create a Random Walk """

import turtle as b
import random

bim = b.Turtle()
b.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color

 
bim.pensize(10)
bim.speed("fastest")

directions = [0, 90, 180, 270]

for _ in range(300):
    bim.color(random_color())
    bim.forward(30)
    bim.setheading(random.choice(directions))
    