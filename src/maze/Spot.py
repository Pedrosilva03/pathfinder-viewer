class Spot:
    def __init__(self, i, j):
        self.i = i
        self.j = j

        self.neighbours = []

        self.f = 0
        self.g = 0
        self.h = 0

    def geti(self):
        return self.i
    
    def getj(self):
        return self.j
    
    def getNeighbours(self):
        return self.neighbours
    
    def getf(self):
        return self.f
    
    def setf(self, f):
        self.f = f
    
    def getg(self):
        return self.g
    
    def setg(self, g):
        self.g = g
    
    def geth(self):
        return self.h
    
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
    
    def generateHeuristic(self, end):
        self.h = abs(self.i - end.i) + abs(self.j + end.j)
        return self.h