# CTEC 121
# Ruben Sanduleac
# Module 6 / Problem Set 4
# Problem 1 (25 points)

'''
SNOWMAN SPECIFICATIONS
=======================

Using the starter code provided, write a Python program that will create a snowman.
Be sure to change YOUR NAME to your first and last name

- The snowman must contain 3 circles for the body.
- The snowman must have two eyes on its face drawn with circles.
- The snowman must have a nose made out of a tirangle and it must be colored orange.
- The snowman must have a hat made out of a rectangle and a line (a top hat).
- The hat must be filled with the color black.
- The snowman must have two arms drawn using lines.

'''

import graphics
import tkinter


def snowman():
    # create the graphics window
    win = graphics.GraphWin('Problem 1 - Snowman', 800, 800)


    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circle3

    center = graphics.Point(400,250)
    circle1 = graphics.Circle(center,60)
    circle1.setFill("White")
    circle1.setWidth(4)
    circle1.draw(win)

    center2 = graphics.Point(400,400)
    circle2 = graphics.Circle(center2,90)
    circle2.setFill("White")
    circle2.setWidth(4)
    circle2.draw(win)

    center3 = graphics.Point(400,610)
    circle3 = graphics.Circle(center3,120)
    circle3.setFill("White")
    circle3.setWidth(4)
    circle3.draw(win)


    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2

    center = graphics.Point(370,230)
    eye1 = graphics.Circle(center, 10)
    eye1.setFill("Black")
    eye1.draw(win)

    center = graphics.Point(430,230)
    eye2 = graphics.Circle(center, 10)
    eye2.setFill("Black")
    eye2.draw(win)

    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose

    p1 = graphics.Point(400,250)
    p2 = graphics.Point(400,270)
    p3 = graphics.Point(500,250)
    nose = graphics.Polygon(p1,p2,p3)
    nose.setFill("Orange")
    nose.draw(win)

    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat

    hat = graphics.Rectangle(graphics.Point(350, 200),graphics.Point(450,70))
    hat.setFill("Black")
    hat.draw(win)

    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline

    hatline = graphics.Line(graphics.Point(300,200),graphics.Point(500,200))
    hatline.setFill("Black")
    hatline.setWidth(4)
    hatline.draw(win)

    # draw two arms that connect to the body of the snowman
    # name the line objects leftArm and rightArm

    leftArm = graphics.Line(graphics.Point(200,420),graphics.Point(325,350))
    leftArm.setFill("Black")
    leftArm.setWidth(4)
    leftArm.draw(win)

    rightArm = graphics.Line(graphics.Point(485,370),graphics.Point(610,300))
    rightArm.setFill("Black")
    rightArm.setWidth(4)
    rightArm.draw(win)

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()
