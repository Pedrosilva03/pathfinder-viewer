import random, time

def greedySimulation(ui, maze, start, end):
    openSet = []
    closedSet = []

    path = []

    openSet.append(start)

    while len(openSet) > 0:
        # Get the node with the less cost left
        current = openSet[0]
        currentIndex = 0
        index = 0
        for queuedNode in openSet:
            if queuedNode.getDistanceLeft() < current.getDistanceLeft():
                current = queuedNode
                currentIndex = index
            index += 1

        if current is end:
            while True:
                path.append(current)
                if current is start:
                    break
                current = current.getCameFrom()
            break

        closedSet.append(current)
        del openSet[currentIndex]

        for neighbourCoord in current.getNeighbours():
            neighbour = maze[neighbourCoord[0]][neighbourCoord[1]]
            if neighbour not in closedSet and not neighbour.getWallStatus():
                neighbour.setCameFrom(current)
                openSet.append(neighbour)

        for queuedElement in openSet[-8:]:
            ui.drawCell(queuedElement, "green", maze)

        ui.drawCell(closedSet[-1], "red", maze)

        ui.update()

    # Draws the way back

    if len(path) == 0:
        print("No path found")
    else:
        for pathSpot in path:
            ui.drawCell(pathSpot, "blue", maze)
            ui.update()
            time.sleep(0.01)
        print("Greedy done")
