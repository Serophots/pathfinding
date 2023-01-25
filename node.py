from __future__ import annotations

import math
import turtle
from SETTINGS import GRID_SIZE, WIDTH, HEIGHT

def drawSquare(pen: turtle.Pen,
               x: int,
               y: int,
               ):
    pen.up()
    pen.goto(x * GRID_SIZE, y * GRID_SIZE)
    pen.down()
    pen.setheading(0)

    pen.forward(GRID_SIZE)
    pen.left(90)
    pen.forward(GRID_SIZE)
    pen.left(90)
    pen.forward(GRID_SIZE)
    pen.left(90)
    pen.forward(GRID_SIZE)
def fillSquare(pen: turtle.Pen,
               x: int,
               y: int,
               colour
               ):
    pen.fillcolor(colour)
    pen.begin_fill()
    drawSquare(pen, x, y)
    pen.end_fill()
    pen.up()


class Node:
    def __init__(self,
                 nodes: dict[int, dict[int, Node]],
                 pen: turtle.Pen,
                 position: (int, int),
                 ):
        self.nodes = nodes
        self.pen = pen
        self.position = position

        self.textPen = turtle.Turtle()
        self.textPen.hideturtle()

        self.isWall = False
        self.beenChecked = False

        self.fCost = 0
        self.hCost = 0
        self.gCost = 0
        self.parent = None

        drawSquare(pen, position[0], position[1])

    def calculateCostH(self, end: Node):
        hX, hY = ( abs(self.position[0] - end.position[0]), abs(self.position[1] - end.position[1]) )
        distance = 0

        if hX != 0 and hY != 0:
            #Diagonal steps
            if hX < hY:
                distance = hX * math.sqrt(1**2 + 1**2)
                hY -= hX
                hX = 0
            else:
                distance = hY * math.sqrt(1**2 + 1**2)
                hX -= hY
                hY = 0
        if hX == 0 and hY != 0:
            #Adjacent step
            distance += hY
            hY = 0
        elif hY == 0 and hX != 0:
            distance += hX
            hX = 0
        self.hCost = distance


    def calculateCostF(self): self.fCost = self.hCost + self.gCost

    def goto(self):
        self.pen.goto(self.position[0]*GRID_SIZE, self.position[1]*GRID_SIZE)
        self.pen.setheading(0)
        self.textPen.goto(self.position[0]*GRID_SIZE, self.position[1]*GRID_SIZE)
        self.textPen.setheading(0)

    def color(self, color):
        fillSquare(self.pen, self.position[0], self.position[1], color)

    def rawLabel(self, text: str, size: int = 12):
        self.goto()
        self.textPen.clear()
        self.textPen.write(text, font=('Arial', size, 'normal'))

    def wall(self):
        self.isWall = True
        self.color("black")

    def getAt(self, relativePosition: (int,int)) -> Node | None:
        absolutePosition = (self.position[0]+relativePosition[0], self.position[1]+relativePosition[1])
        try:
            return self.nodes[absolutePosition[0]][absolutePosition[1]]
        except KeyError:
            return

    def labelCosts(self):
        #F cost = g + h                   = middle
        #G cost = dist from starting node = top left
        #H cost = dist from ending node   = top right

        self.goto()
        self.textPen.clear()
        self.textPen.forward(GRID_SIZE/2)
        self.textPen.write(round(self.fCost*10), font=('Arial', 12, 'normal'), align='center')
        self.textPen.penup()

        self.textPen.left(180)
        self.textPen.forward(GRID_SIZE/4)
        self.textPen.right(90)
        self.textPen.forward(GRID_SIZE/2)
        self.textPen.write(round(self.gCost*10), font=('Arial', 8, 'normal'), align='center')
        self.textPen.penup()

        self.textPen.right(90)
        self.textPen.forward(GRID_SIZE/4)
        self.textPen.forward(GRID_SIZE/4)
        self.textPen.write(round(self.hCost*10), font=('Arial', 8, 'normal'), align='center')
        self.textPen.penup()
