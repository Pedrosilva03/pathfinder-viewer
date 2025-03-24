import random, time
import sys

sys.setrecursionlimit(10**6)

def dfsSimulation(ui, maze, start, end):
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
            ui.update()
            time.sleep(0.01)
        print("DFS done")
    else:
        print("No path found")