from maze.Spot import Spot

rows = 10
cols = 10

def generateMaze():
    # Generate grid
    maze = []
    for col in range(cols):
        colList = []
        for row in range(rows):
            colList.append(Spot(col, row))
        maze.append(colList)

    # Add obstacles

    return maze