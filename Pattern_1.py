from turtle import *
from random import randint

def draw_circles():
    bgcolor("black")
    x = 1
    speed(0)
    while x < 200:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        colormode(255)
        pencolor(r, g, b)
        circle(5 + x)
        rt(59.991)
        x = x + 1
    exitonclick()

draw_circles()
