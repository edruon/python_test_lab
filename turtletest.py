# Turtle code example from the Python documentation
#from turtle import *
import turtle
drawing = turtle.Turtle()
drawing.speed(0)
drawing.color('red', 'yellow')
drawing.begin_fill()
while True:
    drawing.forward(200)
    drawing.left(170)
    if abs(drawing.pos()) < 1:
        break
drawing.end_fill()
#turtle.exitonclick()
turtle.done()
