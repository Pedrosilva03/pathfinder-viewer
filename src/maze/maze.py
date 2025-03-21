from maze.Spot import Spot
import random

rows = 50
cols = 50

def generateMaze():
    # Generate grid
    maze = []
    for row in range(rows):
        rowList = []
        for col in range(cols):
            rowList.append(Spot(row, col))
        maze.append(rowList)

    # Add obstacles

    for row in range(rows):
        for col in range(cols):
            maze[row][col].setWallStatus(random.randint(0, 3) == 3)

    # Add neighbours
    for row in range(rows):
        for col in range(cols):
            maze[row][col].createNeighbours(maze)

    return maze