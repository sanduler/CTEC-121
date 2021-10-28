# CTEC 121
# Ruben Sanduleac
# Module 6 / Problem Set 4
# Problem 2 (25 points)

'''
CAR SPECIFICATIONS
==================

Using the graphics library, draw a picture of the side view of a car. 
The car MUST include:

- 2 tires
- an area for windows and the roof
- a front and rear bumper
- You must Use all of the following object types and functions listed below:
    - Line
    - Circle
    - Rectangle
    - Polygon
    - setOutline
    - setFill

'''

import graphics


def main():
    # create the graphics window
    win = graphics.GraphWin('Problem 2 - Car', 800, 800)

    # Create the body of the car
    ractangleCar = graphics.Rectangle(graphics.Point(100, 600),graphics.Point(700,400))
    ractangleCar.setFill("Black")
    ractangleCar.setOutline("Yellow")
    ractangleCar.setWidth(3)
    ractangleCar.draw(win)

    # Create two tires
    center = graphics.Point(200,600)
    tire1rim = graphics.Circle(center,60)
    tire1rim.setFill("Gray")
    tire1rim.setWidth(20)
    tire1rim.draw(win)

    center = graphics.Point(600,600)
    tire2rim = graphics.Circle(center,60)
    tire2rim.setFill("Gray")
    tire2rim.setWidth(20)
    tire2rim.draw(win)

    # create red outline for the tires
    center = graphics.Point(200,600)
    tire1 = graphics.Circle(center,70)
    tire1.setOutline("Red")
    tire1.setWidth(2)
    tire1.draw(win)

    center = graphics.Point(600,600)
    tire2 = graphics.Circle(center,70)
    tire2.setOutline("Red")
    tire2.setWidth(2)
    tire2.draw(win)

    # roof
    p1 = graphics.Point(200,400)
    p2 = graphics.Point(350,270)
    p3 = graphics.Point(600,270)
    p4 = graphics.Point(700,400)
    roof = graphics.Polygon(p1,p2,p3,p4)
    roof.setFill("Black")
    roof.setOutline("Yellow")
    roof.setWidth(3)
    roof.draw(win)

    # windows
    window1 = graphics.Line(graphics.Point(350,270),graphics.Point(350,400))
    window1.setFill("Gray")
    window1.setWidth(2)
    window1.draw(win)

    window2 = graphics.Line(graphics.Point(600,270),graphics.Point(600,400))
    window2.setFill("Gray")
    window2.setWidth(2)
    window2.draw(win)

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()



main()
