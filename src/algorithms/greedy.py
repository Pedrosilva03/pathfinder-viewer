import random

def greedyAlgorithm(ui, maze):
    start, end = maze[random.randint(0, len(maze) - 1)][0], maze[random.randint(0, len(maze[0]) - 1)][len(maze) - 1]

    start.setWallStatus(False) # Makes sure that the start and the end are not walls
    end.setWallStatus(False)

    ui.drawCell(start, "green", maze)
    ui.drawCell(end, "red", maze)