from maze.Spot import Spot

rows = 10
cols = 10

def generateMaze():
    # Generate grid
    maze = [[Spot() for row in range(rows)] for col in range(cols)]

    # Add obstacles

    return maze