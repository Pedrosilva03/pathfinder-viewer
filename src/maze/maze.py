from maze.Spot import Spot

rows = 25
cols = 25

def generateMaze():
    # Generate grid
    maze = []
    for row in range(rows):
        rowList = []
        for col in range(cols):
            rowList.append(Spot(row, col))
        maze.append(rowList)

    # Add obstacles

    # Add neighbours
    for row in range(rows):
        for col in range(cols):
            maze[row][col].createNeighbours(maze)

    return maze