import random

def djikstraSimulation(ui, maze):
    start, end = maze[random.randint(0, len(maze) - 1)][0], maze[random.randint(0, len(maze[0]) - 1)][len(maze) - 1]

    ui.drawCell(start, "green", maze)
    ui.drawCell(end, "red", maze)