import turtle
import config
from config import *
#for keybinds
def pos():
    turtle.goto(0,0)
def bg():
    if turtle.bgcolor() == "white":
        turtle.bgcolor("black")
    else:
        turtle.bgcolor("white")
def dot():
    turtle.dot(adot)
def circle():
    if turtle.isdown() == True:
        turtle.circle(ccircle)
    else:
        turtle.down()
        turtle.circle(ccircle)
        turtle.up()
def up():
    turtle.fd(go)
def left():
    turtle.lt(turn)
def right():
    turtle.rt(turn)
def back():
    turtle.bk(go)
def quitTurtles():
    turtle.bye()
def stamp():
    turtle.stamp()
def pup():
    if turtle.isdown() == True:
        turtle.up()
    else:
        turtle.down()

def tcolor():
    if turtle.color == 'blue':
        turtle.color('red', 'red')
def reset():
    turtle.reset()
    setup()
