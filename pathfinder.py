import math, time
import turtle

from node import Node

update = False
def triggerUpdate():
  global update
  update = True


def bestNode(open: list[Node]) -> Node:
    # Find the lowest f cost
    bestCostF = 9999
    for node in open:
        if node.fCost < bestCostF:
            bestCostF = node.fCost
    fNodes = [node for node in open if node.fCost == bestCostF]
    if len(fNodes) == 1: return fNodes[0]

    # Of those, find the lowest h cost
    bestCostH = 9999
    for node in fNodes:
        if node.hCost < bestCostH:
            bestCostH = node.hCost
    hNodes = [node for node in fNodes if node.hCost == bestCostH]

    return hNodes[0] #Typically here there'll only be 1 node, but if there's multiple there is no further way to choose which is better

def pathfind(start: Node, end: Node):
    global update
    open = [start]
    closed = []

    #Find path
    while True:
        if end.parent is not None: break

        current = bestNode(open)

        current.color('red')
        open.remove(current)
        closed.append(current)


        for direction in [(+1, 0), (-1, 0), (0, +1), (0, -1), (+1, -1), (+1, +1), (-1, -1), (-1, +1)]:
            neighbour = current.getAt(direction)

            if neighbour and (not neighbour.isWall) and (not neighbour in closed):
                supposedCostG = current.gCost + math.sqrt(direction[0]**2 + direction[1]**2)
                if (not neighbour in open) or (supposedCostG < neighbour.gCost):
                    neighbour.gCost = supposedCostG
                    neighbour.calculateCostH(end)
                    neighbour.calculateCostF()

                    neighbour.color('green')
                    neighbour.labelCosts()

                    neighbour.parent = current
                    if not neighbour in open: open.append(neighbour)

        # turtle.update()
        # time.sleep(0.1)

        while True:
            time.sleep(0.1)
            turtle.update()
            if update:
                update = False
                break

    #Outline selected path
    found = end
    while True:
        if found.parent is None: break
        found = found.parent
        found.color('blue')
