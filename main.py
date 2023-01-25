import turtle
from SETTINGS import WIDTH,HEIGHT,GRID_SIZE
from node import Node
from pathfinder import pathfind, triggerUpdate

#Stop screen refreshes
turtle.tracer(0,0)

#Screen + pen
screen = turtle.getscreen()
screen.setworldcoordinates(-1,-1, screen.window_width()-1, screen.window_height()-1)
pen = turtle.Turtle()
pen.hideturtle()

#Write text to top
textTurtle = turtle.Turtle()
textTurtle.hideturtle()
def write(text: str):
    textTurtle.clear()
    textTurtle.goto(GRID_SIZE/4, (HEIGHT+0.25)*GRID_SIZE)
    textTurtle.write(text, font=('Arial', 16, 'normal'))
    textTurtle.penup()

#Draw grid
nodes = {}
for X in range(WIDTH):
    nodes[X] = {}
    for Y in range(HEIGHT):
        nodes[X][Y] = Node(nodes, pen, (X,Y))

#Set up the start,end,walls
startNode = False
endNode = False
drawingWalls = False
write("Click on the starting node")

def onclick(x: float, y: float):
    global startNode, endNode, drawingWalls

    try:
        clickedNode = nodes[x//GRID_SIZE][y//GRID_SIZE]
        if not startNode:
            startNode = clickedNode
            startNode.color("blue")
            startNode.rawLabel("A")
            write("Click on the ending node")
        elif not endNode:
            endNode = clickedNode
            endNode.color("blue")
            endNode.rawLabel("B")
            drawingWalls = True
            write("Click to draw walls. Click outside the grid to finish")
        elif drawingWalls:
            clickedNode.wall()
    except KeyError:
        if drawingWalls:
            drawingWalls = False
            write("Click outside the grid to progress the algorithm")
            pathfind(startNode, endNode)
        else:
            triggerUpdate()



    turtle.update()
turtle.onscreenclick(onclick)

turtle.done()