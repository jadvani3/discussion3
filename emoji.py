from string import whitespace
from turtle import *

### write all new functions here ###

def face(jai, color, rad):
    jai.fillcolor(color)
    jai.begin_fill()
    jai.circle(rad)
    jai.end_fill()
    jai.penup()


def eye(jai, color, rad):
    jai.penup()
    jai.goto(-50,70)
    jai.pendown()
    jai.color(color)
    jai.begin_fill()
    jai.circle(30,360)
    jai.end_fill()
    jai.penup()

def eye2(jai, color, rad):
    jai.penup()
    jai.goto(50,70)
    jai.pendown()
    jai.color(color)
    jai.begin_fill()
    jai.circle(30,360)
    jai.end_fill()
    jai.penup()



def draw_emoji(turtle):
    """
    Write a function to draw an emoji.
    """

    pass

def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_emoji.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.

    """
    screen= Screen()
    screen.setup(400,400)
    jai = Turtle()
    jai.speed(0)
    face(jai, "red", 100)
    eye(jai, "white", 30)
    eye2(jai, "white", 30)
    screen.exitonclick()
    
# Only run the main function if this file is executed (not imported)
if __name__ == '__main__':
    main()


