import random

class Spot:
    def __init__(self, i, j):
        self.i = i
        self.j = j

        self.cell = None

        self.neighbours = []

        self.distSource = 999999

        self.f = 0
        self.g = 0
        self.h = 0

        self.cameFrom = None

        self.wall = self.setWallStatus()

    #####
    def geti(self):
        return self.i
    
    def getj(self):
        return self.j
    
    #####
    def getCell(self):
        return self.cell
    
    def setCell(self, cell):
        self.cell = cell
    
    #####
    def getNeighbours(self):
        return self.neighbours
    
    def getDistance(self):
        return self.distSource
    
    def setDistance(self, dist):
        self.distSource = dist
    
    #####
    def getf(self):
        return self.f
    
    def setf(self, f):
        self.f = f
    
    #####
    def getg(self):
        return self.g
    
    def setg(self, g):
        self.g = g
    
    #####
    def geth(self):
        return self.h
    
    #####
    def setCameFrom(self, spot):
        self.cameFrom = spot

    def getCameFrom(self):
        return self.cameFrom
    
    #####
    def createNeighbours(self, maze):
        neighbours = []
        if self.i > 0:
            neighbours.append((self.i - 1, self.j))
        if self.i < len(maze) - 1:
            neighbours.append((self.i + 1, self.j))
        if self.j > 0:
            neighbours.append((self.i, self.j - 1))
        if self.j < len(maze[0]) - 1:
            neighbours.append((self.i, self.j + 1))
        self.neighbours = neighbours
    
    #####
    def generateHeuristic(self, end):
        self.h = abs(self.i - end.i) + abs(self.j - end.j)
        return self.h
    
    #####
    def setWallStatus(self):
        if random.randint(0, 3) == 3:
            return True
        return False
    
    def getWallStatus(self):
        return self.wall