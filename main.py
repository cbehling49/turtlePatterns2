"""
Project Name: Turtle Patterns II
Author: Cody Behling
Due Date: 11/14/2020
Course: CS1400-X01

This program will ask for one input from a user to determine which scene is to be displayed.
It will then display a window and draw a picture using the turtle commands.
The picture will be of a landscape, containing three basic shapes: rectangle, triangle, circle
These shapes will be used on their own or together to add variety to the landscape.
The shapes will consist of different colors, sizes, and angles.
The scene is made up of shapes depicting the land, sky, mountains, sun, sun rays, a house, and a lake.
"""


import turtle


# user input
def getScene():
    scene = input("Enter one of the following: morning, afternoon, evening, night: ")
    return scene


# rectangle code
def rectangle(cody, width, height, tilt, tiltDirection, borderColor, fillColor):
    if tiltDirection == 'left':
        cody.left(tilt)
    elif tiltDirection == 'right':
        cody.right(tilt)
    cody.pencolor(borderColor)
    cody.fillcolor(fillColor)
    cody.begin_fill()
    sides = 4
    for i in range(0, sides):
        if(i + 1) % 2 == 0:
            cody.forward(height/2)
            cody.left(90)
        else:
            cody.forward(width)
            cody.left(90)
    cody.end_fill()
    if tiltDirection == 'left':
        cody.right(tilt)
    elif tiltDirection == 'right':
        cody.left(tilt)


# triangle code
def triangle(cody, sideLength, tilt, tiltDirection, borderColor, fillColor):
    if tiltDirection == 'left':
        cody.left(tilt)
    elif tiltDirection == 'right':
        cody.right(tilt)
    cody.pencolor(borderColor)
    cody.fillcolor(fillColor)
    cody.begin_fill()
    sides = 3
    for i in range(0, sides):
        cody.forward(sideLength)
        cody.left(120)
    cody.end_fill()
    if tiltDirection == 'left':
        cody.right(tilt)
    elif tiltDirection == 'right':
        cody.left(tilt)


# circle code
def circle(cody, radius, borderColor, fillColor):
    cody.pencolor(borderColor)
    cody.fillcolor(fillColor)
    cody.begin_fill()
    cody.circle(radius)
    cody.end_fill()


# allows the turtle to move to another location without drawing a line to get there
def goto(cody, x, y):
    cody.penup()
    cody.goto(x, y)
    cody.pendown()


def main():

    try:
        # turtle setup
        turtleScreen = turtle.Screen()
        cody = turtle.Turtle()

        # window setup
        width = 500
        height = 500
        maxWidth = width / 2
        maxHeight = height / 2
        scene = getScene()
        if scene != 'morning' and scene != 'afternoon' and scene != 'evening' and scene != 'night':
            print("Please enter one of the four options.")
            return

        # turtle dictionary
        turtleDict = {
            'skyColor': 'skyblue',
            'landColor': 'lightgreen',
            'sunColor': 'yellow',
            'sunRayColor': 'red',
            'sunPosition': 0,
            'sunRayPosition': (0 - (maxWidth / 6))
        }

        # scene selection
        if scene == 'morning':
            turtleDict['skyColor'] = 'lightskyblue'
            turtleDict['landColor'] = 'darkseagreen2'
            turtleDict['sunColor'] = 'lightyellow'
            turtleDict['sunRayColor'] = 'palegoldenrod'
            turtleDict['sunPosition'] = (maxWidth - ((maxWidth / 10) * 2))
            turtleDict['sunRayPosition'] = (maxWidth - (maxWidth / 2.75))
        elif scene == 'evening':
            turtleDict['skyColor'] = 'peachpuff'
            turtleDict['landColor'] = 'darkseagreen3'
            turtleDict['sunColor'] = 'orange'
            turtleDict['sunRayColor'] = 'darkred'
            turtleDict['sunPosition'] = (maxWidth - ((maxWidth / 10) * 2)) * -1
            turtleDict['sunRayPosition'] = (maxWidth - (maxWidth / 28)) * -1
        elif scene == 'night':
            turtleDict['skyColor'] = 'darkslategray'
            turtleDict['landColor'] = 'darkseagreen4'
            turtleDict['sunColor'] = 'white'
            turtleDict['sunRayColor'] = 'whitesmoke'

    except ValueError:
        print("Enter positive integers for width and height.")
        return
    if width < 1 or height < 1:
        print("Enter positive integers for width and height.")
        return

    turtleScreen.setup(width + 30, height + 30)

    # sky
    goto(cody, (maxWidth * -1), 0)
    rectangle(cody, width, height, 1, 'right', turtleDict['skyColor'], turtleDict['skyColor'])

    # land
    goto(cody, (maxWidth * -1), (maxHeight * -1))
    rectangle(cody, width, height, 1, 'left',  turtleDict['landColor'], turtleDict['landColor'])

    # first mountain
    goto(cody, (maxWidth / 2 * -1), 0)
    triangle(cody, (maxWidth / 2), 1.5, 'left', 'black', 'slategrey')

    # second mountain
    goto(cody, 0, 0)
    triangle(cody, (maxWidth / 2), 1.5, 'right', 'darkslategrey', 'lightslategrey')

    # sun ray
    if scene != 'night':
        goto(cody,  turtleDict['sunRayPosition'], (maxHeight - ((maxHeight / 10) * 3)))
        triangle(cody, (maxWidth / 3), 0, 'right',  turtleDict['sunRayColor'], turtleDict['sunRayColor'])

    # sun
    goto(cody,  turtleDict['sunPosition'], (maxHeight - ((maxHeight / 10) * 3)))
    circle(cody, (maxWidth / 10),  turtleDict['sunColor'], turtleDict['sunColor'])

    # lake
    goto(cody, 0, ((maxWidth / 1.25) * -1))
    circle(cody, (maxWidth / 3), 'blue', 'steelblue')

    # house base
    goto(cody, ((maxWidth / 3) * 2), 0)
    rectangle(cody, (maxWidth / 8), (maxHeight / 6), 0, 'left', 'tan4', 'tan3')

    # house roof
    goto(cody, ((maxWidth / 3) * 1.9), (maxHeight / 12))
    triangle(cody, ((maxWidth / 8) * 1.5), 0, 'right', 'seashell4', 'snow4')

    print("To exit the program, please click on the screen.")
    turtleScreen.exitonclick()


if __name__ == "__main__":
    main()
