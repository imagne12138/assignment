import turtle as t
from turtle import *

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)
        t.right(120)
        koch_curve(t, length, level-1)
        t.left(60)
        koch_curve(t, length, level-1)

t.speed(0)
t.penup()
t.goto(-150, 100)
t.pendown()

for i in range(3):
    koch_curve(t, 300, 4)   # 4阶分形雪花
    right(120)

t.done()




