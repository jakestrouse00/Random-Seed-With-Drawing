import random
from turtle import *


class Create:
    @staticmethod
    def drawing():
        turtle = Turtle()
        turtle.speed(0)
        screen = Screen()
        w = screen.window_width()
        h = screen.window_height()
        w, h = w // 2, h // 2
        for i in range(random.randint(5, 100)):
            x, y = turtle.pos()  # Get x, y positions.
            if abs(x) > w or abs(y) > h:  # Check if pen is outside of frame
                # set the pen back to 0, 0
                turtle.setx(0)
                turtle.sety(0)
            turtle.right(random.randint(10, 358))
            turtle.forward(random.randint(10, 200))
            turtle.left(random.randint(10, 358))
        ts = turtle.getscreen()
        j = ts.getcanvas().postscript()
        return j
