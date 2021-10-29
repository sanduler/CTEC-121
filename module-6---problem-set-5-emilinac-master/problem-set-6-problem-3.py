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
    win = graphics.GraphWin('Problem 3 - Lego', 800, 650)

    #random color
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)

    # initial lego
    Lego = graphics.Rectangle(graphics.Point(20, 200),graphics.Point(300,100))
    Lego.setFill(graphics.color_rgb(r,g,b))
    Lego.setOutline("Black")
    Lego.setWidth(3)
    Lego.draw(win)

    Top = graphics.Rectangle(graphics.Point(40, 90),graphics.Point(60,100))
    Top.setOutline("Black")
    Top.setFill(graphics.color_rgb(r,g,b))
    Top.setWidth(3)

    xLocation = 0
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

    Lego2 = Lego.clone()
    Lego2.move(400,0)
    Lego2.setFill(graphics.color_rgb(r,g,b))
    Lego2.draw(win)


    xLocation = 400

    for x in range(1, 6):
        secondTop = Top.clone()
        secondTop.move(xLocation,0)
        secondTop.setFill(graphics.color_rgb(r,g,b))
        secondTop.draw(win)
        xLocation = xLocation + 55


    i = 1
    moveY = 200

    # create 5 more cubes
 
    while i < 3: 
        #random color
        r =random.randint(0,255)
        g =random.randint(0,255)
        b =random.randint(0,255)

        LegoCloneY = Lego.clone()
        LegoCloneY.move(0,moveY)
        LegoCloneY.setFill(graphics.color_rgb(r,g,b))
        LegoCloneY.draw(win)

        b = 1
        moveX = 400
        while b < 3:
            LegoCloneX = LegoCloneY.clone()
            LegoCloneX.move(moveX,0)
            LegoCloneX.setFill(graphics.color_rgb(r,g,b))
            LegoCloneX.draw(win)
            b = b + 1
            
            xLocation = 0
            for x in range(1, 6):
                firstTop = Top.clone()
                firstTop.move(xLocation,200)
                firstTop.draw(win)
                firstTop.setFill(graphics.color_rgb(r,g,b))
                xLocation = xLocation + 55
            
        b = b + 1
        moveY = moveY + 200

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


main()
