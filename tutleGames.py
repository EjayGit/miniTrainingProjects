from turtle import Turtle, Screen


myTurtle = Turtle()
screen = Screen()

#def moveForward():
#    myTurtle.forward(50)

def up():
    myTurtle.setheading(90)
    myTurtle.forward(40)

def down():
    myTurtle.setheading(270)
    myTurtle.forward(40)

def right():
    myTurtle.setheading(0)
    myTurtle.forward(40)

def left():
    myTurtle.setheading(180)
    myTurtle.forward(40)

def red():
    myTurtle.color("red")

def blue():
    myTurtle.color("blue")

def green():
    myTurtle.color("green")

def black():
    myTurtle.color("black")

screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")
screen.onkey(fun=black, key="c")
screen.onkey(fun=red, key="r")
screen.onkey(fun=green, key="g")
screen.onkey(fun=blue, key="b")


#screen.onkey(fun=moveForward, key='space')
#name = screen.textinput("Name", "What is your name")
#print(name)

screen.exitonclick()