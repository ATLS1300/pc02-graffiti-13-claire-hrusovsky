#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Erika Andrade
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

up() #move to eye
goto(-17,115) # draws on left eye
down()
color("red")
dot(20) #red eye on left
up()
goto(45,125) #draws on right eye
dot(20) #red eye on right

up() #draw circle to start speech cloud
goto(80,50) 
down()
circle(10) #start of a speech bubble
up()
goto(115,80)
down()
circle(10) #second circle
up()
goto(140,110)
down()
circle(10) #third and final circle

up() # move to draw a speech bubble
goto(180,150)
down() #down to draw a rectangle speech bubble
forward(120) #Forward turtle by 120 
left(90) #Turn turtle left by 90 degree 
forward(80) 
left(90) 
forward(120)  
left(90) 
forward(80) 
left(90) #last side of rectangle

up() #write a message on speech bubble
goto(210,180) #try to center words
down()
color("black")
write("Aww poor people")

up() #move to his forhead
color("red")
pensize(7)
goto(-20,160) 
down()
forward(50) #draw an equilateral triangle

left(120) #turn left 120 degrees
forward(50)

left(120)
forward(50) #last side of triangle
done()

