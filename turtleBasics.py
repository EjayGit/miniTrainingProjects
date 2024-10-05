import turtle
from turtle import Turtle, Screen
import random

newTurtle = Turtle()
screen = Screen()
newTurtle.shape("turtle")
newTurtle.forward(100)
newTurtle.right(90)
newTurtle.forward(100)
newTurtle.goto(-100,-100)
newTurtle.home()
newTurtle.dot(100, "red")
newTurtle.hideturtle()
newTurtle.goto(100,100)
newTurtle.begin_fill()
newTurtle.pensize(10)
newTurtle.circle(100)
newTurtle.end_fill()

sides = 3
def randomColour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour

def drawPolygon(sides):
    angle = 360/sides
    for _ in range(sides):
        newTurtle.forward(100)
        newTurtle.right(angle)

#newTurtle.pencolor(randomColour())
drawPolygon(3)
newTurtle.bgcolor(randomColour())

screen.exitonclick()