from turtle import Turtle, Screen
import random
biruk = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_polygon(sides, length):
    for _ in range(sides):
        biruk.color(random.choice(colours))
        biruk.forward(length)
        biruk.right(360/sides)


# Draw a triangle
draw_polygon(3,100)

# Draw a square
draw_polygon(4, 100)

# Draw a pentagon
draw_polygon(5, 100)

# Draw a hexagon
draw_polygon(6, 100)

# Draw a heptagon
draw_polygon(7, 100)

# Draw a octagon
draw_polygon(8, 100)

# Draw a nonagon
draw_polygon(9, 100)

# Draw a decagon
draw_polygon(10, 10)
screen = Screen()
screen.exitonclick()
