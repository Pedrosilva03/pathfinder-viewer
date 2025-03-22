import random
import sys

sys.setrecursionlimit(10**6)

def dfsSimulation(ui, maze):
    start, end = maze[random.randint(0, len(maze) - 1)][0], maze[random.randint(0, len(maze[0]) - 1)][len(maze) - 1]

    start.setWallStatus(False) # Makes sure that the start and the end are not walls
    end.setWallStatus(False)

    ui.drawCell(start, "green", maze)
    ui.drawCell(end, "red", maze)

    visitedNodes = []
    nodesToVisit = []

    path = []

    def recursiveChecking(current):
        visitedNodes.append(current)
        for neighbourCoord in current.getNeighbours():
            neighbour = maze[neighbourCoord[0]][neighbourCoord[1]]
            if neighbour in visitedNodes or neighbour.getWallStatus():
                continue
            visitedNodes.append(neighbour)
            ui.drawCell(visitedNodes[-1], "red", maze)
            ui.update()
            if neighbour is end:
                return True
            if recursiveChecking(neighbour):
                path.append(neighbour)
                return True
        return False
    
    if recursiveChecking(start):
        for pathSpot in path:
            ui.drawCell(pathSpot, "blue", maze)
        print("DFS done")
    else:
        print("No path found")