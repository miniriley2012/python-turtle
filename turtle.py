#!/usr/bin/env python

# arrow keys to move
# escape to quit
# i to toggle drawing
# b to toggle black or white background
# p to return to start
# r ro reset
# space to stamp
# d to place dot
# c to draw circle

import turtle
#set distance, turing degrees, dot size ect.
_turn = 45
_go = 45
_dot = 20
_circle = 20


#for keybinds
def pos():
    turtle.goto(0,0)
def bg():
    if turtle.bgcolor() == "white":
        turtle.bgcolor("black")
    else:
        turtle.bgcolor("white")
def dot():
    turtle.dot(_dot)
def circle():
    if turtle.isdown() == True:
        turtle.circle(_circle)
    else:
        turtle.down()
        turtle.circle(_circle)
        turtle.up()
def up():
    turtle.fd(_go)
def left():
    turtle.lt(_turn)
def right():
    turtle.rt(_turn)
def back():
    turtle.bk(_go)
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

#sets up turtle
def setup():
    wn = turtle.Screen()
    turtle.up()
    # turtle.bgcolor("black")
    turtle.shape("turtle")
    turtle.color("blue")
    wn.listen()
    wn.onkey(bg, "b")
    wn.onkey(pos, "p")
    wn.onkey(up, "Up")
    wn.onkey(left, "Left")
    wn.onkey(right, "Right")
    wn.onkey(back, "Down")
    wn.onkey(stamp, "space")
    wn.onkey(reset, "r")
    wn.onkey(pup, "i")
    wn.onkey(dot, "d")
    wn.onkey(circle, "c")
    wn.onkey(quitTurtles, "Escape")

#finally runs the program
setup()
print("keybinds:\narrow keys to move\nescape to quit\ni to toggle drawing\nb to toggle black or white background\np to return to start\nr ro reset\nspace to stamp\nd to place dot\nc to draw circle")
turtle.mainloop()
