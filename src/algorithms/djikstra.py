import random

# This is pretty much a BFS but using a random cost for each jump instead of a constant one
def djikstraSimulation(ui, maze):
    start, end = maze[random.randint(0, len(maze) - 1)][0], maze[random.randint(0, len(maze[0]) - 1)][len(maze) - 1]

    start.setWallStatus(False) # Makes sure that the start and the end are not walls
    end.setWallStatus(False)

    ui.drawCell(start, "green", maze)
    ui.drawCell(end, "red", maze)

    nodesQueue = []
    visited = []

    cameFrom = []

    start.setDistance(0)
    nodesQueue.append(start)

    while len(nodesQueue) > 0:
        # Gets the node with the shortest cost
        current = nodesQueue[0]
        currentIndex = 0
        nodeIndex = 0
        for node in nodesQueue:
            if node.getDistance() < current.getDistance():
                current = node
                currentIndex = nodeIndex
            nodeIndex += 1

        if current is end:
            while True:
                cameFrom.append(current)
                if current.getDistance() == 0:
                    break

                currentShortestCoord = current.getNeighbours()[0]
                currentShortest = maze[currentShortestCoord[0]][currentShortestCoord[1]]
                for neighbourCoord in current.getNeighbours():
                    neighbour = maze[neighbourCoord[0]][neighbourCoord[1]]
                    if neighbour.getDistance() < currentShortest.getDistance():
                        currentShortest = neighbour

                current = currentShortest
            break


        visited.append(current)
        del nodesQueue[currentIndex]
        for neighbourCoord in current.getNeighbours():
            neighbour = maze[neighbourCoord[0]][neighbourCoord[1]]
            if neighbour not in visited and not neighbour.getWallStatus() and neighbour not in nodesQueue:
                neighbour.setCameFrom(current)
                neighbour.setDistance(current.getDistance() + random.randint(1, 10))
                nodesQueue.append(neighbour)

        for queuedElement in nodesQueue[-8:]:
            ui.drawCell(queuedElement, "green", maze)

        ui.drawCell(visited[-1], "red", maze)

        ui.update()

    # Draws the way back

    if len(cameFrom) == 0:
        print("No path found")
    else:
        for pathSpot in cameFrom:
            ui.drawCell(pathSpot, "blue", maze)
        print("Djikstra done")