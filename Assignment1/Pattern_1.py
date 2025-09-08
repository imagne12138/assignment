# Import Turtle graphic module and all its functions, which allows dirct usage of functions like cicle(), bgcolor()...
from turtle import *
# Used to generate random RGB color values
from random import randint

def draw_circles():
    # Set background color as black
    bgcolor("black")
    # Set speed of the tutrle to the fastest
    speed(0)
    # Set the color mode as 0~255 integer values instead of 0~1
    colormode(255)
    # Initialize loop counter variable
    x = 0
    # Loop for 200 times (0, 1, 2, 3, ..., 199)
    while x < 200:
    # Generating color combinations randomly
        r = randint(0, 255) # The red component
        g = randint(0, 255) # The green component
        b = randint(0, 255) # The Blue component
        # A random pen color using 3 values between 0~255 generated before
        pencolor(r, g, b)
        # Draw a circle and increase the circle radius by 1 every iteration, initially 5
        circle(5 + x)
        # Rotate right by 60 degrees every time
        rt(60)
        # Increase the x value by 1 every loop
        x += 1
    # Keep the window open until exit button clicked
    exitonclick()
# Invoke the function defined above to start drawing
draw_circles()
