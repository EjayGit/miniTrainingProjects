import turtle as t
import random

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

myTurtle = t.Turtle()
screen = t.Screen()
directions = [0, 90, 180, 270]
for _ in range(250):
    myTurtle.color(random_color())
    myTurtle.forward(40)
    myTurtle.setheading(random.choice(directions))


screen.exitonclick()