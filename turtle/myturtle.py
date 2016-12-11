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
import config
import turtle
from commands import *
#set distance, turing degrees, dot size ect.



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

# def __main__():
    #finally runs the program
setup()
print("keybinds:\narrow keys to move\nescape to quit\ni to toggle drawing\nb to toggle black or white background\np to return to start\nr ro reset\nspace to stamp\nd to place dot\nc to draw circle")
turtle.mainloop()
