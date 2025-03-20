import random, time, threading

def aStarSimulation(ui, maze):
    start, end = maze[random.randint(0, len(maze) - 1)][0], maze[random.randint(0, len(maze[0]) - 1)][len(maze) - 1]

    ui.drawCell(start, "green", maze)
    ui.drawCell(end, "red", maze)

    openSet = []
    closedSet = []

    cameFrom = []

    openSet.append(start)

    while len(openSet) > 0:
        # Looks for the spot with the lowest fscore
        lowestFIndex = 0
        for currentFIndex in range(len(openSet)):
            if openSet[currentFIndex].getf() < openSet[lowestFIndex].getf():
                lowestFIndex = currentFIndex
        current = openSet[lowestFIndex]

        # Checks if it got to the end
        if current is end:
            print("DONE")
            # Reconstruct path
            break

        del openSet[lowestFIndex]
        closedSet.append(current)

        for neighbourCoord in current.getNeighbours():
            neighbour = maze[neighbourCoord[0]][neighbourCoord[1]]
            if neighbour in closedSet:
                continue # Spot was already evaluated

            tryG = current.getg() + 1
            if neighbour not in openSet:
                openSet.append(neighbour)
            elif tryG >= neighbour.getg():
                continue # It's not a better path

            neighbour.setg(tryG)
            neighbour.setf(neighbour.getg() + neighbour.generateHeuristic(end))

        for openSetElement in openSet:
            ui.drawCell(openSetElement, "green", maze)

        for closedSetElement in closedSet:
            ui.drawCell(closedSetElement, "red", maze)

        ui.update()