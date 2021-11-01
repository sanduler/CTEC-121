# CTEC 121
# Ruben Sanduleac
# Module 6 / Problem Set 4
# Problem 3 (25 POINTS)

"""
DRAW THESE LEGOS
================

Using the graphics library, develop a Python program to draw 
the set of LEGOS provided in this assignment.

You will find a picture of the LEGO's in a file named LEGOS.png or LEGOS.pdf.

Be sure to create one LEGO and then use the .clone() method whenever possible to create the other five.
"""

import graphics
import random

def main():
    # create the graphics window
    win = graphics.GraphWin('Problem 3 - Lego', 725, 650)

    #random color
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)

    # initial lego
    Lego = graphics.Rectangle(graphics.Point(20, 200),graphics.Point(300,100))
    # fills the lego
    Lego.setFill(graphics.color_rgb(r,g,b))
    # creates an outline around the block of the lego
    Lego.setOutline("Black")
    # sets the width of the line
    Lego.setWidth(3)
    Lego.draw(win)

    # creates the top point of the lego 
    Top = graphics.Rectangle(graphics.Point(40, 90),graphics.Point(60,100))
    Top.setOutline("Black")
    # sets the color of the top of the lego
    Top.setFill(graphics.color_rgb(r,g,b))
    # sets the width of the line of the top of the lego
    Top.setWidth(3)

    # create a for loop that will create 3 more pieces of the top of the lego
    # set the inital x location of 0
    xLocation = 0
    # use the for loop to loop the clone of the top of the lego
    for x in range(1, 6):
        firstTop = Top.clone()
        # starts at the x location of 0
        firstTop.move(xLocation,0)
        # creates a color based on the random colors found above
        firstTop.setFill(graphics.color_rgb(r,g,b))
        # draws the a top of the lego in the every interfval of the for loop
        firstTop.draw(win)
        # increments the x location 55 
        xLocation = xLocation + 55

    #random color
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)

    Lego2 = Lego.clone()
    Lego2.move(400,0)
    Lego2.setFill(graphics.color_rgb(r,g,b))
    Lego2.draw(win)

    xLocation = 400
    for x in range(1, 6):
        firstTop = Top.clone()
        firstTop.move(xLocation,0)
        firstTop.setFill(graphics.color_rgb(r,g,b))
        firstTop.draw(win)
        xLocation = xLocation + 55

    #random color
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)

    Lego3 = Lego.clone()
    Lego3.move(0,200)
    Lego3.setFill(graphics.color_rgb(r,g,b))
    Lego3.draw(win)

    xLocation = 0
    for x in range(1, 6):
        firstTop = Top.clone()
        firstTop.move(xLocation,200)
        firstTop.setFill(graphics.color_rgb(r,g,b))
        firstTop.draw(win)
        xLocation = xLocation + 55

    #random color
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)

    Lego4 = Lego.clone()
    Lego4.move(400,200)
    Lego4.setFill(graphics.color_rgb(r,g,b))
    Lego4.draw(win)

    xLocation = 400
    for x in range(1, 6):
        firstTop = Top.clone()
        firstTop.move(xLocation,200)
        firstTop.setFill(graphics.color_rgb(r,g,b))
        firstTop.draw(win)
        xLocation = xLocation + 55

    #random color
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)

    Lego3 = Lego.clone()
    Lego3.move(0,400)
    Lego3.setFill(graphics.color_rgb(r,g,b))
    Lego3.draw(win)

    xLocation = 0
    for x in range(1, 6):
        firstTop = Top.clone()
        firstTop.move(xLocation,400)
        firstTop.setFill(graphics.color_rgb(r,g,b))
        firstTop.draw(win)
        xLocation = xLocation + 55

    #random color
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)

    Lego4 = Lego.clone()
    Lego4.move(400,400)
    Lego4.setFill(graphics.color_rgb(r,g,b))
    Lego4.draw(win)

    xLocation = 400
    for x in range(1, 6):
        firstTop = Top.clone()
        firstTop.move(xLocation,400)
        firstTop.setFill(graphics.color_rgb(r,g,b))
        firstTop.draw(win)
        xLocation = xLocation + 55    

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


main()
