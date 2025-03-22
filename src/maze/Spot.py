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

        self.wall = False

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
        # Vizinhos ortogonais (cima, baixo, esquerda, direita)
        if self.i > 0:
            neighbours.append((self.i - 1, self.j))  # Cima
        if self.i < len(maze) - 1:
            neighbours.append((self.i + 1, self.j))  # Baixo
        if self.j > 0:
            neighbours.append((self.i, self.j - 1))  # Esquerda
        if self.j < len(maze[0]) - 1:
            neighbours.append((self.i, self.j + 1))  # Direita

        # Vizinhos diagonais
        if self.i > 0 and self.j > 0:
            neighbours.append((self.i - 1, self.j - 1))  # Superior esquerdo
        if self.i > 0 and self.j < len(maze[0]) - 1:
            neighbours.append((self.i - 1, self.j + 1))  # Superior direito
        if self.i < len(maze) - 1 and self.j > 0:
            neighbours.append((self.i + 1, self.j - 1))  # Inferior esquerdo
        if self.i < len(maze) - 1 and self.j < len(maze[0]) - 1:
            neighbours.append((self.i + 1, self.j + 1))  # Inferior direito
        self.neighbours = neighbours
    
    #####
    def generateHeuristic(self, end):
        if end is self:
            self.h = 0
            return self.h
        self.h = abs(self.i - end.i) + abs(self.j - end.j)
        return self.h
    
    #####
    def setWallStatus(self, status):
        self.wall = status
    
    def getWallStatus(self):
        return self.wall