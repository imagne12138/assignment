# Import Turtle graphic module and all its functions, which allows dirct usage of functions like circle(), bgcolor()...
from turtle import *

# Define a recursion function to draw the snowflake
def draw_snowflake(length, level):
    # The 0th recursion is a straight line
    if level == 0:
        forward(length)
    else:
        # Divide the length by 3
        length /= 3.0
        # Recursively replace the middle part with two sides of a triangle
        draw_snowflake(length, level-1)
        # The recursive step: draw four smaller segments with turns (left 60°, right 120°, left 60°),
        # After forward, turn 60 degrees left 
        left(60)
        # After 60 degrees left, forward again
        draw_snowflake(length, level-1)
        # 120 degrees right
        right(120)
        # forward again
        draw_snowflake(length, level-1)
        # left 60 degrees
        left(60)
        # forward again, one level is finished
        draw_snowflake(length, level-1)
        # When the lowest level is finished, go back to the higher level and repeat, the pattern repeats itself until all levels iterated 

# Set the background color as black
bgcolor("black")
# Set the pen color as white
pencolor("white")
# Set the speed as the fastest 
speed(0)
# Pen up, stop drawing
penup()
# Go to a proper start point(-150, 100) is a relatively proper position to start the whole pattern
goto(-150, 100)
# Pen down, begin drawing
pendown()

# The index is not important, so use _ here and loop for 3 times (0, 1, 2)
for _ in range(3):
	# Invoke the function for 3 times, choose 4 level and length of 300
    draw_snowflake(300, 4)
    # After the recursion is finished, turn right 120 degrees to enclose the pattern, a closed snowflake is formed
    right(120)

exitonclick()
